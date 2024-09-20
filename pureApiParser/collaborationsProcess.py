from constants import TITLING, SPU_CHANGE_LINES
import pydash as _


def collaborationsProcess(preprocessedData: dict, finalProcessedDewuApiData: dict) -> (dict, str):
    is_collab = False

    # Список коллабораций для фильтра
    collab_names = []

    brandNameWithCollaboration = finalProcessedDewuApiData["brandName"]
    title = " " + preprocessedData["title"] + " "
    nameWithoutCollaborations = ""

    # region Find main brand
    brand_id = ""

    for brand_id1 in map(str, preprocessedData["allBrands"]):
        if brand_id1 not in TITLING:
            continue

        brand_id = brand_id1
        break
    # endregion

    # region Добавляем все коллаборации по вхождению строк в название, по брендам или конкретным артикулам
    collabsToFind = _.get(TITLING[brand_id], "collaborations", {})
    for collabToFind in collabsToFind:
        # if len(collab_names) != 0 and not _.get(titling_copy[brand_id], "many_collaborations", False):
        #     break

        collab_added = False

        for collab_name in _.get(collabsToFind[collabToFind], "collab_brand_names", list()):
            if collab_name.lower() in title.lower() and none_in_string(title.lower(), _.get(collabsToFind[collabToFind],
                                                                                            "collab_skip_names",
                                                                                            list())):
                collab_names.append(collabToFind)
                collab_added = True
                brandsToAdd = _.get(collabsToFind[collabToFind], "collab_brand_ids", list())
                for brandToAdd in brandsToAdd:
                    if int(brandToAdd) not in preprocessedData["allBrands"]:
                        preprocessedData["allBrands"].append(int(brandToAdd))
                    if brandToAdd in TITLING and TITLING[brandToAdd]["brand_names"][0] not in finalProcessedDewuApiData[
                        "brands"]:
                        finalProcessedDewuApiData["brands"].append(TITLING[brandToAdd]["brand_names"][0])
                break

        if collab_added:
            continue

        for collab_brand_id in _.get(collabsToFind[collabToFind], "collab_brand_ids", list()):
            if collab_brand_id in map(str, preprocessedData["allBrands"]):
                collab_names.append(collabToFind)
                collab_added = True
                break

        if collab_added:
            continue

        if preprocessedData["manufacturer_sku"] in _.get(collabsToFind[collabToFind], "collab_skus", list()):
            collab_names.append(collabToFind)

            brandsToAdd = _.get(collabsToFind[collabToFind], "collab_brand_ids", list())
            for brandToAdd in brandsToAdd:
                if int(brandToAdd) not in preprocessedData["allBrands"]:
                    preprocessedData["allBrands"].append(int(brandToAdd))
                if brandToAdd in TITLING and TITLING[brandToAdd]["brand_names"][0] not in finalProcessedDewuApiData[
                    "brands"]:
                    finalProcessedDewuApiData["brands"].append(TITLING[brandToAdd]["brand_names"][0])

    # endregion

    # region Дополнительно удаляем коллаборации у некоторых товаров
    for spu_change_line in SPU_CHANGE_LINES:
        if spu_change_line == str(preprocessedData["spuId"]):
            for collab_to_remove in _.get(SPU_CHANGE_LINES[spu_change_line], "collabs_to_remove", []):
                collab_names.remove(collab_to_remove)
    # endregion

    # Определяем в итоге, является ли товар коллаборацией
    if len(collab_names) > 0 or len(preprocessedData["allBrands"]) > 1 or " x " in title.lower():
        is_collab = True

    # Создаем brandNameWithCollaboration - бренд с коллаборацией -> будет в поле brandName на карточке товара
    if collab_names:
        brandNameWithCollaboration = collab_names[0]

    # region Создаем nameWithoutCollaborations - название, из которого вырезана коллаборация (она указана в brandNameWithCollaboration)
    # Вначале пытаемся вырезать строки от первой коллаборации
    if collab_names:
        for collab_name in sorted(_.get(collabsToFind[collab_names[0]], "collab_brand_names", list()),
                                  key=lambda s: -len(s)):
            if collab_name.lower() in title.lower():
                for collab_name_no_crop in sorted(
                        _.get(collabsToFind[collab_names[0]], "collab_brand_names_no_crop", list()),
                        key=lambda s: -len(s)):
                    if collab_name_no_crop.lower() in collab_name.lower():
                        nameWithoutCollaborations = remove_substring(title, collab_name.strip(), collab_name_no_crop.strip())
                        break
                else:
                    nameWithoutCollaborations = remove_substring(title, collab_name.strip())
        if not nameWithoutCollaborations:
            brId = _.get(collabsToFind[collab_names[0]], "collab_brand_ids.0", "")
            brNames = _.get(TITLING, f'{brId}.brand_names', [])
            for brName in brNames:
                if brName.lower() in title.lower():
                    nameWithoutCollaborations = remove_substring(title, brName.strip())
                    break
    # Если нами созданной коллаборации не обнаружено, но брендов несколько, то есть коллаборация, то находим все известные нам бренды, добавляем их в название бренда и вырезаем из остального названия.
    elif len(preprocessedData["allBrands"]) > 1:
        for br in preprocessedData["allBrands"]:
            if str(br) in TITLING and br != brand_id:
                brName = TITLING[str(br)]["brand_names"][0]
                brandNameWithCollaboration = brandNameWithCollaboration + " x " + brName
                if brName.lower() in title.lower():
                    nameWithoutCollaborations = remove_substring(title, brName.strip())

    else:
        nameWithoutCollaborations = title.strip()

    # endregion

    finalProcessedDewuApiData["is_collab"] = is_collab
    finalProcessedDewuApiData["collab_names"] = collab_names
    finalProcessedDewuApiData["brandName"] = brandNameWithCollaboration

    return finalProcessedDewuApiData, nameWithoutCollaborations


def none_in_string(input_string, string_list):
    for item in string_list:
        if item.lower() in input_string.lower():
            return False
    return True


def remove_substring(s, sub, replace=""):
    s_lower = s.lower()
    sub_lower = sub.lower()

    start = s_lower.find(sub_lower)

    if start != -1:
        end = start + len(sub)

        s = " ".join((s[:start] + replace + s[end:]).split())

    return s
