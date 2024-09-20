from constants.process_constants import SIZE_TABLES_DEFAULT_FILTERS, CATEGORY_NAMES, SIZE_TABLES_SHOES_BRANDS


def connectSizeTables(preprocessedData: dict, finalProcessedDewuApiData: dict) -> dict:
    brands = finalProcessedDewuApiData["brands"]
    categories = finalProcessedDewuApiData["categories"]
    genders = finalProcessedDewuApiData["gender"]

    if any(category in ["Перчатки", "Спортивные перчатки"] for category in categories):
        values = {}
        rows_order = []
        for sizeRow in SIZE_TABLES_DEFAULT_FILTERS["Gloves"]["allSizes"]:
            rows_order.append(sizeRow["name"])
            values[sizeRow["name"]] = sizeRow["sizes"]
        table = {
            "rows_order": rows_order,
            "values": values,
            "table_name": "Основная таблица",
            "table_title": f"Перчатки {brands[0]}",
            "table_description": "Обратите внимание, представленная таблица является таблицей по умолчанию. Для разных брендов размеры могут отличаться. Рекомендуем сверять размер конкретно для данного бренда. Вы всегда можете обратиться в службу поддержки, и мы обязательно поможем подобрать вам подходящий размер!"
        }

        finalProcessedDewuApiData["size_tables"]["default_table"] = table

    elif any(category in ["Солнцезащитные очки", "Оправы для очков"] for category in categories):
        values = {}
        rows_order = []
        for sizeRow in SIZE_TABLES_DEFAULT_FILTERS["Glasses"]["allSizes"]:
            rows_order.append(sizeRow["name"])
            values[sizeRow["name"]] = sizeRow["sizes"]
        table = {
            "rows_order": rows_order,
            "values": values,
            "table_name": "Основная таблица",
            "table_title": f"Очки {brands[0]}",
            "table_description": "Обратите внимание, представленная таблица является таблицей по умолчанию. Для разных брендов размеры могут отличаться. Рекомендуем сверять размер конкретно для данного бренда. Вы всегда можете обратиться в службу поддержки, и мы обязательно поможем подобрать вам подходящий размер!"
        }

        finalProcessedDewuApiData["size_tables"]["default_table"] = table

    elif any("Головные уборы" in CATEGORY_NAMES[category]["path"] for category in categories):
        values = {}
        rows_order = []
        for sizeRow in SIZE_TABLES_DEFAULT_FILTERS["Hats"]["allSizes"]:
            rows_order.append(sizeRow["name"])
            values[sizeRow["name"]] = sizeRow["sizes"]
        table = {
            "rows_order": rows_order,
            "values": values,
            "table_name": "Основная таблица",
            "table_title": f"Головной убор {brands[0]}",
            "table_description": "Обратите внимание, представленная таблица является таблицей по умолчанию. Для разных брендов размеры могут отличаться. Рекомендуем сверять размер конкретно для данного бренда. Вы всегда можете обратиться в службу поддержки, и мы обязательно поможем подобрать вам подходящий размер!"
        }

        finalProcessedDewuApiData["size_tables"]["default_table"] = table

    elif any(category in ["Ремни"] for category in categories):
        values = {}
        rows_order = []
        for sizeRow in SIZE_TABLES_DEFAULT_FILTERS["Belts"]["allSizes"]:
            rows_order.append(sizeRow["name"])
            values[sizeRow["name"]] = sizeRow["sizes"]
        table = {
            "rows_order": rows_order,
            "values": values,
            "table_name": "Основная таблица",
            "table_title": f"Ремень {brands[0]}",
            "table_description": "Обратите внимание, представленная таблица является таблицей по умолчанию. Для разных брендов размеры могут отличаться. Рекомендуем сверять размер конкретно для данного бренда. Вы всегда можете обратиться в службу поддержки, и мы обязательно поможем подобрать вам подходящий размер!"
        }

        finalProcessedDewuApiData["size_tables"]["default_table"] = table

    elif any("Одежда" in CATEGORY_NAMES[category]["path"] for category in categories) and "K" in genders:
        values = {}
        rows_order = []
        for sizeRow in SIZE_TABLES_DEFAULT_FILTERS["Clothes_Kids"]["allSizes"]:
            rows_order.append(sizeRow["name"])
            values[sizeRow["name"]] = sizeRow["sizes"]
        table = {
            "rows_order": rows_order,
            "values": values,
            "table_name": "Основная таблица",
            "table_title": f"Детская одежда {brands[0]}",
            "table_description": "Обратите внимание, представленная таблица является таблицей по умолчанию. Для разных брендов размеры могут отличаться. Рекомендуем сверять размер конкретно для данного бренда. Вы всегда можете обратиться в службу поддержки, и мы обязательно поможем подобрать вам подходящий размер!"
        }

        finalProcessedDewuApiData["size_tables"]["default_table"] = table

    elif any("Одежда" in CATEGORY_NAMES[category]["path"] for category in categories) and "F" in genders:
        values = {}
        rows_order = []
        for sizeRow in SIZE_TABLES_DEFAULT_FILTERS["Clothes_Women"]["allSizes"]:
            rows_order.append(sizeRow["name"])
            values[sizeRow["name"]] = sizeRow["sizes"]
        table = {
            "rows_order": rows_order,
            "values": values,
            "table_name": "Основная таблица",
            "table_title": f"Женская одежда {brands[0]}",
            "table_description": "Обратите внимание, представленная таблица является таблицей по умолчанию. Для разных брендов размеры могут отличаться. Рекомендуем сверять размер конкретно для данного бренда. Вы всегда можете обратиться в службу поддержки, и мы обязательно поможем подобрать вам подходящий размер!"
        }

        finalProcessedDewuApiData["size_tables"]["default_table"] = table

    elif any("Одежда" in CATEGORY_NAMES[category]["path"] for category in categories) and "M" in genders:
        values = {}
        rows_order = []
        for sizeRow in SIZE_TABLES_DEFAULT_FILTERS["Clothes_Men"]["allSizes"]:
            rows_order.append(sizeRow["name"])
            values[sizeRow["name"]] = sizeRow["sizes"]
        table = {
            "rows_order": rows_order,
            "values": values,
            "table_name": "Основная таблица",
            "table_title": f"Мужская одежда {brands[0]}",
            "table_description": "Обратите внимание, представленная таблица является таблицей по умолчанию. Для разных брендов размеры могут отличаться. Рекомендуем сверять размер конкретно для данного бренда. Вы всегда можете обратиться в службу поддержки, и мы обязательно поможем подобрать вам подходящий размер!"
        }

        finalProcessedDewuApiData["size_tables"]["default_table"] = table

    elif any("Обувь" in CATEGORY_NAMES[category]["path"] for category in categories) and any(
            brand in SIZE_TABLES_SHOES_BRANDS for brand in brands):
        brand_ = ""
        for brand in brands:
            if brand in SIZE_TABLES_SHOES_BRANDS:
                brand_ = brand
                break

        if "M" == genders[0]:
            values = {}
            rows_order = []
            for sizeRow in SIZE_TABLES_SHOES_BRANDS[brand_]["Men"]["allSizes"]:
                rows_order.append(sizeRow["name"])
                values[sizeRow["name"]] = sizeRow["sizes"]
            table = {
                "rows_order": rows_order,
                "values": values,
                "table_name": f"Таблица {brand_}",
                "table_title": f"Мужская обувь {brand_}",
                "table_description": f"Обратите внимание, таблица представлена брендом {brand_}, для других брендов рекомендуем пользоваться своей размерной сеткой и быть бдительным при сравнении размеров разных брендов. Вы всегда можете обратиться в службу поддержки, и мы обязательно поможем подобрать вам подходящий размер!"
            }

            finalProcessedDewuApiData["size_tables"]["main_regular_table"] = table

        elif "F" == genders[0]:
            values = {}
            rows_order = []
            for sizeRow in SIZE_TABLES_SHOES_BRANDS[brand_]["Women"]["allSizes"]:
                rows_order.append(sizeRow["name"])
                values[sizeRow["name"]] = sizeRow["sizes"]
            table = {
                "rows_order": rows_order,
                "values": values,
                "table_name": f"Таблица {brand_}",
                "table_title": f"Женская обувь {brand_}",
                "table_description": f"Обратите внимание, таблица представлена брендом {brand_}, для других брендов рекомендуем пользоваться своей размерной сеткой и быть бдительным при сравнении размеров разных брендов. Вы всегда можете обратиться в службу поддержки, и мы обязательно поможем подобрать вам подходящий размер!"
            }

            finalProcessedDewuApiData["size_tables"]["main_regular_table"] = table

        elif "K" == genders[0]:
            values = {}
            rows_order = []
            for sizeRow in SIZE_TABLES_SHOES_BRANDS[brand_]["Kids"]["allSizes"]:
                rows_order.append(sizeRow["name"])
                values[sizeRow["name"]] = sizeRow["sizes"]
            table = {
                "rows_order": rows_order,
                "values": values,
                "table_name": f"Таблица {brand_}",
                "table_title": f"Детская обувь {brand_}",
                "table_description": f"Обратите внимание, таблица представлена брендом {brand_}, для других брендов рекомендуем пользоваться своей размерной сеткой и быть бдительным при сравнении размеров разных брендов. Вы всегда можете обратиться в службу поддержки, и мы обязательно поможем подобрать вам подходящий размер!"
            }

            finalProcessedDewuApiData["size_tables"]["main_regular_table"] = table

    elif any("Обувь" in CATEGORY_NAMES[category]["path"] for category in categories) and genders[0] in ["M", "F"]:
        values = {}
        rows_order = []
        for sizeRow in SIZE_TABLES_DEFAULT_FILTERS["Shoes_Adults"]["allSizes"]:
            rows_order.append(sizeRow["name"])
            values[sizeRow["name"]] = sizeRow["sizes"]
        table = {
            "rows_order": rows_order,
            "values": values,
            "table_name": "Основная таблица",
            "table_title": f"Обувь {brands[0]}",
            "table_description": "Обратите внимание, представленная таблица является таблицей по умолчанию. Для разных брендов размеры могут отличаться. Рекомендуем сверять размер конкретно для данного бренда. Вы всегда можете обратиться в службу поддержки, и мы обязательно поможем подобрать вам подходящий размер!"
        }

        finalProcessedDewuApiData["size_tables"]["default_table"] = table

    elif any("Обувь" in CATEGORY_NAMES[category]["path"] for category in categories) and genders[0] == "K":
        values = {}
        rows_order = []
        for sizeRow in SIZE_TABLES_DEFAULT_FILTERS["Shoes_Kids"]["allSizes"]:
            rows_order.append(sizeRow["name"])
            values[sizeRow["name"]] = sizeRow["sizes"]
        table = {
            "rows_order": rows_order,
            "values": values,
            "table_name": "Основная таблица",
            "table_title": f"Детская обувь {brands[0]}",
            "table_description": "Обратите внимание, представленная таблица является таблицей по умолчанию. Для разных брендов размеры могут отличаться. Рекомендуем сверять размер конкретно для данного бренда. Вы всегда можете обратиться в службу поддержки, и мы обязательно поможем подобрать вам подходящий размер!"
        }

        finalProcessedDewuApiData["size_tables"]["default_table"] = table

    return finalProcessedDewuApiData
