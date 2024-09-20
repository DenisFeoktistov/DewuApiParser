import copy
import json

from constants import CATEGORY_NAMES
from constants.process_constants import SIZE_TABLES_DEFAULT_FILTERS, CATEGORIES_WEIGHTS
import pydash as _


# Функция должна взять товар из нашей БД и изменить данные (исправить ошибки) + подправить формат.
# Идем по каждому товару из БД Sellout -> Берем spuId товара -> получаем apiPreprocessedData(вообще не тронутая дата из АПИ) + обработанную через функцию pureApiParser.main (получаем poizonApiProductInfo) -> запускаем эту функцию и на выходе получаем данные в таком же правильном формате для бекенда, но уже с исправленными данными + новыми полями. Перезаполняем инфу об этом товаре в БД.
def hkCorrect(hkProductInfo, poizonApiProductInfo, apiPreprocessedData):
    # Обновляем всю информацию, основанную на АПИ
    for key in ["brands", "is_collab", "collab_names", "lines", "categories", "brandName", "model", "colorway",
                "gender", "baseGenders", "extraGenders", "custom", "manufacturer_sku", "other_manufacturer_skus",
                "date", "approximate_date", "retailPrice"]:
        hkProductInfo[key] = poizonApiProductInfo[key]

    # Таблицы размеров
    if not any(bool(value) for value in hkProductInfo["size_tables"].values()):
        hkProductInfo["size_tables"] = poizonApiProductInfo["size_tables"]

    # region Получение верхне уровневой категории товара на английском языке: categoryEng
    categoryEng = ""
    for category in hkProductInfo["categories"]:
        if "Обувь" in CATEGORY_NAMES[category]["path"]:
            categoryEng = "shoes"
            break
        elif "Одежда" in CATEGORY_NAMES[category]["path"]:
            categoryEng = "clothes"
            break
        elif "Сумки" in CATEGORY_NAMES[category]["path"]:
            categoryEng = "bags"
            break
        elif "Аксессуары" in CATEGORY_NAMES[category]["path"]:
            categoryEng = "accessories"
            break
    # endregion

    gender = hkProductInfo["gender"][0]

    finalUnits = []

    if not poizonApiProductInfo["hasConfigurationsWithDifferentImages"]:
        if categoryEng in ["shoes", "clothes"]:
            # Поправляем дробные размеры для adidas
            if categoryEng == "shoes" and hkProductInfo["brands"][0] == "adidas":
                row = [
                    "35 1/3",
                    "35 2/3",
                    "36",
                    "36 2/3",
                    "37 1/3",
                    "38",
                    "38 2/3",
                    "39 1/3",
                    "40",
                    "40 2/3",
                    "41 1/3",
                    "42",
                    "42 2/3",
                    "43 1/3",
                    "44",
                    "44 2/3",
                    "45 1/3",
                    "46",
                    "46 2/3",
                    "47 1/3",
                    "48",
                    "48 2/3",
                    "49 1/3",
                    "50",
                    "50 2/3",
                    "51 1/3",
                    "52 2/3",
                    "53 1/3",
                    "54 2/3",
                    "55 2/3"
                ] if gender in ["M", "F"] else [
                    "16",
                    "17",
                    "18",
                    "19",
                    "20",
                    "21",
                    "22",
                    "23",
                    "23.5",
                    "24",
                    "25",
                    "25.5",
                    "26",
                    "26.5",
                    "27",
                    "28",
                    "28.5",
                    "29",
                    "30",
                    "30.5",
                    "31",
                    "31.5",
                    "32",
                    "33",
                    "33.5",
                    "34",
                    "35",
                    "35.5",
                    "36",
                    "36 2/3",
                    "37 1/3",
                    "38",
                    "38 2/3",
                    "39 1/3",
                    "40",
                    "40 2/3"
                ]
                for unitHk in hkProductInfo["units"]:
                    if not any(size in unitHk["view_name"] for size in row):
                        unitHk["view_name"] = unitHk["view_name"].replace(".5", " 2/3") if ".5" in unitHk[
                            "view_name"] else unitHk["view_name"].replace(" EU", " 1/3 EU")

            # Пытаемся связать юниты из ГК и из АПИ
            for unitApi in poizonApiProductInfo["units"]:
                for unitHk in hkProductInfo["units"]:
                    # Если есть АПИ название в ГК
                    if (" " + unitApi["view_name"] + " ") in (" " + unitHk["view_name"] + " "):
                        unitHk["unitId"] = len(finalUnits) + 1
                        unitHk["showImage"] = False
                        unitHk["imagesIds"] = [0]
                        unitHk["offers"].extend(unitApi["offers"])
                        unitHk["weight"] = CATEGORIES_WEIGHTS[hkProductInfo["categories"][0]]
                        finalUnits.append(copy.deepcopy(unitHk))
                        break
                else:
                    # Пробуем соединить по размеру из filter_size_table_info у юнита.
                    if categoryEng == "shoes":
                        apiRow = [
                            "34",
                            "34.5",
                            "35",
                            "35.5",
                            "36",
                            "36.5",
                            "37",
                            "37.5",
                            "38",
                            "38.5",
                            "39",
                            "39.5",
                            "40",
                            "40.5",
                            "41",
                            "41.5",
                            "42",
                            "42.5",
                            "43",
                            "43.5",
                            "44",
                            "44.5",
                            "45",
                            "45.5",
                            "46",
                            "46.5",
                            "47",
                            "47.5",
                            "48",
                            "48.5",
                            "49",
                            "49.5",
                            "50",
                            "50.5",
                            "51",
                            "51.5",
                            "52",
                            "52.5",
                            "53"
                        ] if gender in ["M", "F"] else [
                            "16",
                            "16.5",
                            "17",
                            "17.5",
                            "18",
                            "18.5",
                            "19",
                            "19.5",
                            "20",
                            "21",
                            "22",
                            "23",
                            "23.5",
                            "24",
                            "25",
                            "26",
                            "27",
                            "27.5",
                            "28",
                            "28.5",
                            "29",
                            "29.5",
                            "30",
                            "30.5",
                            "31",
                            "31.5",
                            "32",
                            "32.5",
                            "33",
                            "33.5",
                            "34",
                            "34.5",
                            "35",
                            "35.5",
                            "36",
                            "36.5",
                            "37",
                            "37.5",
                            "38",
                            "38.5",
                            "39",
                            "39.5",
                            "40",
                            "40.5",
                            "41",
                            "41.5",
                            "42",
                            "42.5",
                            "43",
                            "43.5",
                            "44",
                            "44.5"
                        ]
                    else:
                        apiRow = [
                            "XXXS",
                            "XXS",
                            "XS",
                            "S",
                            "M",
                            "L",
                            "XL",
                            "XXL",
                            "XXXL",
                            "4XL",
                            "5XL",
                            "6XL",
                            "7XL",
                            "8XL",
                            "9XL",
                            "10XL"
                        ] if gender in ["M"] else [
                            "XXXS",
                            "XXS",
                            "XS",
                            "S",
                            "M",
                            "L",
                            "XL",
                            "XXL",
                            "XXXL",
                            "4XL",
                            "5XL"
                        ] if gender in ["F"] else [
                            "46-52",
                            "58-64",
                            "64-70",
                            "70-76",
                            "76-88",
                            "88-94",
                            "94-100",
                            "100-106",
                            "106-112",
                            "112-118",
                            "118-124",
                            "124-130",
                            "130-136",
                            "136-142",
                            "142-148",
                            "148-154",
                            "154-160",
                            "160-166",
                            "166-172",
                            "172-178"
                        ]

                    size = unitApi["filter_size_table_info"]["sizes"][0] if unitApi["filter_size_table_info"][
                        "sizes"] else ""
                    indexSizeApi = apiRow.index(size) if size in apiRow else -1

                    for unitHk in hkProductInfo["units"]:
                        table = unitHk["filter_size_table_info"]["table_name"]
                        row = unitHk["filter_size_table_info"]["table_row_name"]
                        size = unitHk["filter_size_table_info"]["sizes"][0] if unitHk["filter_size_table_info"][
                            "sizes"] else ""
                        allSizeRows = _.get(SIZE_TABLES_DEFAULT_FILTERS, f"{table}.allSizes", [])
                        allSizes = []
                        for row_ in allSizeRows:
                            if row_["filter_name"] == row:
                                allSizes = row_["sizes"]
                        indexSizeHk = allSizes.index(size) if size in allSizes else -1
                        if indexSizeHk == indexSizeApi and indexSizeHk != -1:
                            unitHk["unitId"] = len(finalUnits) + 1
                            unitHk["showImage"] = False
                            unitHk["imagesIds"] = [0]
                            unitHk["offers"].extend(unitApi["offers"])
                            unitHk["weight"] = CATEGORIES_WEIGHTS[hkProductInfo["categories"][0]]
                            finalUnits.append(copy.deepcopy(unitHk))
                            break
                    else:
                        # Не смогли соединить, тогда добавляем пустой юнит из АПИ (то есть дополняем размерный ряд размерами без оферов)
                        unitApi["unitId"] = len(finalUnits) + 1
                        finalUnits.append(unitApi)

            # Теперь все юниты, которые есть в ГК, но не удалось их сопоставить с АПИ юнитами (какие-то странные названия)
            for i, unitHk in enumerate(hkProductInfo["units"]):
                if "unitId" not in unitHk:
                    # Вычисляем индекс, куда (после какого unitId) вставлять этот юнит в finalUnits
                    unitIdToInsertAfter = hkProductInfo["units"][i - 1]["unitId"] if i != 0 else 0
                    unitHk["unitId"] = unitIdToInsertAfter + 1
                    unitHk["showImage"] = False
                    unitHk["imagesIds"] = [0]
                    unitHk["weight"] = CATEGORIES_WEIGHTS[hkProductInfo["categories"][0]]
                    finalUnits.insert(unitIdToInsertAfter, copy.deepcopy(unitHk))
                    for u in finalUnits[unitIdToInsertAfter + 1:]:
                        u["unitId"] += 1
                    for u in hkProductInfo["units"][i + 1:]:
                        if "unitId" in u:
                            u["unitId"] += 1

            # Обновляем unitsIds у фото
            for image in poizonApiProductInfo["images"]:
                image["unitsIds"] = list(range(1, len(finalUnits) + 1))
            hkProductInfo["images"] = poizonApiProductInfo["images"]

        else:
            foundOS = False
            for unitHk in hkProductInfo["units"]:
                unitHk["unitId"] = len(finalUnits) + 1
                unitHk["showImage"] = False
                unitHk["imagesIds"] = [0]
                unitHk["weight"] = CATEGORIES_WEIGHTS[hkProductInfo["categories"][0]]
                if unitHk["view_name"] == "Один размер":
                    unitHk["filter_size_table_info"] = {
                        "table_name": "",
                        "table_row_name": "",
                        "sizes": []
                    }
                    unitHk["offers"].extend(poizonApiProductInfo["units"][0]["offers"])
                    finalUnits.append(copy.deepcopy(unitHk))
                    foundOS = True
                else:
                    finalUnits.append(copy.deepcopy(unitHk))
            if not foundOS:
                poizonApiProductInfo["units"][0]["unitId"] = len(finalUnits) + 1
                finalUnits.append(poizonApiProductInfo["units"][0])

        if not any(unit["offers"] for unit in finalUnits):
            hkProductInfo["minPrice"] = poizonApiProductInfo["minPrice"]

        hkProductInfo["hasConfigurationsWithDifferentImages"] = False

        # TODO: platformsInfo poizonWebParser
        # Пока что сделано так, что товары, у которых был hasConfigurationsWithDifferentImages = True, больше не будут обновляться. (то есть spuId в базе уже будет, а вот в привязанных платформах работающих не будет, таким образом, товар не обновится)
        hkProductInfo["platformsInfo"] = {
            "poizonNotFullApi": {
                "preprocessedData": {
                    "apiData": apiPreprocessedData,
                    "hkData": {}
                },
                "processedData": {
                    "apiData": poizonApiProductInfo,
                    "hkData": {}
                }
            },
            "poizonHK": {
                "preprocessedData": {
                    "apiData": {},
                    "hkData": {}
                },
                "processedData": {
                    "apiData": {},
                    "hkData": {}
                }
            }
        }

    else:
        # TODO: Здесь еще раз посмотреть на формат текущих данных
        # Если с ГК у товара нет никаких оферов, то заменяем на формат из АПИ
        if not any(unit["offers"] for unit in hkProductInfo["units"]):
            hkProductInfo["images"] = poizonApiProductInfo["images"]
            hkProductInfo["units"] = poizonApiProductInfo["units"]
            hkProductInfo["minPrice"] = poizonApiProductInfo["minPrice"]
            hkProductInfo["hasConfigurationsWithDifferentImages"] = poizonApiProductInfo[
                "hasConfigurationsWithDifferentImages"]
            return hkProductInfo
        if categoryEng == "clothes":
            # Вначале переписываем все те же юниты из ГК, а затем дополняем полную размерную сетку одежды
            for unitHk in hkProductInfo["units"]:
                unitHk["unitId"] = len(finalUnits) + 1
                unitHk["showImage"] = False
                unitHk["imagesIds"] = [0]
                unitHk["weight"] = CATEGORIES_WEIGHTS[hkProductInfo["categories"][0]]
                finalUnits.append(copy.deepcopy(unitHk))
            if gender in ["M", "F"]:
                for size in [
                    "XXS",
                    "XS",
                    "S",
                    "M",
                    "L",
                    "XL",
                    "XXL"
                ]:
                    # Если такого размера еще нет
                    if not any((" " + size + " ") in (" " + unit["view_name"] + " ") for unit in
                               hkProductInfo["units"]):
                        finalUnits.append({
                            "view_name": size,
                            "unitId": len(finalUnits) + 1,
                            "imagesIds": [0],
                            "showImage": False,
                            "filter_size_table_info": {
                                "table_name": "Clothes_Men" if gender == "M" else "Clothes_Women",
                                "table_row_name": "Международный(INT)",
                                "sizes": [size]
                            },
                            "offers": [],
                            "weight": CATEGORIES_WEIGHTS[hkProductInfo["categories"][0]],
                            "height": 0,
                            "width": 0,
                            "length": 0
                        })

            # Обновляем unitsIds у фото
            for image in poizonApiProductInfo["images"]:
                image["unitsIds"] = list(range(1, len(finalUnits) + 1))
            hkProductInfo["images"] = poizonApiProductInfo["images"]

            hkProductInfo["minPrice"] = {
                "currency": "",
                "price": 0
            }
            hkProductInfo["hasConfigurationsWithDifferentImages"] = False

        else:
            for unitHk in hkProductInfo["units"]:
                unitHk["unitId"] = len(finalUnits) + 1
                unitHk["showImage"] = False
                unitHk["imagesIds"] = [0]
                unitHk["weight"] = CATEGORIES_WEIGHTS[hkProductInfo["categories"][0]]
                finalUnits.append(copy.deepcopy(unitHk))
            # Обновляем unitsIds у фото
            for image in poizonApiProductInfo["images"]:
                image["unitsIds"] = list(range(1, len(finalUnits) + 1))
            hkProductInfo["images"] = poizonApiProductInfo["images"]

            hkProductInfo["minPrice"] = {
                "currency": "",
                "price": 0
            }
            hkProductInfo["hasConfigurationsWithDifferentImages"] = False

        # TODO: platformsInfo poizonWebParser
        # Пока что сделано так, что товары, у которых был hasConfigurationsWithDifferentImages = True, больше не будут обновляться. (то есть spuId в базе уже будет, а вот в привязанных платформах работающих не будет, таким образом, товар не обновится)
        hkProductInfo["platformsInfo"] = {
            "poizonHK": {
                "preprocessedData": {
                    "apiData": {},
                    "hkData": {}
                },
                "processedData": {
                    "apiData": {},
                    "hkData": {}
                }
            }
        }

    hkProductInfo["units"] = finalUnits

    return hkProductInfo


