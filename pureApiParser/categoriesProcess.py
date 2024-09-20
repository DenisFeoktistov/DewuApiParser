import copy
import pydash as _

from constants import GENDERS, CATEGORY_FULL_PROCESS


# В CATEGORY_FULL_PROCESS лежит словарь, который по ID категории определяет основную категорию, а также предлагает условия для добавления дополнительных категорий
# 4 доп способа: по названию, по гендеру, по параметрам, по цене (этот способ для обработки без цен недоступен).
# "1000108": {
#     "categories_to_add_directly": [
#       "Кроссовки"
#     ],
#     "categories_to_add_by_title": [],
#     "categories_to_add_by_gender": [],
#     "categories_to_add_by_parameters": [],
#     "categories_to_add_by_min_price": []
#   }


def categoriesProcess(preprocessedData: dict, finalProcessedDewuApiData: dict) -> dict:
    categoriesFinal = []

    title = preprocessedData["title"]
    categoryId = preprocessedData["categoryId"]
    categoryName = preprocessedData["categoryName"]
    level1CategoryId = preprocessedData["level1CategoryId"]
    level2CategoryId = preprocessedData["level2CategoryId"]
    min_price = _.get(preprocessedData, "item.floorPrice", 0)

    parameters = finalProcessedDewuApiData["parameters_to_use_in_filters"]

    # Базовое получение гендеров (необходимо для одного из способов определения категории
    genders = GENDERS[str(preprocessedData["fitId"])]

    # Добавляем базовые категории по первому ID
    if str(categoryId) in CATEGORY_FULL_PROCESS:
        categoriesFinal.extend(copy.deepcopy(CATEGORY_FULL_PROCESS[str(categoryId)]["categories_to_add_directly"]))
    else:
        categoriesFinal.extend(["Другие аксессуары"])

    # Добавляем категории по вхождениям в title
    for category_to_add_by_title in _.get(CATEGORY_FULL_PROCESS, f"{str(categoryId)}.categories_to_add_by_title", []):
        if any(subtitle.lower() in title for subtitle in category_to_add_by_title["any_subtitles"]):
            categoriesFinal = [category for category in categoriesFinal if
                               category not in category_to_add_by_title["main_names_to_delete"]]
            categoriesFinal.extend(category_to_add_by_title["main_names_to_add"])

    # Добавляем категории по гендеру
    for category_to_add_by_gender in _.get(CATEGORY_FULL_PROCESS, f"{str(categoryId)}.categories_to_add_by_gender", []):
        if any(gender_in_cat in genders for gender_in_cat in category_to_add_by_gender["genders"]):
            categoriesFinal = [category for category in categoriesFinal if
                               category not in category_to_add_by_gender["main_names_to_delete"]]
            categoriesFinal.extend(category_to_add_by_gender["main_names_to_add"])

    # Добавляем категории по параметрам
    for category_to_add_by_parameters in _.get(CATEGORY_FULL_PROCESS,
                                               f"{str(categoryId)}.categories_to_add_by_parameters", []):
        for parameter in category_to_add_by_parameters["any_parameters"]:
            if any(param in parameters[parameter] for param in
                   category_to_add_by_parameters["any_parameters"][parameter]):
                categoriesFinal = [category for category in categoriesFinal if
                                   category not in category_to_add_by_parameters["main_names_to_delete"]]
                categoriesFinal.extend(category_to_add_by_parameters["main_names_to_add"])

    # Добавляем категории по минимальной цене
    if min_price > 0:
        for category_to_add_by_min_price in _.get(CATEGORY_FULL_PROCESS,
                                                  f"{str(categoryId)}.categories_to_add_by_min_price", []):
            if min_price >= category_to_add_by_min_price["min_price"]:
                categoriesFinal = [category for category in categoriesFinal if
                                   category not in category_to_add_by_min_price["main_names_to_delete"]]
                categoriesFinal.extend(category_to_add_by_min_price["main_names_to_add"])

    # Убираем дубликаты
    c_ = copy.deepcopy(categoriesFinal)
    categoriesFinal = []

    for c in c_:
        if c not in categoriesFinal:
            categoriesFinal.append(c)

    allCategoriesInCorrectOrder = ['Баскетбольные кроссовки', 'Футбольные бутсы', 'Другие кроссовки для спорта',
                                   'Зимние кроссовки', 'Кеды', 'Лоферы', 'Мокасины и топсайдеры', 'Слипоны',
                                   'Эспадрильи', 'Сандалии и босоножки', 'Пляжные сандалии', 'Шлёпки и тапки',
                                   'Мюли и сабо', 'Дерби', 'Оксфорды', 'Броги', 'Монки', 'Все туфли',
                                   'Туфли на высоком каблуке', 'Туфли на среднем каблуке', 'Туфли на низком каблуке',
                                   'Туфли на танкетке', 'Мужские туфли', 'Ботинки на толстой подошве',
                                   'Высокие ботинки и ботфорты', 'Средние ботинки', 'Короткие ботинки и ботильоны',
                                   'Челси', 'Мартинсы', 'Тимберленды', 'Дезерты', 'Казаки', 'Все ботинки', 'Вся обувь',
                                   'Высокие кроссовки', 'Низкие кроссовки', 'Все кроссовки', 'Футболки', 'Лонгсливы',
                                   'Худи с капюшоном', 'Толстовки на молнии', 'Свитшоты', 'Все худи и толстовки',
                                   'Свитеры', 'Кардиганы', 'Водолазки', 'Все свитеры и трикотаж', 'Жилеты', 'Шорты',
                                   'Треники', 'Баскетбольные джерси', 'Баскетбольные шорты', 'Футбольные майки',
                                   'Футбольные шорты', 'Спортивные майки', 'Спортивные шорты', 'Спортивные топы',
                                   'Спортивные костюмы', 'Легинсы и термобелье', 'Топы', 'Майки', 'Поло', 'Джинсы',
                                   'Юбки', 'Платья', 'Рубашки', 'Брюки', 'Пиджаки', 'Костюмы', 'Деним',
                                   'Вся спортивная одежда', 'Комбинезоны и боди', 'Зимние штаны', 'Кожаные куртки',
                                   'Джинсовые куртки', 'Бейсбольные куртки', 'Жилетки', 'Ветровки', 'Плащи', 'Пальто',
                                   'Пуховики', 'Шубы', 'Лыжные костюмы', 'Куртки', 'Вся верхняя одежда',
                                   'Мужские плавки', 'Женские купальники', 'Сплошные купальники', 'Домашняя одежда',
                                   'Носки', 'Бюстгальтеры', 'Трусы', 'Все нижнее бельё и домашняя одежда',
                                   'Вся пляжная одежда', 'Вся одежда', 'Сумки тоут', 'Сумки хобо', 'Сумки вёдра',
                                   'Рюкзаки', 'Портфели', 'Клатчи', 'Кошельки', 'Кардхолдеры', 'Сумки через плечо',
                                   'Сумки на плечо', 'Сумки на грудь', 'Сумки на пояс', 'Сумки с ручками',
                                   'Обложки на паспорт', 'Косметички', 'Спортивные сумки', 'Чемоданы и дорожные сумки',
                                   'Аксессуары для сумок', 'Все сумки', 'Ремни', 'Шарфы', 'Перчатки', 'Кепки', 'Шапки',
                                   'Панамы', 'Шляпы', 'Береты', 'Все головные уборы', 'Баскетбольные мячи',
                                   'Футбольные мячи', 'Волейбольные мячи', 'Спортивные перчатки',
                                   'Спортивная экипировка', 'Другие спортивные товары', 'Все спортивные товары',
                                   'Цепочки', 'Браслеты', 'Кольца', 'Серьги', 'Кулоны', 'Брошь', 'Другие украшения',
                                   'Все украшения', 'Bearbricks и другие коллекционные предметы', 'Солнцезащитные очки',
                                   'Оправы для очков', 'Очешники', 'Галстуки', 'Часы', 'Духи', 'Косметика', 'Брелоки',
                                   'Чехлы для телефона', 'Аксессуары для техники', 'Все аксессуары',
                                   'Другие аксессуары']

    categoriesFinal = sorted(categoriesFinal, key=lambda x: allCategoriesInCorrectOrder.index(x))

    # Список категорий имеет произвольный порядок. При формировании названия важно это учитывать и выдать верный порядок, чтобы название было более точным.
    finalProcessedDewuApiData["categories"] = categoriesFinal

    return finalProcessedDewuApiData
