from constants import CATEGORY_NAMES
from constants.process_constants import SIZE_TABLES_SHOES_BRANDS, CATEGORIES_WEIGHTS, SIZE_TABLES_ADJACENT_SHOES_BRANDS
import pydash as _


# Данная функция должна полностью собрать юниты, а также заполнить некоторые поля.
# - Собрать юниты: то, что будет отражено в выборе на странице товара. Сами юниты содержат информацию о связанном размере из таблицы для фильтров, название, id юнита, id фото (список), веса, оферы, поле showImage
# - Поле hasConfigurationsWithDifferentImages: Поле показывает, есть ли у этого товара конфигурации с разными фото -> на странице товара необходимо реализовать отображение картинок рядом с названием конфигурации.
# - Поле minPrice: Минимальная цена товара. Заполненность этого поля означает, что мы не знаем точных цен на конфигурации, но знаем общую минимальную цену товара. (p.s. Если мы принимаем решение, что перед нами товар одного размера, мы не заполняем это поле, а полноценно создаем офер в юните "одного размера")
# Примеры заполненного юнита (без офера и с офером): {
#     "view_name": "38 EU",
#     "unitId": 1,
#     "imagesIds": [0],
#     "filter_size_table_info": {
#         "table_name": "Shoes_Adults",
#         "table_row_name": "Европейский(EU)",
#         "sizes": ["38"]
#     },
#     "offers": [
#     ],
#     "weight": 1.5,
#     "height": 0,
#     "width": 0,
#     "length": 0
# }, {
#     "view_name": "Один размер",
#     "filter_size_table_info": {
#         "table_name": "",
#         "table_row_name": "",
#         "sizes": []
#     },
#     "offers": [
#         {
#             "price": 500.0,
#             "currency": "CNY",
#             "days_min_to_international_warehouse": 0,
#             "days_max_to_international_warehouse": 0,
#             "delivery_type": "express",
#             "platform_info": {
#                 "poizonNotFullApi": {
#                 }
#             }
#         }
#     ],
#     "weight": 1.5,
#     "height": 0,
#     "width": 0,
#     "length": 0
# }

