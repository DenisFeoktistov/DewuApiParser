# В этой папке будет реализована обработка товара исключительно по неполной API пойзона: https://spucdn.dewu.com/dewu/commodity/detail/simple/{spuId}.json
# Формат входного productInfo: данные JSON по ссылке выше.
import json
import re

from pureApiParser.brandProcess import brandProcess
from pureApiParser.categoriesProcess import categoriesProcess
from pureApiParser.collaborationsProcess import collaborationsProcess
from pureApiParser.connectSizeTables import connectSizeTables
from pureApiParser.dateProcess import dateProcess
from pureApiParser.gendersProcess import gendersProcess
from pureApiParser.linesProcess import linesProcess
from pureApiParser.nameProcess import nameProcess
from pureApiParser.parametersProcess import parametersProcess
from pureApiParser.preprocessApiData import preprocess_dewu_api
from pureApiParser.unitsAndImagesProcess import unitsAndImagesProcess

resultsExamples = [
    # Пример с пустыми данными: общий верхне уровневый формат.
    {
        "brands": [],  # Хотя бы 1 есть
        "is_collab": False,
        "collab_names": [],
        "lines": [],
        "categories": [],  # Хотя бы 1 есть
        "brandName": "",  # Есть всегда
        "model": "",  # Может не быть (редко)
        "colorway": "",  # Может не быть
        "gender": [],  # Тут лежат все гендеры для фильтров
        "baseGenders": [],
        # Тут лежат базовые гендеры (заданные через fitId и наш словарь). Это нужно для улучшения рекомендаций.
        "extraGenders": [],  # Тут лежат добавленные вручную нами гендеры
        "custom": False,
        "manufacturer_sku": "",
        "other_manufacturer_skus": [],  # Может быть пустым
        "date": "",  # Есть всегда (наверное)
        "approximate_date": "",  # Может не быть
        "retailPrice": {
            "currency": "CNY",
            "price": 0  # Может быть 0
        },
        "images": [],  # Может не быть
        "size_tables": {  # Во всех четырех таблицах будет одинаковый стандартный формат. Могут быть пустыми (как тут)
            "main_regular_table": {},
            "main_measurements_table": {},
            "default_table": {},
            "tables_recommendations": {}
        },
        "parameters_to_show_in_product": {  # Формат всегда такой: название: строка. Соблюдаем порядок
            "parameters": {},
            "parameters_order": [
                "Основные цвета",
                "Материалы",
                "Цена на ритейле"
            ]
        },
        "parameters_to_use_in_filters": {
            # Для фильтров используются только первые 2. Остальное используется для определения категорий. Однако можно впоследствии использовать для улучшения рекомендаций
            "colors": [],
            "material": [],
            "upper_height": [],
            "heel_type": [],
            "boots_height": [],
            "length": [],
            "sleeve_length": [],
            "collar_type": [],
            "closure_type": []
        },
        "units": [],  # Может быть пустым (в том случае, если какой-то странный товар)
        "hasConfigurationsWithDifferentImages": False,
        "minPrice": {
            "currency": "CNY",
            "price": 915.0
        },
        # Если есть конкретная цена или нет никаких цен, это поле 0. Если есть минимальная цена, но оферов построить не удалось, это поле не 0.
        "likesCount": 0,  # Может быть 0
        "spuId": 0  # Всегда есть
    }
]


