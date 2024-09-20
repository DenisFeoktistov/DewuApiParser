import re


def dateProcess(preprocessedData: dict, finalProcessedDewuApiData: dict) -> dict:
    releaseDate = preprocessedData["releaseDate"]

    if releaseDate == "":
        finalProcessedDewuApiData["date"] = "22.02.2022"
        return finalProcessedDewuApiData

    # Проверяем, если это просто 4 цифры (год)
    if re.match(r"^\d{4}$", releaseDate):
        finalProcessedDewuApiData["date"] = f"02.07.{releaseDate}"
        finalProcessedDewuApiData["approximate_date"] = f"02.07.{releaseDate}"
        return finalProcessedDewuApiData

    # Пытаемся обработать формат YYYY.MM.DD или YYYY.M.DD
    if re.match(r"^\d{4}\.\d{1,2}\.\d{2}$", releaseDate):
        parts = releaseDate.split('.')
        finalProcessedDewuApiData["date"] = f"{parts[2]}.{parts[1].zfill(2)}.{parts[0]}"
        finalProcessedDewuApiData["approximate_date"] = f"{parts[2]}.{parts[1].zfill(2)}.{parts[0]}"
        return finalProcessedDewuApiData

    # Проверка на формат YYYY.MM
    if re.match(r"^\d{4}\.\d{2}$", releaseDate):
        year, month = releaseDate.split(".")
        finalProcessedDewuApiData["date"] = f"01.{month}.{year}"
        finalProcessedDewuApiData["approximate_date"] = f"{month}.{year}"
        return finalProcessedDewuApiData

    releaseDate = releaseDate.replace("年", "")

    # Пытаемся обработать формат YYYY-MM-DD
    if re.match(r"^\d{4}-\d{2}-\d{2}$", releaseDate):
        parts = releaseDate.split('-')
        finalProcessedDewuApiData["date"] = f"{parts[2]}.{parts[1]}.{parts[0]}"
        finalProcessedDewuApiData["approximate_date"] = f"{parts[2]}.{parts[1]}.{parts[0]}"
        return finalProcessedDewuApiData

    if "春夏" in releaseDate:
        finalProcessedDewuApiData["date"] = "04.05." + releaseDate.rstrip("春夏").rstrip(".")
        finalProcessedDewuApiData["approximate_date"] = "Весна/лето " + releaseDate.rstrip("春夏")
        return finalProcessedDewuApiData
    elif "秋冬" in releaseDate:
        finalProcessedDewuApiData["date"] = "16.10." + releaseDate.rstrip("秋冬").rstrip(".")
        finalProcessedDewuApiData["approximate_date"] = "Осень/зима " + releaseDate.rstrip("秋冬")
        return finalProcessedDewuApiData
    elif "秋季" in releaseDate:
        finalProcessedDewuApiData["date"] = "27.09." + releaseDate.rstrip("秋季").rstrip(".")
        finalProcessedDewuApiData["approximate_date"] = "Осень " + releaseDate.rstrip("秋季")
        return finalProcessedDewuApiData
    elif "冬季" in releaseDate:
        finalProcessedDewuApiData["date"] = "01.01." + releaseDate.rstrip("冬季").rstrip(".")
        finalProcessedDewuApiData["approximate_date"] = "Зима " + releaseDate.rstrip("冬季")
        return finalProcessedDewuApiData
    elif "春季" in releaseDate:
        finalProcessedDewuApiData["date"] = "01.03." + releaseDate.rstrip("春季").rstrip(".")
        finalProcessedDewuApiData["approximate_date"] = "Весна " + releaseDate.rstrip("春季")
        return finalProcessedDewuApiData
    elif "夏季" in releaseDate:
        finalProcessedDewuApiData["date"] = "09.08." + releaseDate.rstrip("夏季").rstrip(".")
        finalProcessedDewuApiData["approximate_date"] = "Лето " + releaseDate.rstrip("夏季")
        return finalProcessedDewuApiData

    return finalProcessedDewuApiData
