from constants import GENDERS, CATEGORY_NAMES


def gendersProcess(preprocessedData: dict, finalProcessedDewuApiData: dict) -> dict:
    genders = []
    baseGenders = []
    extraGenders = []

    fitId = str(preprocessedData["fitId"])

    genders.extend(GENDERS[fitId])
    baseGenders.extend(GENDERS[fitId])

    # Так как у нас нет никаких размеров, а названия у пойзона плохие, придется сделать только 2 допущения: для fitId 2 и 3 добавляем второй гендер для обуви определенных брендов.

    addMenToWomen = [144, 13, 494, 10139, 3]
    addWomenToMen = [144, 13, 494, 10139, 3, 9, 34, 4, 33, 2, 8, 10098, 176, 6]

    categories = finalProcessedDewuApiData["categories"]
    categoryEng = ""
    for category in categories:
        if "Кроссовки" in CATEGORY_NAMES[category]["path"]:
            categoryEng = "sneakers"

    if fitId == "2" and categoryEng == "sneakers" and any(
            brandId in addWomenToMen for brandId in preprocessedData["allBrands"]):
        genders.append("F")
        extraGenders.append("F")

    if fitId == "3" and categoryEng == "sneakers" and any(
            brandId in addMenToWomen for brandId in preprocessedData["allBrands"]):
        genders.append("M")
        extraGenders.append("M")

    finalProcessedDewuApiData["gender"] = genders
    finalProcessedDewuApiData["baseGenders"] = baseGenders
    finalProcessedDewuApiData["extraGenders"] = extraGenders

    return finalProcessedDewuApiData
