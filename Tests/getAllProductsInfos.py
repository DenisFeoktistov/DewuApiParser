import re
import pydash as _
import asyncio
import json

from aiohttp import ClientSession

from Tests.constants.processConstants import PROCESSED_SPUS, INVALID_DATES, GENDERS, ALL_CATEGORIES, STRANGE_DATA, \
    CONFIGS, ARTICLES
from constants.process_constants import CATEGORY_FULL_PROCESS, CATEGORY_NAMES, TITLING
from functions.fetch_functions.api_and_filter import api_and_filter
from functions.fetch_functions.get_from_api_async import get_from_api_async
from pureApiParser.preprocessApiData import preprocess_dewu_api


def updateAllUniqueProductsValues(unprocessedProductInfo: dict):
    if not unprocessedProductInfo:
        return

    preprocessedProductInfo = preprocess_dewu_api(unprocessedProductInfo)

    if preprocessedProductInfo["spuId"] in PROCESSED_SPUS:
        print(f'{preprocessedProductInfo["spuId"]} already processed!')
        return

    # region releaseDate
    valid_formats = [
        r"^\d{4}\.\d{2}\.\d{2}$",  # YYYY.MM.DD
        r"^\d{4}\.\d{2}$",  # YYYY.MM
        r"^\d{4}$",  # YYYY
        r"^\d{4}(春夏|秋冬|秋季|冬季|春季|夏季)$"  # YYYY + season
    ]
    validDate = False
    for fmt in valid_formats:
        if re.match(fmt, preprocessedProductInfo["releaseDate"]):
            validDate = True

    if not validDate:
        if preprocessedProductInfo["releaseDate"] not in INVALID_DATES:
            INVALID_DATES[preprocessedProductInfo["releaseDate"]] = [1, preprocessedProductInfo["spuId"]]
        else:
            INVALID_DATES[preprocessedProductInfo["releaseDate"]][0] += 1
            if INVALID_DATES[preprocessedProductInfo["releaseDate"]][0] < 6:
                INVALID_DATES[preprocessedProductInfo["releaseDate"]].append(preprocessedProductInfo["spuId"])
    # endregion

    # region genders
    fitId = preprocessedProductInfo["fitId"]
    categoriesDewu = [preprocessedProductInfo["categoryId"], preprocessedProductInfo["level1CategoryId"],
                      preprocessedProductInfo["level2CategoryId"]]
    categories = []
    for category in categoriesDewu:
        categories.extend(_.get(CATEGORY_FULL_PROCESS, f"{category}.categories_to_add_directly", []))

    categoryEng = "otherAccessories"
    for category in categories:
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

    if str(fitId) in GENDERS:
        if len(GENDERS[str(fitId)][categoryEng]) < 20:
            GENDERS[str(fitId)][categoryEng].append(preprocessedProductInfo["spuId"])
    else:
        if str(fitId) not in GENDERS["other"]:
            GENDERS["other"][str(fitId)] = {
                "shoes": [],
                "clothes": [],
                "bags": [],
                "accessories": []
            }
        if len(GENDERS["other"][str(fitId)][categoryEng]) < 20:
            GENDERS["other"][str(fitId)][categoryEng].append(preprocessedProductInfo["spuId"])
    # endregion

    # region Категории
    categoryId = preprocessedProductInfo["categoryId"]
    categoryName = preprocessedProductInfo["categoryName"]
    level1CategoryId = preprocessedProductInfo["level1CategoryId"]
    level2CategoryId = preprocessedProductInfo["level2CategoryId"]

    if str(categoryId) not in CATEGORY_FULL_PROCESS:
        if categoryId not in ALL_CATEGORIES["categoryIds"]:
            ALL_CATEGORIES["categoryIds"][categoryId] = {
                "count": 0,
                "examples": []
            }
        ALL_CATEGORIES["categoryIds"][categoryId]["count"] += 1
        if len(ALL_CATEGORIES["categoryIds"][categoryId]["examples"]) < 20:
            ALL_CATEGORIES["categoryIds"][categoryId]["examples"].append(preprocessedProductInfo["spuId"])

    for key, val in [["categoryNames", str(categoryName)], ["level1CategoryIds", str(level1CategoryId)],
                     ["level2CategoryIds", str(level2CategoryId)]]:
        if val not in ALL_CATEGORIES[key]:
            ALL_CATEGORIES[key][val] = {
                "count": 0,
                "examples": []
            }
        ALL_CATEGORIES[key][val]["count"] += 1
        if len(ALL_CATEGORIES[key][val]["examples"]) < 20:
            ALL_CATEGORIES[key][val]["examples"].append(preprocessedProductInfo["spuId"])

    # endregion

    # region Артикулы
    # Проверяем наличие китайских символов
    if re.search(r'[\u4e00-\u9fff]', preprocessedProductInfo["manufacturer_sku"]):
        key = "chineseSymbols"
        if key not in ARTICLES:
            ARTICLES[key] = {"count": 0, "products": [], "examples": []}

        ARTICLES[key]["count"] += 1
        if len(ARTICLES[key]["products"]) < 100:
            ARTICLES[key]["products"].append(preprocessedProductInfo["spuId"])
            ARTICLES[key]["examples"].append(preprocessedProductInfo["manufacturer_sku"])

    # Поиск специальных символов (не англ. буквы)
    for char in re.findall(r'[^a-zA-Z0-9\u4e00-\u9fff]', preprocessedProductInfo["manufacturer_sku"]):
        if char not in ARTICLES:
            ARTICLES[char] = {"count": 0, "products": [], "examples": []}

        ARTICLES[char]["count"] += 1
        if len(ARTICLES[char]["products"]) < 100:
            ARTICLES[char]["products"].append(preprocessedProductInfo["spuId"])
            ARTICLES[char]["products"].append(preprocessedProductInfo["manufacturer_sku"])
    # endregion

    # region Специальные символы в названии (не англ. буквы).
    for char in re.findall(r'[^a-zA-Z0-9\u4e00-\u9fff]', preprocessedProductInfo["title"]):
        if char not in ARTICLES["titling"]:
            ARTICLES["titling"][char] = {"count": 0, "products": [], "examples": []}

        ARTICLES["titling"][char]["count"] += 1
        if len(ARTICLES["titling"][char]["products"]) < 100:
            ARTICLES["titling"][char]["products"].append(preprocessedProductInfo["spuId"])
            ARTICLES["titling"][char]["products"].append(preprocessedProductInfo["title"])
    # endregion

    # region Конфигурации
    images_full = preprocessedProductInfo["images_full"]
    arSkuIdRelation = preprocessedProductInfo["arSkuIdRelation"]
    skus = preprocessedProductInfo["skus"]
    # region Получение верхне уровневой категории товара
    categoriesDewu = [preprocessedProductInfo["categoryId"], preprocessedProductInfo["level1CategoryId"],
                      preprocessedProductInfo["level2CategoryId"]]
    categories = []
    for category in categoriesDewu:
        categories.extend(_.get(CATEGORY_FULL_PROCESS, f"{category}.categories_to_add_directly", []))

    categoryEng = "otherAccessories"
    for category in categories:
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

    #
    # region Начнем со сбора полей и нахождения странных данных
    #

    # region Обработка поля images_full
    if not images_full:
        STRANGE_DATA["images"]["noImages"]["count"] += 1
        if len(STRANGE_DATA["images"]["noImages"]["products"]) < 20:
            STRANGE_DATA["images"]["noImages"]["products"].append(preprocessedProductInfo["spuId"])

    allUniquePropertiesFromImages = []
    for image in images_full:
        if "propertyValueId" not in image:
            STRANGE_DATA["images"]["noPropertyValueId"]["count"] += 1
            if len(STRANGE_DATA["images"]["noPropertyValueId"]["products"]) < 20:
                STRANGE_DATA["images"]["noPropertyValueId"]["products"].append(
                    preprocessedProductInfo["spuId"])
            continue
        if "url" not in image:
            STRANGE_DATA["images"]["noUrl"]["count"] += 1
            if len(STRANGE_DATA["images"]["noUrl"]["products"]) < 20:
                STRANGE_DATA["images"]["noUrl"]["products"].append(preprocessedProductInfo["spuId"])

        if image["propertyValueId"] not in allUniquePropertiesFromImages:
            allUniquePropertiesFromImages.append(image["propertyValueId"])

    if len(allUniquePropertiesFromImages) == 2 and 0 in allUniquePropertiesFromImages:
        STRANGE_DATA["images"]["2PrIdsAnd0InPrIds"]["count"] += 1
        if len(STRANGE_DATA["images"]["2PrIdsAnd0InPrIds"]["products"]) < 20:
            STRANGE_DATA["images"]["2PrIdsAnd0InPrIds"]["products"].append(preprocessedProductInfo["spuId"])

    if len(allUniquePropertiesFromImages) > 2 and 0 in allUniquePropertiesFromImages:
        STRANGE_DATA["images"]["moreTh2PrIdsAndStill0InPrIds"]["count"] += 1
        if len(STRANGE_DATA["images"]["moreTh2PrIdsAndStill0InPrIds"]["products"]) < 20:
            STRANGE_DATA["images"]["moreTh2PrIdsAndStill0InPrIds"]["products"].append(
                preprocessedProductInfo["spuId"])

    oneConfig = False
    # Считаем, что все фото относятся к одной конфигурации
    if len(allUniquePropertiesFromImages) <= 1 or (
            len(allUniquePropertiesFromImages) == 2 and 0 in allUniquePropertiesFromImages):
        oneConfig = True
    # endregion

    # region Обработка поля skus
    if not skus:
        if not images_full:
            STRANGE_DATA["skus"]["noSkus"]["noImages"]["count"] += 1
            if len(STRANGE_DATA["skus"]["noSkus"]["noImages"]["products"]) < 20:
                STRANGE_DATA["skus"]["noSkus"]["noImages"]["products"].append(preprocessedProductInfo["spuId"])
        else:
            STRANGE_DATA["skus"]["noSkus"]["withImages"]["count"] += 1
            if len(STRANGE_DATA["skus"]["noSkus"]["withImages"]["products"]) < 20:
                STRANGE_DATA["skus"]["noSkus"]["withImages"]["products"].append(
                    preprocessedProductInfo["spuId"])

    allSkus = []
    allSkusOtherProducts = []
    for sku in skus:
        if sku["skuId"] not in allSkus and sku["spuId"] == preprocessedProductInfo["spuId"]:
            allSkus.append(sku["skuId"])
        elif sku["skuId"] not in allSkusOtherProducts and sku["spuId"] != preprocessedProductInfo["spuId"]:
            allSkusOtherProducts.append(sku["skuId"])
            STRANGE_DATA["skus"]["otherSpuId"]["count"] += 1
            if len(STRANGE_DATA["skus"]["otherSpuId"]["products"]) < 20:
                STRANGE_DATA["skus"]["otherSpuId"]["products"].append(preprocessedProductInfo["spuId"])

        # Хотим понять, если у нас есть разные фото (propertyId), всегда ли в каждом sku.properties есть такой property, в котором propertyId равен одному из известных из фото.
        if not oneConfig and not any(
                property_["propertyValueId"] in allUniquePropertiesFromImages for property_ in sku["properties"]):
            STRANGE_DATA["skus"]["noCorrectPropIdInSku"]["count"] += 1
            if len(STRANGE_DATA["skus"]["noCorrectPropIdInSku"]["products"]) < 20:
                STRANGE_DATA["skus"]["noCorrectPropIdInSku"]["products"].append(preprocessedProductInfo["spuId"])
    # endregion

    # region Обработка поля arSkuIdRelation
    if not arSkuIdRelation:
        if len(allSkus) == 1:
            STRANGE_DATA["arSkuIdRelation"]["noArSkuIdRelation"]["oneSku"]["count"] += 1
            if len(STRANGE_DATA["arSkuIdRelation"]["noArSkuIdRelation"]["oneSku"]["products"]) < 20:
                STRANGE_DATA["arSkuIdRelation"]["noArSkuIdRelation"]["oneSku"]["products"].append(
                    preprocessedProductInfo["spuId"])
        elif len(allSkus) > 1 and oneConfig:
            STRANGE_DATA["arSkuIdRelation"]["noArSkuIdRelation"]["severalSkuAndOnePrId"]["count"] += 1
            if len(STRANGE_DATA["arSkuIdRelation"]["noArSkuIdRelation"]["severalSkuAndOnePrId"]["products"]) < 20:
                STRANGE_DATA["arSkuIdRelation"]["noArSkuIdRelation"]["severalSkuAndOnePrId"]["products"].append(
                    preprocessedProductInfo["spuId"])
        else:
            STRANGE_DATA["arSkuIdRelation"]["noArSkuIdRelation"]["severalSkuAndSeveralPrId"]["count"] += 1
            if len(STRANGE_DATA["arSkuIdRelation"]["noArSkuIdRelation"]["severalSkuAndSeveralPrId"]["products"]) < 20:
                STRANGE_DATA["arSkuIdRelation"]["noArSkuIdRelation"]["severalSkuAndSeveralPrId"]["products"].append(
                    preprocessedProductInfo["spuId"])

    else:
        for arSku in arSkuIdRelation:
            if "propertyValueId" not in arSku:
                STRANGE_DATA["arSkuIdRelation"]["noPrId"]["count"] += 1
                if len(STRANGE_DATA["arSkuIdRelation"]["noPrId"]["products"]) < 20 and preprocessedProductInfo[
                    "spuId"] not in STRANGE_DATA["arSkuIdRelation"]["noPrId"]["products"]:
                    STRANGE_DATA["arSkuIdRelation"]["noPrId"]["products"].append(
                        preprocessedProductInfo["spuId"])
            elif not oneConfig and arSku["propertyValueId"] not in allUniquePropertiesFromImages:
                STRANGE_DATA["arSkuIdRelation"]["noCorrectPrId"]["count"] += 1
                if len(STRANGE_DATA["arSkuIdRelation"]["noCorrectPrId"]["products"]) < 20 and preprocessedProductInfo[
                    "spuId"] not in STRANGE_DATA["arSkuIdRelation"]["noCorrectPrId"]["products"]:
                    STRANGE_DATA["arSkuIdRelation"]["noCorrectPrId"]["products"].append(
                        preprocessedProductInfo["spuId"])
    # endregion

    #
    # endregion

    #
    #  region Заполняем информации о товарах с разными конфигурациями (хотим проанализировать кол-во, бренды), чтобы попробовать с большей вероятностью предсказывать, где разные цвета -> нельзя выдавать всему одну цену, а где комплектации и можно выдавать одну цену и продавать по ней.
    #

    # Для обуви и одежды с разными конфигурациями с фото
    if categoryEng in ["shoes", "clothes"] and not oneConfig:
        CONFIGS[categoryEng]["manyPrIds"]["count"] += 1
        if len(CONFIGS[categoryEng]["manyPrIds"]["products"]) < 100:
            CONFIGS[categoryEng]["manyPrIds"]["products"].append(preprocessedProductInfo["spuId"])

    if categoryEng in ["bags", "accessories", "otherAccessories"]:
        # Одна конфигурация
        if oneConfig and len(allSkus) == 1:
            CONFIGS[categoryEng]["oneSku"] += 1
        # Несколько конфигураций, но единые фотки (предположительно, комплектации)
        elif oneConfig and len(allSkus) > 1:
            mainBrand = ""
            for brand in preprocessedProductInfo["allBrands"]:
                if str(brand) in TITLING:
                    mainBrand = str(brand)
                    break
            if TITLING[mainBrand]["brand_names"][0] not in CONFIGS[categoryEng]["manySkus"]:
                CONFIGS[categoryEng]["manySkus"][TITLING[mainBrand]["brand_names"][0]] = {
                    "count": 0,
                    "products": []
                }
            CONFIGS[categoryEng]["manySkus"][TITLING[mainBrand]["brand_names"][0]]["count"] += 1
            if len(CONFIGS[categoryEng]["manySkus"][TITLING[mainBrand]["brand_names"][0]]["products"]) < 100:
                CONFIGS[categoryEng]["manySkus"][TITLING[mainBrand]["brand_names"][0]]["products"].append(
                    preprocessedProductInfo["spuId"])
        # Несколько конфигурация с разными фотографиями (цвета или комплектации)
        elif not oneConfig and len(allSkus) > 1:
            mainBrand = 0
            for brand in preprocessedProductInfo["allBrands"]:
                if str(brand) in TITLING:
                    mainBrand = str(brand)
                    break
            if TITLING[mainBrand]["brand_names"][0] not in CONFIGS[categoryEng]["manyPrIds"]:
                CONFIGS[categoryEng]["manyPrIds"][TITLING[mainBrand]["brand_names"][0]] = {
                    "count": 0,
                    "products": []
                }
            CONFIGS[categoryEng]["manyPrIds"][TITLING[mainBrand]["brand_names"][0]]["count"] += 1
            if len(CONFIGS[categoryEng]["manyPrIds"][TITLING[mainBrand]["brand_names"][0]]["products"]) < 100:
                CONFIGS[categoryEng]["manyPrIds"][TITLING[mainBrand]["brand_names"][0]]["products"].append(
                    preprocessedProductInfo["spuId"])
    #
    # endregion
    # endregion

    PROCESSED_SPUS.append(preprocessedProductInfo["spuId"])

    print(f"Successfully processed product: {preprocessedProductInfo['spuId']}")
    print("--------------------------------")
    print()


