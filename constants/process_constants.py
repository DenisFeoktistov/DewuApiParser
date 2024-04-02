import json


with open("constants/files/titling.json", encoding='utf-8') as f:
    TITLING = json.load(f)


with open("constants/files/genders.json", encoding='utf-8') as f:
    GENDERS = json.load(f)


with open("constants/files/category_names.json", encoding='utf-8') as f:
    CATEGORY_NAMES = json.load(f)


with open("constants/files/category_full_process.json", encoding='utf-8') as f:
    CATEGORY_FULL_PROCESS = json.load(f)


with open("constants/files/title_translations.json", encoding='utf-8') as f:
    TITLE_TRANSLATIONS = json.load(f)


with open("constants/files/spu_change_lines.json", encoding='utf-8') as f:
    SPU_CHANGE_LINES = json.load(f)
