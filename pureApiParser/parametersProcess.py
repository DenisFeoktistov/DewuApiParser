from constants.process_constants import PARAMETERS


# Так как с этим API мы можем определять параметры только по названию, придется по нему и определять.
# Мы пытаемся определить следующие параметры:
# "colors", "material" - для фильтров и отображения на странице товара
# "upper_height", "heel_type", "boots_height", "sleeve_length", "collar_type", "closure_type" - для определения категории (ну и для рекомендаций поможет слегка)
# У нас есть словарь с подстроками и значениями этих параметров, по нему и будем пытаться что-нибудь определить.
def parametersProcess(preprocessedData: dict, finalProcessedDewuApiData: dict) -> dict:
    parameters_to_show_in_product = {
        "parameters": {},
        "parameters_order": [
            "Основные цвета",
            "Материалы",
            "Цена на ритейле"
        ]
    }

    parameters_to_use_in_filters = {
        "colors": [],
        "material": [],
        "upper_height": [],
        "heel_type": [],
        "boots_height": [],
        "length": [],
        "sleeve_length": [],
        "collar_type": [],
        "closure_type": []
    }

    colorsRu = ""
    materialsRu = ""

    title = " " + preprocessedData["title"] + " "

    retailPrice = finalProcessedDewuApiData["retailPrice"]["price"]

    for mainParam in PARAMETERS["mainParams"]:
        for titleSub in PARAMETERS["mainParams"][mainParam]:
            if titleSub.lower() in title.lower():
                parameters_to_use_in_filters[mainParam].extend(PARAMETERS["mainParams"][mainParam][titleSub]["name"])
                if mainParam == "colors" and PARAMETERS["mainParams"][mainParam][titleSub][
                    "russian_name"] not in colorsRu:
                    colorsRu += PARAMETERS["mainParams"][mainParam][titleSub]["russian_name"] + ", "
                if mainParam == "material" and PARAMETERS["mainParams"][mainParam][titleSub][
                    "russian_name"] not in materialsRu:
                    materialsRu += PARAMETERS["mainParams"][mainParam][titleSub]["russian_name"] + ", "

        parameters_to_use_in_filters[mainParam] = list(set(parameters_to_use_in_filters[mainParam]))

    colorsRu = colorsRu.strip().rstrip(',')
    materialsRu = materialsRu.strip().rstrip(',')

    if colorsRu:
        parameters_to_show_in_product["parameters"]["Основные цвета"] = colorsRu

    if materialsRu:
        parameters_to_show_in_product["parameters"]["Материалы"] = materialsRu

    if retailPrice:
        parameters_to_show_in_product["parameters"]["Цена на ритейле"] = f"{round(retailPrice * 13, -2)}₽"

    for otherParam in PARAMETERS["otherParams"]:
        for titleSub in PARAMETERS["otherParams"][otherParam]:
            if titleSub.lower() in title.lower():
                parameters_to_use_in_filters[otherParam].append(PARAMETERS["otherParams"][otherParam][titleSub])
        parameters_to_use_in_filters[otherParam] = list(set(parameters_to_use_in_filters[otherParam]))

    finalProcessedDewuApiData["parameters_to_show_in_product"] = parameters_to_show_in_product
    finalProcessedDewuApiData["parameters_to_use_in_filters"] = parameters_to_use_in_filters

    return finalProcessedDewuApiData