def proceedAllData(allData: list) -> None:
    for preprocessedProductInfo in allData:
        updateAllUniqueProductsValues(preprocessedProductInfo)

    # region Запись в файлы
    for result, fileName in [[PROCESSED_SPUS, "constants/processedSpus.json"],
                             [INVALID_DATES, "constants/invalidDates.json"],
                             [GENDERS, "constants/genders.json"],
                             [ALL_CATEGORIES, "constants/allCategories.json"],
                             [ARTICLES, "constants/articles.json"],
                             [STRANGE_DATA, "constants/strangeData.json"],
                             [CONFIGS, "constants/configs.json"]]:
        with open(fileName, "w", encoding="utf-8") as result_file:
            result_file.write(json.dumps(result, indent=4, ensure_ascii=False))
    # endregion

    print()
    print(f"Successfully processed {len(allData)} products")
    print("|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|")


async def main(start, end, batch_size=10_000):
    async with ClientSession() as session:
        for i in range(start, end, batch_size):
            tasks = [asyncio.create_task(api_and_filter(spu, session=session)) for spu in range(i, i + batch_size)]
            results = await asyncio.gather(*tasks)

            good_spus = [result[0] for result in results if result[1]]
            tasks = [asyncio.create_task(get_from_api_async(spu, session)) for spu in good_spus]
            data_results = await asyncio.gather(*tasks)

            print(f"Received info about {len(data_results)} products in {i}-{i + batch_size - 1} spuIds range")
            proceedAllData(data_results)

            # обрабатываем results_data, записываем в файлы


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    asyncio.run(main(5_290_001, 6_000_001))