def unitsAndImagesProcess(preprocessedData: dict, finalProcessedDewuApiData: dict) -> (dict, int):
    units = []
    images = []

    images_full = preprocessedData["images_full"]
    arSkuIdRelation = preprocessedData["arSkuIdRelation"]
    skus = preprocessedData["skus"]
    item = preprocessedData["item"]

    brands = finalProcessedDewuApiData["brands"]
    mainGender = finalProcessedDewuApiData["gender"][0]
    categories = finalProcessedDewuApiData["categories"]

    # region Получение верхне уровневой категории товара на английском языке: categoryEng
    categoryEng = ""
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

    # Для начала мы хотим понять, сколько у нас уникальных sku (предложений - конечных конфигураций) и сколько разных propertyId - фото разных товаров (цвета/комплектации)

    # Обработка поля images_full: если вообще нет фотографий, то мы все возвращаем нулевым
    if not images_full:
        return finalProcessedDewuApiData, 0

    # Собираем все уникальные значения propertyId
    allUniquePropertiesFromImages = []
    for image in images_full:
        if image["propertyValueId"] not in allUniquePropertiesFromImages and "url" in image:
            allUniquePropertiesFromImages.append(image["propertyValueId"])

    hasConfigurationsWithDifferentImages = True
    configsAmount = len(allUniquePropertiesFromImages)
    # Определяем, все ли фото относятся к одному товару
    if len(allUniquePropertiesFromImages) <= 1 or (
            len(allUniquePropertiesFromImages) == 2 and 0 in allUniquePropertiesFromImages):
        hasConfigurationsWithDifferentImages = False
        configsAmount = 0

    # Здесь можно добавить попытку определять, цвет перед нами или комплектация у самок/аксессуаров.

    # Определяем кол-во уникальных sku:
    allUniqueSkus = []
    if skus:
        for sku in skus:
            if sku["skuId"] not in allUniqueSkus:
                allUniqueSkus.append(sku["skuId"])
    if not allUniqueSkus and arSkuIdRelation:
        for arSkuId in arSkuIdRelation:
            if arSkuId["skuId"] not in allUniqueSkus:
                allUniqueSkus.append(arSkuId["skuId"])
    if not allUniqueSkus:
        return finalProcessedDewuApiData, 0

    imagesDict = []
    minPriceSkuId = _.get(item, "skuId", -1)
    minPrice = _.get(item, "floorPrice", 0) / 100
    maxPrice = _.get(item, "maxPrice", -100) / 100
    if hasConfigurationsWithDifferentImages and categoryEng != "shoes":
        minPricePropertyId = -1
        if minPriceSkuId != -1:
            for arSkuId in arSkuIdRelation:
                if "propertyValueId" in arSkuId and arSkuId[
                    "propertyValueId"] in allUniquePropertiesFromImages and "skuId" in arSkuId and arSkuId[
                    "skuId"] == minPriceSkuId:
                    minPricePropertyId = arSkuId["propertyValueId"]
                    break
            if minPricePropertyId == -1:
                for sku in skus:
                    if "skuId" in sku and sku["skuId"] == minPriceSkuId:
                        if "properties" in sku:
                            for property_ in sku["properties"]:
                                if _.get(property_, "propertyValueId", -1) in allUniquePropertiesFromImages:
                                    minPricePropertyId = property_["propertyValueId"]
                                    break

        if minPricePropertyId != -1:
            imagesDict.append(minPricePropertyId)
        for img in images_full:
            if img["propertyValueId"] not in imagesDict:
                imagesDict.append(img["propertyValueId"])

    offersBasedOnMinMaxPrice = []
    if 0 <= maxPrice - minPrice <= 50 and minPrice > 0 and maxPrice > 0:
        offersBasedOnMinMaxPrice = [{
            "price": maxPrice,
            "currency": "CNY",
            "days_min_to_international_warehouse": 3 if not _.get(item, "includeTax", False) else 10,
            "days_max_to_international_warehouse": 6 if not _.get(item, "includeTax", False) else 15,
            "delivery_type": "standard",
            "platform_info": {
                "poizonNotFullApi": {
                    "sku": -1,
                    "poizon_abroad": _.get(item, "includeTax", False)
                }
            }
        }]
    # Начинаем обработку. + Собираем список фото: кроме url, храним imageId, unitsIds - список юнитов, к которым эта фотка относится. Для товаров с одной фото-конфигурацией (и shoes) все imageId = 0, а списки unitsIds (просто range 1, len(units)). Если несколько, то
    #
    # 1. Обувь: Всегда вне зависимости от hasConfigurationsWithDifferentImages собираем базовый набор из юнитов (размеры в зависимости от бренда)
    if categoryEng == "shoes":
        hasConfigurationsWithDifferentImages = False
        if not any(brand in SIZE_TABLES_SHOES_BRANDS for brand in brands):
            euSizeRow = []
            tableName = ""
            if mainGender in ["M", "F"]:
                euSizeRow = [
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
                ]
                tableName = "Shoes_Adults"
            elif mainGender in ["K"]:
                euSizeRow = [
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
                tableName = "Shoes_Kids"
            allUnitsIds = []
            for i, size in enumerate(euSizeRow, start=1):
                allUnitsIds.append(i)
                units.append({
                    "view_name": f"{size} EU",
                    "unitId": i,
                    "imagesIds": [0],
                    "showImage": False,
                    "filter_size_table_info": {
                        "table_name": tableName,
                        "table_row_name": "Европейский(EU)",
                        "sizes": [size]
                    },
                    "offers": offersBasedOnMinMaxPrice,
                    "weight": CATEGORIES_WEIGHTS[categories[0]],
                    "height": 0,
                    "width": 0,
                    "length": 0
                })
            for image in images_full:
                if "url" in image:
                    images.append({
                        "imageId": 0,
                        "unitsIds": allUnitsIds,
                        "url": image["url"]
                    })
        elif any(brand in SIZE_TABLES_SHOES_BRANDS for brand in brands):
            mainBrand = ""
            for brand in brands:
                if brand in SIZE_TABLES_SHOES_BRANDS:
                    mainBrand = brand

            genderName = "Men" if mainGender == "M" else "Women" if mainGender == "F" else "Kids"
            tableName = "Shoes_Adults" if mainGender in ["M", "F"] else "Shoes_Kids"
            tableRowName = "Европейский(EU)"
            euSizeRow = []
            for row in SIZE_TABLES_SHOES_BRANDS[mainBrand][genderName]["allSizes"]:
                if row["name"] in ["EU", "EU/FR", "EU-wmns"]:
                    euSizeRow = row["sizes"]
                    break

            euSizeRowGeneral = [
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
            ] if mainGender in ["M", "F"] else [
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
            allUnitsIds = []
            for i, size in enumerate(euSizeRow, start=1):
                allUnitsIds.append(i)
                filterSizeRow = []

                sizeView = size.replace(" 1/3", "").replace(" 2/3", ".5")
                if sizeView in euSizeRowGeneral:
                    filterSizeRow.append(sizeView)
                filterSizeRow.extend(_.get(SIZE_TABLES_ADJACENT_SHOES_BRANDS[mainBrand][mainGender], sizeView, []))

                if not filterSizeRow:
                    tableName = ""
                    tableRowName = ""

                units.append({
                    "view_name": f"{size} EU",
                    "unitId": i,
                    "imagesIds": [0],
                    "showImage": False,
                    "filter_size_table_info": {
                        "table_name": tableName,
                        "table_row_name": tableRowName,
                        "sizes": filterSizeRow
                    },
                    "offers": offersBasedOnMinMaxPrice,
                    "weight": CATEGORIES_WEIGHTS[categories[0]],
                    "height": 0,
                    "width": 0,
                    "length": 0
                })
            for image in images_full:
                if "url" in image:
                    images.append({
                        "imageId": 0,
                        "unitsIds": allUnitsIds,
                        "url": image["url"]
                    })
    # 2. Одежда: Если не hasConfigurationsWithDifferentImages собираем базовый набор из юнитов. Если hasConfigurationsWithDifferentImages, то собираем с учетом фотографий.
    elif categoryEng == "clothes":
        if not hasConfigurationsWithDifferentImages:
            tableName = "Clothes_Men" if mainGender == "M" else "Clothes_Women" if mainGender == "F" else "Clothes_Kids"
            tableRowName = "Международный(INT)" if mainGender == "M" else "Международный(INT)" if mainGender == "F" else "Рост(СМ)"
            euSizeRow = [
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
            ] if mainGender == "M" else [
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
            ] if mainGender == "F" else [
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
            name = " CM (Рост)" if mainGender == "K" else ""

            allUnitsIds = []
            for i, size in enumerate(euSizeRow, start=1):
                allUnitsIds.append(i)
                units.append({
                    "view_name": size + name,
                    "unitId": i,
                    "imagesIds": [0],
                    "showImage": False,
                    "filter_size_table_info": {
                        "table_name": tableName,
                        "table_row_name": tableRowName,
                        "sizes": [size]
                    },
                    "offers": offersBasedOnMinMaxPrice,
                    "weight": CATEGORIES_WEIGHTS[categories[0]],
                    "height": 0,
                    "width": 0,
                    "length": 0
                })
            for image in images_full:
                if "url" in image:
                    images.append({
                        "imageId": 0,
                        "unitsIds": allUnitsIds,
                        "url": image["url"]
                    })
        else:
            tableName = "Clothes_Men" if mainGender == "M" else "Clothes_Women" if mainGender == "F" else "Clothes_Kids"
            tableRowName = "Международный(INT)" if mainGender == "M" else "Международный(INT)" if mainGender == "F" else "Рост(СМ)"
            euSizeRow = [
                "XXS",
                "XS",
                "S",
                "M",
                "L",
                "XL",
                "XXL"
            ] if mainGender == "M" else [
                "XXS",
                "XS",
                "S",
                "M",
                "L",
                "XL",
                "XXL"
            ] if mainGender == "F" else [
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
            name = " CM (Рост)" if mainGender == "K" else ""

            for i, propertyIdImage in enumerate(imagesDict, start=1):
                allUnitsIds = []
                for j, size in enumerate(euSizeRow, start=1):
                    allUnitsIds.append(j + (i - 1) * len(euSizeRow))
                    units.append({
                        "view_name": size + name,
                        "unitId": j + (i - 1) * len(euSizeRow),
                        "imagesIds": [i],
                        "showImage": True,
                        "filter_size_table_info": {
                            "table_name": tableName,
                            "table_row_name": tableRowName,
                            "sizes": [size]
                        },
                        "offers": offersBasedOnMinMaxPrice,
                        "weight": CATEGORIES_WEIGHTS[categories[0]],
                        "height": 0,
                        "width": 0,
                        "length": 0
                    })
                for image in images_full:
                    if image["propertyValueId"] == propertyIdImage and "url" in image:
                        images.append({
                            "imageId": i,
                            "unitsIds": allUnitsIds,
                            "url": image["url"]
                        })
    else:
        if not hasConfigurationsWithDifferentImages:
            offers = []
            if minPrice:
                offers = [{
                    "price": minPrice,
                    "currency": "CNY",
                    "days_min_to_international_warehouse": 3 if not _.get(item, "includeTax", False) else 10,
                    "days_max_to_international_warehouse": 6 if not _.get(item, "includeTax", False) else 15,
                    "delivery_type": "standard",
                    "platform_info": {
                        "poizonNotFullApi": {
                            "sku": _.get(item, "skuId", -1),
                            "poizon_abroad": _.get(item, "includeTax", False)
                        }
                    }
                }]
                minPrice = 0

            units.append({
                "view_name": "Один размер",
                "unitId": 1,
                "imagesIds": [0],
                "showImage": False,
                "filter_size_table_info": {
                    "table_name": "",
                    "table_row_name": "",
                    "sizes": []
                },
                "offers": offers,
                "weight": CATEGORIES_WEIGHTS[categories[0]],
                "height": 0,
                "width": 0,
                "length": 0
            })
            for image in images_full:
                if "url" in image:
                    images.append({
                        "imageId": 0,
                        "unitsIds": [1],
                        "url": image["url"]
                    })
        else:
            for i, propertyIdImage in enumerate(imagesDict, start=1):
                units.append({
                    "view_name": "Конфигурация №" + str(i),
                    "unitId": i,
                    "imagesIds": [i],
                    "showImage": True,
                    "filter_size_table_info": {
                        "table_name": "",
                        "table_row_name": "",
                        "sizes": []
                    },
                    "offers": offersBasedOnMinMaxPrice,
                    "weight": CATEGORIES_WEIGHTS[categories[0]],
                    "height": 0,
                    "width": 0,
                    "length": 0
                })
                for image in images_full:
                    if image["propertyValueId"] == propertyIdImage and "url" in image:
                        images.append({
                            "imageId": i,
                            "unitsIds": [i],
                            "url": image["url"]
                        })

    finalProcessedDewuApiData["images"] = images
    finalProcessedDewuApiData["units"] = units
    finalProcessedDewuApiData["hasConfigurationsWithDifferentImages"] = hasConfigurationsWithDifferentImages
    finalProcessedDewuApiData["minPrice"] = {
        "currency": "CNY",
        "price": minPrice if not offersBasedOnMinMaxPrice else 0
    }

    return finalProcessedDewuApiData, configsAmount
