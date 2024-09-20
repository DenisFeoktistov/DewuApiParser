import re

from constants import TITLING
from constants.process_constants import CATEGORIES_NAMING


def nameProcess(preprocessedData: dict, finalProcessedDewuApiData: dict,
                nameWithoutCollaborationsAndLines: str, configsAmount: int) -> dict:
    model = ""
    colorway = ""

    finalName = nameWithoutCollaborationsAndLines

    categories = finalProcessedDewuApiData["categories"]

    # region Find main brand
    brand_id = ""

    for brand_id1 in map(str, preprocessedData["allBrands"]):
        if brand_id1 not in TITLING:
            continue

        brand_id = brand_id1
        break
    # endregion

    # Убираем бренд из названия
    for brand_name in sorted(TITLING[brand_id]["brand_names"], key=lambda s: -len(s)):
        if brand_name.lower() in finalName.lower():
            finalName = remove_substring(finalName, brand_name)
            break
    # Убираем " х " из названия (сколько коллабораций, столько раз и пробуем убрать)
    for collab_name in finalProcessedDewuApiData["collab_names"]:
        for i in range(collab_name.count("x")):
            finalName = remove_substring(finalName, "x")
    if finalProcessedDewuApiData["is_collab"]:
        for i in range(finalName.count(" x ")):
            finalName = finalName.replace(" x ", "")

    finalName = remove_chinese_symbols(finalName)
    finalName = finalName.rstrip("#")
    finalName = finalName.replace("】", " ").replace("【", " ")
    finalName = finalName.strip("-")
    finalName = finalName.strip("-")
    finalName = finalName.strip("/")
    finalName = finalName.strip("|")
    finalName = finalName.strip("\\")
    finalName = finalName.strip(".")
    finalName = finalName.strip(",")
    finalName = " ".join(finalName.split()).strip()

    if finalProcessedDewuApiData["lines"]:
        lineName = finalProcessedDewuApiData["lines"][0][-1]

        if "Другие" in lineName:
            if lineName == "Другие Air Jordan 1":
                finalLineName = "Air Jordan 1"
            elif lineName == "Другие Yeezy":
                finalLineName = "Yeezy"
            else:
                finalLineName = ' '.join(lineName.split()[2:])
        elif 13 in preprocessedData["allBrands"]:
            if lineName.startswith("Air"):
                finalLineName = lineName
            else:
                finalLineName = lineName.replace("Jordan", "").strip()
        else:
            finalLineName = lineName.replace(finalProcessedDewuApiData["lines"][0][0], "").strip()

        if "Баскетбольные кроссовки" in categories:
            model = finalLineName
            colorway = ("Баскетбольные " + finalName).strip()
        elif CATEGORIES_NAMING[categories[0]]:
            model = finalLineName
            colorway = (CATEGORIES_NAMING[categories[0]] + " " + finalName).strip()
        else:
            if len(finalName) < 7:
                model = (finalLineName + " " + finalName).strip()
            else:
                model = finalLineName
                colorway = finalName
    else:
        colorway = (CATEGORIES_NAMING[categories[0]] + " " + finalName).strip()
        if configsAmount:
            colorway = colorway + " " + get_color_phrase(configsAmount)

    if colorway:
        colorway = (colorway[0].upper() + colorway[1:]).strip()

    finalProcessedDewuApiData["model"] = model
    finalProcessedDewuApiData["colorway"] = colorway

    return finalProcessedDewuApiData


def get_color_phrase(number):
    if 11 <= number % 100 <= 19:  # Обработка чисел от 11 до 19
        suffix = "ти"
        color_word = "цветах"
    else:
        last_digit = number % 10
        if last_digit == 1:
            suffix = "ом"
            color_word = "цвете"
        elif 2 <= last_digit <= 4:
            suffix = "ух"
            color_word = "цветах"
        else:
            suffix = "ти"
            color_word = "цветах"

    return f"в {number}-{suffix} {color_word}"


def remove_substring(s, sub, replace=""):
    s_lower = s.lower()
    sub_lower = sub.lower()

    start = s_lower.find(sub_lower)

    if start != -1:
        end = start + len(sub)

        s = " ".join((s[:start] + replace + s[end:]).split())

    return s


def remove_chinese_symbols(text):
    chinese_pattern = "[\u4e00-\u9FFF|\u3400-\u4DBF|\U00020000-\U0002A6DF|\U0002A700-\U0002B73F|\U0002B740-\U0002B81F|\U0002B820-\U0002CEAF|\uF900-\uFAFF|\U0002F800-\U0002FA1F]"
    without_chinese = re.sub(chinese_pattern, '', text)
    without_chinese = ' '.join(without_chinese.split())
    return without_chinese
