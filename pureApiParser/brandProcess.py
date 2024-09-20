from constants import TITLING


def brandProcess(preprocessedData: dict, finalProcessedDewuApiData: dict) -> dict:
    for brand_id in map(str, preprocessedData["allBrands"]):
        if brand_id in TITLING:
            finalProcessedDewuApiData["brands"].append(TITLING[brand_id]["brand_names"][0])

    finalProcessedDewuApiData["brandName"] = finalProcessedDewuApiData["brands"][0]

    return finalProcessedDewuApiData
