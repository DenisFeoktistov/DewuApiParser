from constants import TITLING, SPU_CHANGE_LINES
import pydash as _


def linesProcess(preprocessedData: dict, finalProcessedDewuApiData: dict, nameWithoutCollaborations: str) -> (
        dict, str):
    lines = list()
    title = " " + preprocessedData["title"] + " "

    nameWithoutLines = nameWithoutCollaborations

    # region Find main brand
    brand_id = ""

    for brand_id1 in map(str, preprocessedData["allBrands"]):
        if brand_id1 not in TITLING:
            continue

        brand_id = brand_id1
        break
    # endregion

    # region Find lines
    linesToFind = _.get(TITLING[brand_id], "lines", [])

    for line in linesToFind:
        for line_name in line["line_names"]:
            if line_name.lower() in title.lower() and none_in_string(title.lower(), _.get(line, "line_skip_names", [])):
                lines.append(line)
                break

        if len(lines) != 0 and not _.get(TITLING[brand_id], "many_lines", False):
            break
    # endregion

    # region Создаем nameWithoutLines - название, из которого вырезаны линейка (она будет указана в model)
    if lines:
        for line_name in sorted(_.get(lines[0], "line_names", list()), key=lambda s: -len(s)):
            if line_name.lower() in nameWithoutCollaborations.lower():
                for line_name_no_crop in sorted(_.get(lines[0], "line_name_no_crop", list()), key=lambda s: -len(s)):
                    if line_name_no_crop.lower() in line_name.lower():
                        nameWithoutLines = remove_substring(nameWithoutCollaborations, line_name.strip(), line_name_no_crop.strip())
                        break
                else:
                    nameWithoutLines = remove_substring(nameWithoutCollaborations, line_name.strip())
                break
    # endregion

    # region Try to replace "Другие Jordan 1" to "High/Mid/Low"
    other_jordan_1_line = {
        "path": [
            "Jordan",
            "Air Jordan 1",
            "Другие Air Jordan 1"
        ],
        "line_names": [
            "Air Jordan 1 ",
            "Air Jordan retro 1 ",
            "jordan 1 ",
            "jordan retro 1 "
        ],
        "line_name_no_crop": [
            "retro"
        ]
    }
    air_jordan_1_high_line = {
        "path": [
            "Jordan",
            "Air Jordan 1",
            "Air Jordan 1 High"
        ],
        "line_names": [
            "Air Jordan 1 high",
            "Air Jordan high 1 ",
            "Air Jordan 1 retro high",
            "air jordan retro 1 high",
            "air jordan retro high 1 ",
            "jordan 1 high",
            "jordan high 1 ",
            "jordan retro 1 high",
            "jordan retro high 1 ",
            "jordan 1 retro high",
            "Air Jordan 1 hi "
        ],
        "line_name_no_crop": [
            "retro"
        ]
    }
    air_jordan_1_mid_line = {
        "path": [
            "Jordan",
            "Air Jordan 1",
            "Air Jordan 1 Mid"
        ],
        "line_names": [
            "Air Jordan 1 mid",
            "Air Jordan mid 1 ",
            "Air Jordan 1 retro mid",
            "air jordan retro 1 mid",
            "air jordan retro high 1 ",
            "jordan 1 mid",
            "jordan mid 1 ",
            "jordan retro 1 mid",
            "jordan retro high 1 ",
            "jordan 1 retro mid"
        ],
        "line_name_no_crop": [
            "retro"
        ]
    }
    air_jordan_1_low_line = {
        "path": [
            "Jordan",
            "Air Jordan 1",
            "Air Jordan 1 Low"
        ],
        "line_names": [
            "Air Jordan 1 low",
            "Air Jordan low 1 ",
            "Air Jordan 1 retro low",
            "air jordan retro 1 low",
            "air jordan retro high 1 ",
            "jordan 1 low",
            "jordan low 1 ",
            "jordan retro 1 low",
            "jordan retro high 1 ",
            "jordan 1 retro low"
        ],
        "line_name_no_crop": [
            "retro"
        ]
    }
    if other_jordan_1_line in lines:
        if "高帮" in title.lower():
            lines.remove(other_jordan_1_line)
            lines.append(air_jordan_1_high_line)
        elif "低帮" in title.lower():
            lines.remove(other_jordan_1_line)
            lines.append(air_jordan_1_low_line)
        elif "中帮" in title.lower():
            lines.remove(other_jordan_1_line)
            lines.append(air_jordan_1_mid_line)
    # endregion

    # region Try to replace "Другие Dunk" to "High/Mid/Low"
    other_dunk_line = {
        "path": [
            "Nike",
            "Nike Dunk",
            "Другие Nike Dunk"
        ],
        "line_names": [
            "dunk"
        ],
        "line_skip_names": []
    }
    dunk_high_line = {
        "path": [
            "Nike",
            "Nike Dunk",
            "Nike Dunk High"
        ],
        "line_names": [
            "dunk high",
            "high dunk",
            "dunk pro high",
            "high pro dunk",
            "dunk sb high",
            "high sb dunk",
            "dunk sb pro high",
            "dunk pro sb high",
            "high pro sb dunk",
            "high sb pro dunk"
        ],
        "line_skip_names": [],
        "line_name_no_crop": [
            "pro sb",
            "sb pro",
            "pro",
            "sb"
        ]
    }
    dunk_mid_line = {
        "path": [
            "Nike",
            "Nike Dunk",
            "Nike Dunk Mid"
        ],
        "line_names": [
            "dunk mid",
            "mid dunk",
            "dunk pro mid",
            "mid pro dunk",
            "dunk sb mid",
            "mid sb dunk",
            "dunk sb pro mid",
            "dunk pro sb mid",
            "mid pro sb dunk",
            "mid sb pro dunk"
        ],
        "line_skip_names": [],
        "line_name_no_crop": [
            "pro sb",
            "sb pro",
            "pro",
            "sb"
        ]
    }
    dunk_low_line = {
        "path": [
            "Nike",
            "Nike Dunk",
            "Nike Dunk Low"
        ],
        "line_names": [
            "dunk low",
            "low dunk",
            "dunk pro low",
            "low pro dunk",
            "dunk sb low",
            "low sb dunk",
            "dunk sb pro low",
            "dunk pro sb low",
            "low pro sb dunk",
            "low sb pro dunk"
        ],
        "line_skip_names": [],
        "line_name_no_crop": [
            "pro sb",
            "sb pro",
            "pro",
            "sb"
        ]
    }
    if other_dunk_line in lines:
        if "高帮" in title.lower():
            lines.remove(other_dunk_line)
            lines.append(dunk_high_line)
        elif "低帮" in title.lower():
            lines.remove(other_dunk_line)
            lines.append(dunk_low_line)
        elif "中帮" in title.lower():
            lines.remove(other_dunk_line)
            lines.append(dunk_mid_line)
    # endregion

    # region Try to replace "Другие Nike AF1" to "High/Mid/Low"
    other_force_line = {
        "path": [
            "Nike",
            "Nike Air Force 1",
            "Другие Nike Air Force 1"
        ],
        "line_names": [
            "air force 1",
            "af1"
        ],
        "line_skip_names": []
    }
    force_high_line = {
        "path": [
            "Nike",
            "Nike Air Force 1",
            "Nike Air Force 1 High"
        ],
        "line_names": [
            "air force 1 high",
            "af1 high"
        ],
        "line_skip_names": []
    }
    force_mid_line = {
        "path": [
            "Nike",
            "Nike Air Force 1",
            "Nike Air Force 1 Mid"
        ],
        "line_names": [
            "air force 1 mid",
            "af1 mid"
        ],
        "line_skip_names": []
    }
    force_low_line = {
        "path": [
            "Nike",
            "Nike Air Force 1",
            "Nike Air Force 1 Low"
        ],
        "line_names": [
            "air force 1 low",
            "af1 low"
        ],
        "line_skip_names": []
    }
    if other_force_line in lines:
        if "高帮" in title.lower():
            lines.remove(other_force_line)
            lines.append(force_high_line)
        elif "低帮" in title.lower():
            lines.remove(other_force_line)
            lines.append(force_low_line)
        elif "中帮" in title.lower():
            lines.remove(other_force_line)
            lines.append(force_mid_line)
    # endregion

    # region Изменяю дополнительно какие-то линейки у конкретных товаров
    for spu_change_line in SPU_CHANGE_LINES:
        if spu_change_line == str(preprocessedData["spuId"]):
            for line_to_remove in _.get(SPU_CHANGE_LINES[spu_change_line], "lines_to_remove", []):
                lines.remove(line_to_remove)
            for line_to_add in _.get(SPU_CHANGE_LINES[spu_change_line], "lines_to_add", []):
                lines.append(line_to_add)
    # endregion

    finalLines = [line["path"] for line in lines]

    finalProcessedDewuApiData["lines"] = finalLines

    return finalProcessedDewuApiData, nameWithoutLines


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