def mainProcess(productInfo: dict, alreadyPreProcessed=False) -> (dict, dict):
    # Оставляем только нужные поля из всего ответа API, а также делаем микро преобразования с форматом данных (Формат входных данных есть в папке examples->preprocessedData).
    if not alreadyPreProcessed:
        preprocessedData = preprocess_dewu_api(productInfo)
    else:
        preprocessedData = productInfo

    # Создаем шаблон итогового словаря + заполняем базовые поля
    finalProcessedDewuApiData = {
        "brands": [],
        "is_collab": False,
        "collab_names": [],
        "lines": [],
        "categories": [],
        "brandName": "",
        "model": "",
        "colorway": "",
        "gender": [],
        "baseGenders": [],
        "extraGenders": [],
        "custom": False,
        "manufacturer_sku": preprocessedData["manufacturer_sku"],
        "other_manufacturer_skus": preprocessedData["manufacturer_skus"],
        "date": "",
        "approximate_date": "",
        "retailPrice": {
            "currency": "CNY" if preprocessedData["retailPrice"] else "",
            "price": preprocessedData["retailPrice"]
        },
        "images": [],
        "size_tables": {
            "main_regular_table": {},
            "main_measurements_table": {},
            "default_table": {},
            "tables_recommendations": {}
        },
        "parameters_to_show_in_product": {
            "parameters": {},
            "parameters_order": [
                "Основные цвета",
                "Материалы",
                "Цена на ритейле"
            ]
        },
        "parameters_to_use_in_filters": {
            "colors": [],
            "material": [],
            "upper_height": [],
            "heel_type": [],
            "boots_height": [],
            "length": [],
            "sleeve_length": [],
            "collar_type": [],
            "closure_type": []
        },
        "units": [],
        "minPrice": {
            "currency": "CNY",
            "price": 0
        },
        "likesCount": preprocessedData["likesCount"],
        "spuId": preprocessedData["spuId"]
    }

    # region Убираем китайские символы в артикуле. Если они есть, то в список всех артикулов вначале запишем этот артикул (с иероглифами), а в основной артикул перезапишем артикул без китайских символов. + Заменяем пустой артикул на "неизвестно"
    if remove_chinese_symbols(finalProcessedDewuApiData["manufacturer_sku"]) != finalProcessedDewuApiData[
        "manufacturer_sku"]:
        finalProcessedDewuApiData["other_manufacturer_skus"].append(finalProcessedDewuApiData["manufacturer_sku"])
        finalProcessedDewuApiData["manufacturer_sku"] = remove_chinese_symbols(
            finalProcessedDewuApiData["manufacturer_sku"])
    if not finalProcessedDewuApiData["manufacturer_sku"]:
        finalProcessedDewuApiData["manufacturer_sku"] = "неизвестно"
    # endregion

    # region Определяем, является ли товар кастомным
    if "定制" in preprocessedData["title"] or "team" in preprocessedData["manufacturer_sku"].lower() or any(
            "team" in sku.lower() for sku in preprocessedData["manufacturer_skus"]):
        finalProcessedDewuApiData["custom"] = True
    # endregion

    # Бренды добавляем + поле brandName
    finalProcessedDewuApiData = brandProcess(preprocessedData, finalProcessedDewuApiData)

    # Даты релиза (для фильтров + для страницы товара)
    finalProcessedDewuApiData = dateProcess(preprocessedData, finalProcessedDewuApiData)

    # Параметры (на основе title)
    finalProcessedDewuApiData = parametersProcess(preprocessedData, finalProcessedDewuApiData)

    # Полная обработка категорий на основе четырёх полей категорий + названия (Предварительно необходимо обработать параметры)
    finalProcessedDewuApiData = categoriesProcess(preprocessedData, finalProcessedDewuApiData)

    # Обработка гендера по fitId + несмотря на отсутствие размерных рядов пытаемся придумать, как добавить доп гендеры для некоторых категорий / брендов
    finalProcessedDewuApiData = gendersProcess(preprocessedData, finalProcessedDewuApiData)
    finalProcessedDewuApiData, nameWithoutCollaborations = collaborationsProcess(preprocessedData,
                                                                                 finalProcessedDewuApiData)
    finalProcessedDewuApiData, nameWithoutCollaborationsAndLines = linesProcess(preprocessedData,
                                                                                finalProcessedDewuApiData,
                                                                                nameWithoutCollaborations)

    finalProcessedDewuApiData = connectSizeTables(preprocessedData, finalProcessedDewuApiData)

    # Полноценная обработка юнитов
    finalProcessedDewuApiData, configsAmount = unitsAndImagesProcess(preprocessedData, finalProcessedDewuApiData)

    finalProcessedDewuApiData = nameProcess(preprocessedData, finalProcessedDewuApiData,
                                            nameWithoutCollaborationsAndLines, configsAmount)

    return finalProcessedDewuApiData


# Function remove_chinese_symbols
def remove_chinese_symbols(text):
    chinese_pattern = "[\u4e00-\u9FFF|\u3400-\u4DBF|\U00020000-\U0002A6DF|\U0002A700-\U0002B73F|\U0002B740-\U0002B81F|\U0002B820-\U0002CEAF|\uF900-\uFAFF|\U0002F800-\U0002FA1F]"
    without_chinese = re.sub(chinese_pattern, '', text)
    without_chinese = ' '.join(without_chinese.split())
    return without_chinese
