import re

from constants import CATEGORY_NAMES
from infrastructure.addProductDataToSelloutBase import addProductDataToSelloutBase


# Данная ф-ция должна найти или не найти товар в базе уже существующих товаров с помощью артикула и передать информацию следующей функции - addProductDataToSelloutBase для дальнейшей обработки: добавлении новых данных
def findProductInSelloutBase(platformName: str, productInfo: dict, preprocessedProductInfo: dict):
    # TODO: ALL_SKUS_SELLOUT - моковый объект, в котором должна содержаться структура для связки с товаром из базы Sellout. Логику использования адаптировать под реальный формат. Сейчас у меня написано, будто под ключом артикула лежит вся информация об этом товаре. Важное замечание, что если мы нашли несколько товаров с таким артикулом, то не связываем ни с одним товаром!
    ALL_SKUS_SELLOUT = {
        "AAA": {

        }
    }
    manufacturerSkus = []

    if platformName == "poizonNotFullApi":
        manufacturerSkus.append(productInfo["manufacturer_sku"])
        manufacturerSkus.extend(productInfo["other_manufacturer_skus"])
    elif platformName == "goat":
        manufacturerSkus.append(productInfo["manufacturer_sku"])

    # TODO: Если мы нашли несколько товаров с таким артикулом, то не связываем ни с одним товаром!
    # if найдено many skus: # запускаем процесс добавления как будто бы нового товара
    # addProductDataToSelloutBase(platformOfAddingProduct=platformName,
    #                                 productInfoToAdd=productInfo,
    #                                 sameProductFromSelloutBase={},
    #                                 preprocessedProductInfoToAdd=preprocessedProductInfo)

    for sku in manufacturerSkus:
        # Если не измененный артикул есть в нашей базе:
        if sku in ALL_SKUS_SELLOUT:
            # Делаем проверки, что совпадает бренд и категория:
            if any(brand in ALL_SKUS_SELLOUT[sku]["brands"] for brand in productInfo["brands"]) and \
                    CATEGORY_NAMES[productInfo["categories"][0]]["path"][0] == \
                    CATEGORY_NAMES[ALL_SKUS_SELLOUT[sku]["categories"][0]]["path"][0]:
                # Если нашли этот товар в нашей базе, то получаем всю информацию об этом товаре (в данном случае это ALL_SKUS_SELLOUT[sku]), и передаем все в следующую функцию инфраструктуры - addProductDataToSelloutBase, то есть связывание данных с новой платформы с уже существующим товаром в нашей базе.
                addProductDataToSelloutBase(platformOfAddingProduct=platformName,
                                            productInfoToAdd=productInfo,
                                            sameProductFromSelloutBase=ALL_SKUS_SELLOUT[sku],
                                            preprocessedProductInfoToAdd=preprocessedProductInfo)
                return

    for sku in manufacturerSkus:
        modifiedSku = re.sub(r'[^a-zA-Z0-9]', '', sku)
        # Если измененный артикул есть в нашей базе:
        if modifiedSku in ALL_SKUS_SELLOUT:
            # Делаем проверки, что совпадает бренд и категория:
            if any(brand in ALL_SKUS_SELLOUT[modifiedSku]["brands"] for brand in productInfo["brands"]) and \
                    CATEGORY_NAMES[productInfo["categories"][0]]["path"][0] == \
                    CATEGORY_NAMES[ALL_SKUS_SELLOUT[modifiedSku]["categories"][0]]["path"][0]:
                # Если нашли этот товар в нашей базе, то получаем всю информацию об этом товаре (в данном случае это ALL_SKUS_SELLOUT[modifiedSku]), и передаем все в следующую функцию инфраструктуры - addProductDataToSelloutBase, то есть связывание данных с новой платформы с уже существующим товаром в нашей базе.
                addProductDataToSelloutBase(platformOfAddingProduct=platformName,
                                            productInfoToAdd=productInfo,
                                            sameProductFromSelloutBase=ALL_SKUS_SELLOUT[modifiedSku],
                                            preprocessedProductInfoToAdd=preprocessedProductInfo)
                return

    # Если не удалось связать с существующим товаром, то передаем в следующую функцию инфраструктуры - addProductDataToSelloutBase пустой словарь в качестве sameProductFromSelloutBase.
    addProductDataToSelloutBase(platformOfAddingProduct=platformName,
                                productInfoToAdd=productInfo,
                                sameProductFromSelloutBase={},
                                preprocessedProductInfoToAdd=preprocessedProductInfo)
