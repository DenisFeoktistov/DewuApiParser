import json

with open(r"C:\Users\HP\PycharmProjects\DewuApiParser\Tests\constants\allCategories.json", encoding='utf-8') as f:
    ALL_CATEGORIES = json.load(f)

with open(r"C:\Users\HP\PycharmProjects\DewuApiParser\Tests\constants\articles.json", encoding='utf-8') as f:
    ARTICLES = json.load(f)

with open(r"C:\Users\HP\PycharmProjects\DewuApiParser\Tests\constants\configs.json", encoding='utf-8') as f:
    CONFIGS = json.load(f)

with open(r"C:\Users\HP\PycharmProjects\DewuApiParser\Tests\constants\genders.json", encoding='utf-8') as f:
    GENDERS = json.load(f)

with open(r"C:\Users\HP\PycharmProjects\DewuApiParser\Tests\constants\invalidDates.json", encoding='utf-8') as f:
    INVALID_DATES = json.load(f)

with open(r"C:\Users\HP\PycharmProjects\DewuApiParser\Tests\constants\processedSpus.json", encoding='utf-8') as f:
    PROCESSED_SPUS = json.load(f)

with open(r"C:\Users\HP\PycharmProjects\DewuApiParser\Tests\constants\strangeData.json", encoding='utf-8') as f:
    STRANGE_DATA = json.load(f)