def test():
    poizonApiProductInfo = {
        "brands": [
            "Nike",
            "AMBUSH"
        ],
        "is_collab": True,
        "collab_names": [
            "Nike x Ambush"
        ],
        "lines": [
            [
                "Nike",
                "Nike Dunk",
                "Nike Dunk High"
            ]
        ],
        "categories": [
            "Футболки",
            "Все кроссовки"
        ],
        "brandName": "Nike x Ambush",
        "model": "Dunk High",
        "colorway": "Deep royal",
        "gender": [
            "M",
            "F"
        ],
        "baseGenders": [
            "M",
            "F"
        ],
        "extraGenders": [],
        "custom": False,
        "manufacturer_sku": "CU7544-400",
        "other_manufacturer_skus": [],
        "date": "18.05.2021",
        "approximate_date": "18.05.2021",
        "retailPrice": {
            "currency": "CNY",
            "price": 1299
        },
        "images": [
            {
                "imageId": 0,
                "unitsIds": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    16,
                    17,
                    18,
                    19,
                    20,
                    21,
                    22,
                    23,
                    24,
                    25,
                    26,
                    27,
                    28,
                    29,
                    30,
                    31,
                    32,
                    33,
                    34,
                    35,
                    36,
                    37,
                    38
                ],
                "url": "https://cdn.poizon.com/pro-img/origin-img/20230721/dc21d6128aab4f1e93bc883a3725a313.jpg"
            },
            {
                "imageId": 0,
                "unitsIds": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    16,
                    17,
                    18,
                    19,
                    20,
                    21,
                    22,
                    23,
                    24,
                    25,
                    26,
                    27,
                    28,
                    29,
                    30,
                    31,
                    32,
                    33,
                    34,
                    35,
                    36,
                    37,
                    38
                ],
                "url": "https://cdn.poizon.com/pro-img/origin-img/20230721/d0eff04089d24d33a3cd790cddaba2c2.jpg"
            },
            {
                "imageId": 0,
                "unitsIds": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    16,
                    17,
                    18,
                    19,
                    20,
                    21,
                    22,
                    23,
                    24,
                    25,
                    26,
                    27,
                    28,
                    29,
                    30,
                    31,
                    32,
                    33,
                    34,
                    35,
                    36,
                    37,
                    38
                ],
                "url": "https://cdn.poizon.com/pro-img/origin-img/20230721/02c9f790694f410bb7514e9aa7172aac.jpg"
            },
            {
                "imageId": 0,
                "unitsIds": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    16,
                    17,
                    18,
                    19,
                    20,
                    21,
                    22,
                    23,
                    24,
                    25,
                    26,
                    27,
                    28,
                    29,
                    30,
                    31,
                    32,
                    33,
                    34,
                    35,
                    36,
                    37,
                    38
                ],
                "url": "https://cdn.poizon.com/pro-img/origin-img/20230721/00e9ea928a8e43e0bea3ab147d435be2.jpg"
            },
            {
                "imageId": 0,
                "unitsIds": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    16,
                    17,
                    18,
                    19,
                    20,
                    21,
                    22,
                    23,
                    24,
                    25,
                    26,
                    27,
                    28,
                    29,
                    30,
                    31,
                    32,
                    33,
                    34,
                    35,
                    36,
                    37,
                    38
                ],
                "url": "https://cdn.poizon.com/pro-img/origin-img/20230721/3322602a30f44cc1b1dad7c853271882.jpg"
            },
            {
                "imageId": 0,
                "unitsIds": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    16,
                    17,
                    18,
                    19,
                    20,
                    21,
                    22,
                    23,
                    24,
                    25,
                    26,
                    27,
                    28,
                    29,
                    30,
                    31,
                    32,
                    33,
                    34,
                    35,
                    36,
                    37,
                    38
                ],
                "url": "https://cdn.poizon.com/pro-img/origin-img/20230721/b76a3de9185a46598db29f68ff27ce11.jpg"
            },
            {
                "imageId": 0,
                "unitsIds": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    16,
                    17,
                    18,
                    19,
                    20,
                    21,
                    22,
                    23,
                    24,
                    25,
                    26,
                    27,
                    28,
                    29,
                    30,
                    31,
                    32,
                    33,
                    34,
                    35,
                    36,
                    37,
                    38
                ],
                "url": "https://cdn.poizon.com/pro-img/origin-img/20230721/c6925611501240de9f0c0316c13ca1d3.jpg"
            },
            {
                "imageId": 0,
                "unitsIds": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    16,
                    17,
                    18,
                    19,
                    20,
                    21,
                    22,
                    23,
                    24,
                    25,
                    26,
                    27,
                    28,
                    29,
                    30,
                    31,
                    32,
                    33,
                    34,
                    35,
                    36,
                    37,
                    38
                ],
                "url": "https://cdn.poizon.com/pro-img/origin-img/20230721/769c63715baf46bbb156e6fdf68751ad.jpg"
            }
        ],
        "size_tables": {
            "main_regular_table": {
                "rows_order": [
                    "EU",
                    "RU",
                    "US",
                    "UK",
                    "CM/JP",
                    "US-Kids",
                    "US-Women's"
                ],
                "values": {
                    "EU": [
                        "35.5",
                        "36",
                        "36.5",
                        "37.5",
                        "38",
                        "38.5",
                        "39",
                        "40",
                        "40.5",
                        "41",
                        "42",
                        "42.5",
                        "43",
                        "44",
                        "44.5",
                        "45",
                        "45.5",
                        "46",
                        "47",
                        "47.5",
                        "48",
                        "48.5",
                        "49",
                        "49.5",
                        "50",
                        "50.5",
                        "51",
                        "51.5",
                        "52",
                        "52.5",
                        "53",
                        "53.5",
                        "54",
                        "54.5",
                        "55",
                        "55.5",
                        "56",
                        "56.5"
                    ],
                    "RU": [
                        "34.5",
                        "35",
                        "35.5",
                        "36.5",
                        "37",
                        "37.5",
                        "38",
                        "39",
                        "39.5",
                        "40",
                        "41",
                        "41.5",
                        "42",
                        "43",
                        "43.5",
                        "44",
                        "44.5",
                        "45",
                        "46",
                        "46.5",
                        "47",
                        "47.5",
                        "48",
                        "48.5",
                        "49",
                        "49.5",
                        "50",
                        "50.5",
                        "51",
                        "51.5",
                        "52",
                        "52.5",
                        "53",
                        "53.5",
                        "54",
                        "54.5",
                        "55",
                        "55.5"
                    ],
                    "US": [
                        "3.5",
                        "4",
                        "4.5",
                        "5",
                        "5.5",
                        "6",
                        "6.5",
                        "7",
                        "7.5",
                        "8",
                        "8.5",
                        "9",
                        "9.5",
                        "10",
                        "10.5",
                        "11",
                        "11.5",
                        "12",
                        "12.5",
                        "13",
                        "13.5",
                        "14",
                        "14.5",
                        "15",
                        "15.5",
                        "16",
                        "16.5",
                        "17",
                        "17.5",
                        "18",
                        "18.5",
                        "19",
                        "19.5",
                        "20",
                        "20.5",
                        "21",
                        "21.5",
                        "22"
                    ],
                    "UK": [
                        "3",
                        "3.5",
                        "4",
                        "4.5",
                        "5",
                        "5.5",
                        "6",
                        "6",
                        "6.5",
                        "7",
                        "7.5",
                        "8",
                        "8.5",
                        "9",
                        "9.5",
                        "10",
                        "10.5",
                        "11",
                        "11.5",
                        "12",
                        "12.5",
                        "13",
                        "13.5",
                        "14",
                        "14.5",
                        "15",
                        "15.5",
                        "16",
                        "16.5",
                        "17",
                        "17.5",
                        "18",
                        "18.5",
                        "19",
                        "19.5",
                        "20",
                        "20.5",
                        "21"
                    ],
                    "CM/JP": [
                        "22.5",
                        "23",
                        "23.5",
                        "23.5",
                        "24",
                        "24",
                        "24.5",
                        "25",
                        "25.5",
                        "26",
                        "26.5",
                        "27",
                        "27.5",
                        "28",
                        "28.5",
                        "29",
                        "29.5",
                        "30",
                        "30.5",
                        "31",
                        "31.5",
                        "32",
                        "32.5",
                        "33",
                        "33.5",
                        "34",
                        "34.5",
                        "35",
                        "35.5",
                        "36",
                        "36.5",
                        "37",
                        "37.5",
                        "38",
                        "38.5",
                        "39",
                        "39.5",
                        "40"
                    ],
                    "US-Kids": [
                        "3.5Y",
                        "4Y",
                        "4.5Y",
                        "5Y",
                        "5.5Y",
                        "6Y",
                        "6.5Y",
                        "7Y",
                        "7.5Y",
                        "8Y",
                        "8.5Y",
                        "9Y",
                        "9.5Y",
                        "10Y",
                        "10.5Y",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        ""
                    ],
                    "US-Women's": [
                        "5",
                        "5.5",
                        "6",
                        "6.5",
                        "7",
                        "7.5",
                        "8",
                        "8.5",
                        "9",
                        "9.5",
                        "10",
                        "10.5",
                        "11",
                        "11.5",
                        "12",
                        "12.5",
                        "13",
                        "13.5",
                        "14",
                        "14.5",
                        "15",
                        "15.5",
                        "16",
                        "16.5",
                        "17",
                        "17.5",
                        "18",
                        "18.5",
                        "19",
                        "19.5",
                        "20",
                        "20.5",
                        "21",
                        "21.5",
                        "22",
                        "22.5",
                        "23",
                        "23.5"
                    ]
                },
                "table_name": "Таблица Nike",
                "table_title": "Мужская обувь Nike",
                "table_description": "Обратите внимание, таблица представлена брендом Nike, для других брендов рекомендуем пользоваться своей размерной сеткой и быть бдительным при сравнении размеров разных брендов. Вы всегда можете обратиться в службу поддержки, и мы обязательно поможем подобрать вам подходящий размер!"
            },
            "main_measurements_table": {},
            "default_table": {},
            "tables_recommendations": {}
        },
        "parameters_to_show_in_product": {
            "parameters": {
                "Основные цвета": "Royal Blue, Синий",
                "Цена на ритейле": "16900₽"
            },
            "parameters_order": [
                "Основные цвета",
                "Материалы",
                "Цена на ритейле"
            ]
        },
        "parameters_to_use_in_filters": {
            "colors": [
                "blue"
            ],
            "material": [],
            "upper_height": [
                "high"
            ],
            "heel_type": [],
            "boots_height": [],
            "length": [],
            "sleeve_length": [],
            "collar_type": [],
            "closure_type": []
        },
        "units": [
            {
                "view_name": "XS",
                "unitId": 1,
                "imagesIds": [
                    0
                ],
                "showImage": False,
                "filter_size_table_info": {
                    "table_name": "",
                    "table_row_name": "",
                    "sizes": []
                },
                "offers": [],
                "weight": 1.8,
                "height": 0,
                "width": 0,
                "length": 0
            }
        ],
        "minPrice": {
            "currency": "CNY",
            "price": 915.0
        },
        "likesCount": 242645,
        "spuId": 1498978,
        "hasConfigurationsWithDifferentImages": True
    }
    hkProductInfo = {
        "size_tables": {

        },
        "units": [
            {
                "view_name": "XXS",
                "filter_size_table_info": {
                    "table_name": "Shoes_Adults",
                    "table_row_name": "Европейский(EU)",
                    "sizes": [
                        "37.5"
                    ]
                },
                "offers": [],
                "weight": 1.8,
                "height": 0,
                "width": 0,
                "length": 0
            },
            {
                "view_name": "S",
                "filter_size_table_info": {
                    "table_name": "Shoes_Adults",
                    "table_row_name": "Европейский(EU)",
                    "sizes": [
                        "37.5"
                    ]
                },
                "offers": [
                    {
                        "price": 1099999.0,
                        "currency": "CNY",
                        "days_min_to_international_warehouse": 0,
                        "days_max_to_international_warehouse": 0,
                        "delivery_type": "standard",
                        "platform_info": {
                            "poizonHK": {
                                "source": "notFullAPI",
                                "sku": 610913234,
                                "poizon_abroad": False
                            }
                        }
                    }
                ],
                "weight": 1.8,
                "height": 0,
                "width": 0,
                "length": 0
            }
        ]
    }
    return hkCorrect(hkProductInfo, poizonApiProductInfo, {})


print(json.dumps(test(), ensure_ascii=False))
