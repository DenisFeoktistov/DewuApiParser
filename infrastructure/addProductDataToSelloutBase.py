import copy
import re

import pydash as _

from constants.process_constants import CATEGORIES_WEIGHTS, CATEGORY_NAMES, SIZE_TABLES_DEFAULT_FILTERS

# Функция либо дополняет данные уже существующего в нашей базе товара (sameProductFromSelloutBase не пустой), либо создает новый на основе данных productInfoToAdd от платформы platformOfAddingProduct

# Ниже я привел пример того, как выглядит конечная структура данных товара для передачи на backend.
finalProductInfoFormat = {
    "brands": [
        "Nike",
        "AMBUSH"
    ],
    "is_collab": True,
    "collab_names": [
        "Nike x Ambush"
    ],
    "lines": [
        [
            "Nike",
            "Nike Dunk",
            "Nike Dunk High"
        ]
    ],
    "categories": [
        "Высокие кроссовки",
        "Все кроссовки"
    ],
    "brandName": "Nike x Ambush",
    "model": "Dunk High",
    "colorway": "Deep royal",
    "gender": [
        "M",
        "F"
    ],
    "baseGenders": [
        "M",
        "F"
    ],
    "extraGenders": [],
    "custom": False,
    "manufacturer_sku": "CU7544-400",
    "other_manufacturer_skus": [],
    "date": "18.05.2021",
    "approximate_date": "18.05.2021",
    "retailPrice": {
        "currency": "CNY",
        "price": 1299
    },
    "description": {
        "language": "ENG",
        "description": ""
    },
    "images": [
        {
            "imageId": 0,
            "unitsIds": [
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                13,
                14,
                15,
                16,
                17,
                18,
                19,
                20,
                21,
                22,
                23,
                24,
                25,
                26,
                27,
                28,
                29,
                30,
                31,
                32,
                33,
                34,
                35,
                36,
                37,
                38
            ],
            "url": "https://cdn.poizon.com/pro-img/origin-img/20230721/dc21d6128aab4f1e93bc883a3725a313.jpg"
        },
        {
            "imageId": 0,
            "unitsIds": [
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                13,
                14,
                15,
                16,
                17,
                18,
                19,
                20,
                21,
                22,
                23,
                24,
                25,
                26,
                27,
                28,
                29,
                30,
                31,
                32,
                33,
                34,
                35,
                36,
                37,
                38
            ],
            "url": "https://cdn.poizon.com/pro-img/origin-img/20230721/d0eff04089d24d33a3cd790cddaba2c2.jpg"
        },
        {
            "imageId": 0,
            "unitsIds": [
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                13,
                14,
                15,
                16,
                17,
                18,
                19,
                20,
                21,
                22,
                23,
                24,
                25,
                26,
                27,
                28,
                29,
                30,
                31,
                32,
                33,
                34,
                35,
                36,
                37,
                38
            ],
            "url": "https://cdn.poizon.com/pro-img/origin-img/20230721/02c9f790694f410bb7514e9aa7172aac.jpg"
        },
        {
            "imageId": 0,
            "unitsIds": [
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                13,
                14,
                15,
                16,
                17,
                18,
                19,
                20,
                21,
                22,
                23,
                24,
                25,
                26,
                27,
                28,
                29,
                30,
                31,
                32,
                33,
                34,
                35,
                36,
                37,
                38
            ],
            "url": "https://cdn.poizon.com/pro-img/origin-img/20230721/00e9ea928a8e43e0bea3ab147d435be2.jpg"
        },
        {
            "imageId": 0,
            "unitsIds": [
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                13,
                14,
                15,
                16,
                17,
                18,
                19,
                20,
                21,
                22,
                23,
                24,
                25,
                26,
                27,
                28,
                29,
                30,
                31,
                32,
                33,
                34,
                35,
                36,
                37,
                38
            ],
            "url": "https://cdn.poizon.com/pro-img/origin-img/20230721/3322602a30f44cc1b1dad7c853271882.jpg"
        },
        {
            "imageId": 0,
            "unitsIds": [
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                13,
                14,
                15,
                16,
                17,
                18,
                19,
                20,
                21,
                22,
                23,
                24,
                25,
                26,
                27,
                28,
                29,
                30,
                31,
                32,
                33,
                34,
                35,
                36,
                37,
                38
            ],
            "url": "https://cdn.poizon.com/pro-img/origin-img/20230721/b76a3de9185a46598db29f68ff27ce11.jpg"
        },
        {
            "imageId": 0,
            "unitsIds": [
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                13,
                14,
                15,
                16,
                17,
                18,
                19,
                20,
                21,
                22,
                23,
                24,
                25,
                26,
                27,
                28,
                29,
                30,
                31,
                32,
                33,
                34,
                35,
                36,
                37,
                38
            ],
            "url": "https://cdn.poizon.com/pro-img/origin-img/20230721/c6925611501240de9f0c0316c13ca1d3.jpg"
        },
        {
            "imageId": 0,
            "unitsIds": [
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                13,
                14,
                15,
                16,
                17,
                18,
                19,
                20,
                21,
                22,
                23,
                24,
                25,
                26,
                27,
                28,
                29,
                30,
                31,
                32,
                33,
                34,
                35,
                36,
                37,
                38
            ],
            "url": "https://cdn.poizon.com/pro-img/origin-img/20230721/769c63715baf46bbb156e6fdf68751ad.jpg"
        }
    ],
    "size_tables": {  # Может быть несколько таблиц, везде формат одинаковый
        "main_regular_table": {
            "rows_order": [
                "EU",
                "RU",
                "US",
                "UK",
                "CM/JP",
                "US-Kids",
                "US-Women's"
            ],
            "values": {
                "EU": [
                    "35.5",
                    "36",
                    "36.5",
                    "37.5",
                    "38",
                    "38.5",
                    "39",
                    "40",
                    "40.5",
                    "41",
                    "42",
                    "42.5",
                    "43",
                    "44",
                    "44.5",
                    "45",
                    "45.5",
                    "46",
                    "47",
                    "47.5",
                    "48",
                    "48.5",
                    "49",
                    "49.5",
                    "50",
                    "50.5",
                    "51",
                    "51.5",
                    "52",
                    "52.5",
                    "53",
                    "53.5",
                    "54",
                    "54.5",
                    "55",
                    "55.5",
                    "56",
                    "56.5"
                ],
                "RU": [
                    "34.5",
                    "35",
                    "35.5",
                    "36.5",
                    "37",
                    "37.5",
                    "38",
                    "39",
                    "39.5",
                    "40",
                    "41",
                    "41.5",
                    "42",
                    "43",
                    "43.5",
                    "44",
                    "44.5",
                    "45",
                    "46",
                    "46.5",
                    "47",
                    "47.5",
                    "48",
                    "48.5",
                    "49",
                    "49.5",
                    "50",
                    "50.5",
                    "51",
                    "51.5",
                    "52",
                    "52.5",
                    "53",
                    "53.5",
                    "54",
                    "54.5",
                    "55",
                    "55.5"
                ],
                "US": [
                    "3.5",
                    "4",
                    "4.5",
                    "5",
                    "5.5",
                    "6",
                    "6.5",
                    "7",
                    "7.5",
                    "8",
                    "8.5",
                    "9",
                    "9.5",
                    "10",
                    "10.5",
                    "11",
                    "11.5",
                    "12",
                    "12.5",
                    "13",
                    "13.5",
                    "14",
                    "14.5",
                    "15",
                    "15.5",
                    "16",
                    "16.5",
                    "17",
                    "17.5",
                    "18",
                    "18.5",
                    "19",
                    "19.5",
                    "20",
                    "20.5",
                    "21",
                    "21.5",
                    "22"
                ],
                "UK": [
                    "3",
                    "3.5",
                    "4",
                    "4.5",
                    "5",
                    "5.5",
                    "6",
                    "6",
                    "6.5",
                    "7",
                    "7.5",
                    "8",
                    "8.5",
                    "9",
                    "9.5",
                    "10",
                    "10.5",
                    "11",
                    "11.5",
                    "12",
                    "12.5",
                    "13",
                    "13.5",
                    "14",
                    "14.5",
                    "15",
                    "15.5",
                    "16",
                    "16.5",
                    "17",
                    "17.5",
                    "18",
                    "18.5",
                    "19",
                    "19.5",
                    "20",
                    "20.5",
                    "21"
                ],
                "CM/JP": [
                    "22.5",
                    "23",
                    "23.5",
                    "23.5",
                    "24",
                    "24",
                    "24.5",
                    "25",
                    "25.5",
                    "26",
                    "26.5",
                    "27",
                    "27.5",
                    "28",
                    "28.5",
                    "29",
                    "29.5",
                    "30",
                    "30.5",
                    "31",
                    "31.5",
                    "32",
                    "32.5",
                    "33",
                    "33.5",
                    "34",
                    "34.5",
                    "35",
                    "35.5",
                    "36",
                    "36.5",
                    "37",
                    "37.5",
                    "38",
                    "38.5",
                    "39",
                    "39.5",
                    "40"
                ],
                "US-Kids": [
                    "3.5Y",
                    "4Y",
                    "4.5Y",
                    "5Y",
                    "5.5Y",
                    "6Y",
                    "6.5Y",
                    "7Y",
                    "7.5Y",
                    "8Y",
                    "8.5Y",
                    "9Y",
                    "9.5Y",
                    "10Y",
                    "10.5Y",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    ""
                ],
                "US-Women's": [
                    "5",
                    "5.5",
                    "6",
                    "6.5",
                    "7",
                    "7.5",
                    "8",
                    "8.5",
                    "9",
                    "9.5",
                    "10",
                    "10.5",
                    "11",
                    "11.5",
                    "12",
                    "12.5",
                    "13",
                    "13.5",
                    "14",
                    "14.5",
                    "15",
                    "15.5",
                    "16",
                    "16.5",
                    "17",
                    "17.5",
                    "18",
                    "18.5",
                    "19",
                    "19.5",
                    "20",
                    "20.5",
                    "21",
                    "21.5",
                    "22",
                    "22.5",
                    "23",
                    "23.5"
                ]
            },
            "table_name": "Таблица Nike",
            "table_title": "Мужская обувь Nike",
            "table_description": "Обратите внимание, таблица представлена брендом Nike, для других брендов рекомендуем пользоваться своей размерной сеткой и быть бдительным при сравнении размеров разных брендов. Вы всегда можете обратиться в службу поддержки, и мы обязательно поможем подобрать вам подходящий размер!"
        },
        "main_measurements_table": {},
        "default_table": {},
        "tables_recommendations": {}
    },
    "parameters_to_show_in_product": {
        "parameters": {
            "Основные цвета": "Royal Blue, Синий",
            "Цена на ритейле": "16900₽"
        },
        "parameters_order": [
            "Основные цвета",
            "Материал верха",
            "Материалы",
            "Цена на ритейле",
            "Дизайнер",
            "Технология подошвы",
            "Дополнительные цвета",
            "Текстура",
            "Размер баскетбольного мяча",
            "Размер футбольного мяча",
            "Размер мяча",
            "Материал подошвы",
            "Содержание материалов",
            "Наполнение",
            "Содержание пуха",
            "Содержание кашемира",
            "Содержание шерсти",
            "Высота товара",
            "Упаковка",
            "Длина ремешка",
            "Высота ручки",
            "Переносица",
            "Ширина оправы",
            "Ширина линз",
            "Высота линз",
            "Высота оправы",
            "Размер линз",
            "Длина дужки",
            "Длина галстука",
            "Размер",
            "Вес",
            "Вес",
            "Объём",
            "Применение мяча"
        ]
    },
    "parameters_to_use_in_filters": {
        "colors": [
            "blue"
        ],
        "material": [],
        "upper_height": [
            "high"
        ],
        "heel_type": [],
        "boots_height": [],
        "length": [],
        "sleeve_length": [],
        "collar_type": [],
        "closure_type": []
    },
    "hasConfigurationsWithDifferentImages": True,
    "minPrice": {
        "currency": "CNY",
        "price": 915.0
    },
    "units": [
        {
            "view_name": "35.5 EU",
            "unitId": 1,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Adults",
                "table_row_name": "Европейский(EU)",
                "sizes": [
                    "35.5"
                ]
            },
            "offers": [],
            "weight": 1.8,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "36 EU",
            "unitId": 2,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Adults",
                "table_row_name": "Европейский(EU)",
                "sizes": [
                    "36"
                ]
            },
            "offers": [],
            "weight": 1.8,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "36.5 EU",
            "unitId": 3,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Adults",
                "table_row_name": "Европейский(EU)",
                "sizes": [
                    "36.5"
                ]
            },
            "offers": [],
            "weight": 1.8,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "37.5 EU",
            "unitId": 4,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Adults",
                "table_row_name": "Европейский(EU)",
                "sizes": [
                    "37.5"
                ]
            },
            "offers": [],
            "weight": 1.8,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "38 EU",
            "unitId": 5,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Adults",
                "table_row_name": "Европейский(EU)",
                "sizes": [
                    "38"
                ]
            },
            "offers": [],
            "weight": 1.8,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "38.5 EU",
            "unitId": 6,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Adults",
                "table_row_name": "Европейский(EU)",
                "sizes": [
                    "38.5"
                ]
            },
            "offers": [],
            "weight": 1.8,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "39 EU",
            "unitId": 7,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Adults",
                "table_row_name": "Европейский(EU)",
                "sizes": [
                    "39",
                    "39.5"
                ]
            },
            "offers": [],
            "weight": 1.8,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "40 EU",
            "unitId": 8,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Adults",
                "table_row_name": "Европейский(EU)",
                "sizes": [
                    "40",
                    "39.5"
                ]
            },
            "offers": [],
            "weight": 1.8,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "40.5 EU",
            "unitId": 9,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Adults",
                "table_row_name": "Европейский(EU)",
                "sizes": [
                    "40.5"
                ]
            },
            "offers": [],
            "weight": 1.8,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "41 EU",
            "unitId": 10,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Adults",
                "table_row_name": "Европейский(EU)",
                "sizes": [
                    "41",
                    "41.5"
                ]
            },
            "offers": [],
            "weight": 1.8,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "42 EU",
            "unitId": 11,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Adults",
                "table_row_name": "Европейский(EU)",
                "sizes": [
                    "42",
                    "41.5"
                ]
            },
            "offers": [],
            "weight": 1.8,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "42.5 EU",
            "unitId": 12,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Adults",
                "table_row_name": "Европейский(EU)",
                "sizes": [
                    "42.5"
                ]
            },
            "offers": [],
            "weight": 1.8,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "43 EU",
            "unitId": 13,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Adults",
                "table_row_name": "Европейский(EU)",
                "sizes": [
                    "43",
                    "43.5"
                ]
            },
            "offers": [],
            "weight": 1.8,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "44 EU",
            "unitId": 14,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Adults",
                "table_row_name": "Европейский(EU)",
                "sizes": [
                    "44",
                    "43.5"
                ]
            },
            "offers": [],
            "weight": 1.8,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "44.5 EU",
            "unitId": 15,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Adults",
                "table_row_name": "Европейский(EU)",
                "sizes": [
                    "44.5"
                ]
            },
            "offers": [],
            "weight": 1.8,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "45 EU",
            "unitId": 16,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Adults",
                "table_row_name": "Европейский(EU)",
                "sizes": [
                    "45"
                ]
            },
            "offers": [],
            "weight": 1.8,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "45.5 EU",
            "unitId": 17,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Adults",
                "table_row_name": "Европейский(EU)",
                "sizes": [
                    "45.5"
                ]
            },
            "offers": [],
            "weight": 1.8,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "46 EU",
            "unitId": 18,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Adults",
                "table_row_name": "Европейский(EU)",
                "sizes": [
                    "46",
                    "46.5"
                ]
            },
            "offers": [],
            "weight": 1.8,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "47 EU",
            "unitId": 19,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Adults",
                "table_row_name": "Европейский(EU)",
                "sizes": [
                    "47",
                    "46.5"
                ]
            },
            "offers": [],
            "weight": 1.8,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "47.5 EU",
            "unitId": 20,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Adults",
                "table_row_name": "Европейский(EU)",
                "sizes": [
                    "47.5"
                ]
            },
            "offers": [],
            "weight": 1.8,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "48 EU",
            "unitId": 21,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Adults",
                "table_row_name": "Европейский(EU)",
                "sizes": [
                    "48"
                ]
            },
            "offers": [],
            "weight": 1.8,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "48.5 EU",
            "unitId": 22,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Adults",
                "table_row_name": "Европейский(EU)",
                "sizes": [
                    "48.5"
                ]
            },
            "offers": [],
            "weight": 1.8,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "49 EU",
            "unitId": 23,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Adults",
                "table_row_name": "Европейский(EU)",
                "sizes": [
                    "49"
                ]
            },
            "offers": [],
            "weight": 1.8,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "49.5 EU",
            "unitId": 24,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Adults",
                "table_row_name": "Европейский(EU)",
                "sizes": [
                    "49.5"
                ]
            },
            "offers": [],
            "weight": 1.8,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "50 EU",
            "unitId": 25,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Adults",
                "table_row_name": "Европейский(EU)",
                "sizes": [
                    "50"
                ]
            },
            "offers": [],
            "weight": 1.8,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "50.5 EU",
            "unitId": 26,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Adults",
                "table_row_name": "Европейский(EU)",
                "sizes": [
                    "50.5"
                ]
            },
            "offers": [],
            "weight": 1.8,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "51 EU",
            "unitId": 27,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Adults",
                "table_row_name": "Европейский(EU)",
                "sizes": [
                    "51"
                ]
            },
            "offers": [],
            "weight": 1.8,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "51.5 EU",
            "unitId": 28,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Adults",
                "table_row_name": "Европейский(EU)",
                "sizes": [
                    "51.5"
                ]
            },
            "offers": [],
            "weight": 1.8,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "52 EU",
            "unitId": 29,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Adults",
                "table_row_name": "Европейский(EU)",
                "sizes": [
                    "52"
                ]
            },
            "offers": [],
            "weight": 1.8,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "52.5 EU",
            "unitId": 30,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Adults",
                "table_row_name": "Европейский(EU)",
                "sizes": [
                    "52.5"
                ]
            },
            "offers": [],
            "weight": 1.8,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "53 EU",
            "unitId": 31,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Adults",
                "table_row_name": "Европейский(EU)",
                "sizes": [
                    "53"
                ]
            },
            "offers": [],
            "weight": 1.8,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "53.5 EU",
            "unitId": 32,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "",
                "table_row_name": "",
                "sizes": []
            },
            "offers": [],
            "weight": 1.8,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "54 EU",
            "unitId": 33,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "",
                "table_row_name": "",
                "sizes": []
            },
            "offers": [],
            "weight": 1.8,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "54.5 EU",
            "unitId": 34,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "",
                "table_row_name": "",
                "sizes": []
            },
            "offers": [],
            "weight": 1.8,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "55 EU",
            "unitId": 35,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "",
                "table_row_name": "",
                "sizes": []
            },
            "offers": [],
            "weight": 1.8,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "55.5 EU",
            "unitId": 36,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "",
                "table_row_name": "",
                "sizes": []
            },
            "offers": [],
            "weight": 1.8,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "56 EU",
            "unitId": 37,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "",
                "table_row_name": "",
                "sizes": []
            },
            "offers": [],
            "weight": 1.8,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "56.5 EU",
            "unitId": 38,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "",
                "table_row_name": "",
                "sizes": []
            },
            "offers": [],
            "weight": 1.8,
            "height": 0,
            "width": 0,
            "length": 0
        }
    ],
    "platformsInfo": {
        # Здесь будет храниться вся информация с платформ в 2-ух видах: до обработки (то, как она приходит с платформы), после нашей обработки. Я указал там только несколько полей: те, которые самые важные - для связывания с платформой и посылания запроса на обновление данных с нее.
        "goat": {
            "preprocessedData": {},
            "processedData": {
                "slug": "tazz-slipper-kids-sand-1143776k-san",
                "id": 1341930
            }
        },
        "poizonNotFullApi": {
            "preprocessedData": {},
            "processedData": {
                "likesCount": 242645,
                "spuId": 1498978
            }
        },
        "poizonWebParser": {
            "preprocessedData": {
                "apiData": {},
                "webData": {}
            },
            "processedData": {
                "apiData": {},
                "webData": {}
            }
        },
        "poizonHK": {
            "preprocessedData": {
                "apiData": {},
                "webData": {}
            },
            "processedData": {
                "apiData": {},
                "webData": {}
            }
        }
    }
}


# Из того, что я вижу в сравнении с прежним форматом данных, изменилось (пропало). Добавились: гендеры, retailPrice, minPrice, hasConfigurationsWithDifferentImages. Формат изменился: images, parameters_to_show_in_product.parameters, description, size_tables, units. Нет полей: size_row_name, formatted_manufacturer_sku, many_sizes, many_colors, many_configurations, extra_name, relevance_number, novelty_number.

# Можно разбить на 3 кейса: 1. Товара еще нет в нашей базе (индикатор - sameProductFromSelloutBase == {}) 2. У товара только и есть одна текущая платформа в привязанных и, получается, все данные от нее. 3. Есть несколько связанных платформ
# Эта функция вызывается после нахождения на платформе нового товара (из функции findProductInSelloutBase) или при обновлении товара из нашей базы (то есть последовательно при получении обновленных данных с каждой связанной с товаром платформы).
def addProductDataToSelloutBase(platformOfAddingProduct: str, productInfoToAdd: dict,
                                preprocessedProductInfoToAdd: dict, sameProductFromSelloutBase: dict):
    # 2 случая в одном: товара нет на платформе; товар есть на платформе, но единственная связанная платформа == текущей.
    # Это значит, что мы добавляем новый товар в нашу базу, поэтому создаем все с нуля и заполняем все данные данными с платформы.
    # Случай, когда товар уже есть в нашей базе, но у него из связанных платформ только та, данные с которой мы сейчас пытаемся добавить. То есть по сути мы можем ничего не пытаться заменить, а просто перезаписать все данные новыми данными
    if not sameProductFromSelloutBase or _.get(sameProductFromSelloutBase, "platformsInfo", {}).keys() == [
        platformOfAddingProduct]:
        finalProductInfo = {
            "brands": productInfoToAdd["brands"],
            "is_collab": productInfoToAdd["is_collab"],
            "collab_names": productInfoToAdd["collab_names"],
            "lines": productInfoToAdd["lines"],
            "categories": productInfoToAdd["categories"],
            "brandName": productInfoToAdd["brandName"],
            "model": productInfoToAdd["model"],
            "colorway": productInfoToAdd["colorway"],
            "gender": productInfoToAdd["gender"],
            "baseGenders": productInfoToAdd["baseGenders"],
            "extraGenders": productInfoToAdd["extraGenders"],
            "custom": productInfoToAdd["custom"],
            "manufacturer_sku": productInfoToAdd["manufacturer_sku"],
            "other_manufacturer_skus": _.get(productInfoToAdd, "other_manufacturer_skus", []),
            "date": productInfoToAdd["date"],
            "approximate_date": productInfoToAdd["approximate_date"],
            "retailPrice": {
                "currency": _.get(productInfoToAdd, "retailPrice.currency", ""),
                "price": _.get(productInfoToAdd, "retailPrice.price", 0)
            },
            "description": {
                "language": _.get(productInfoToAdd, "description.language", ""),
                "description": _.get(productInfoToAdd, "description.description", "")
            },
            "images": productInfoToAdd["images"],
            "size_tables": productInfoToAdd["size_tables"],
            "parameters_to_show_in_product": {
                "parameters": productInfoToAdd["parameters_to_show_in_product"]["parameters"],
                "parameters_order": [
                    "Основные цвета",
                    "Материал верха",
                    "Материалы",
                    "Цена на ритейле",
                    "Дизайнер",
                    "Технология подошвы",
                    "Дополнительные цвета",
                    "Текстура",
                    "Размер баскетбольного мяча",
                    "Размер футбольного мяча",
                    "Размер мяча",
                    "Материал подошвы",
                    "Содержание материалов",
                    "Наполнение",
                    "Содержание пуха",
                    "Содержание кашемира",
                    "Содержание шерсти",
                    "Высота товара",
                    "Упаковка",
                    "Длина ремешка",
                    "Высота ручки",
                    "Переносица",
                    "Ширина оправы",
                    "Ширина линз",
                    "Высота линз",
                    "Высота оправы",
                    "Размер линз",
                    "Длина дужки",
                    "Длина галстука",
                    "Размер",
                    "Вес",
                    "Вес",
                    "Объём",
                    "Применение мяча"
                ]
            },
            "parameters_to_use_in_filters": {
                "colors": _.get(productInfoToAdd, "parameters_to_use_in_filters.colors", []),
                "material": _.get(productInfoToAdd, "parameters_to_use_in_filters.material", []),
                "upper_height": _.get(productInfoToAdd, "parameters_to_use_in_filters.upper_height", []),
                "heel_type": _.get(productInfoToAdd, "parameters_to_use_in_filters.heel_type", []),
                "boots_height": _.get(productInfoToAdd, "parameters_to_use_in_filters.boots_height", []),
                "length": _.get(productInfoToAdd, "parameters_to_use_in_filters.length", []),
                "sleeve_length": _.get(productInfoToAdd, "parameters_to_use_in_filters.sleeve_length", []),
                "collar_type": _.get(productInfoToAdd, "parameters_to_use_in_filters.collar_type", []),
                "closure_type": _.get(productInfoToAdd, "parameters_to_use_in_filters.closure_type", [])
            },
            "hasConfigurationsWithDifferentImages": _.get(productInfoToAdd, "hasConfigurationsWithDifferentImages",
                                                          False),
            "minPrice": {
                "currency": _.get(productInfoToAdd, "minPrice.currency", ""),
                "price": _.get(productInfoToAdd, "minPrice.price", 0)
            },
            "units": productInfoToAdd["units"],
            "platformsInfo": {
                platformOfAddingProduct: {
                    "preprocessedData": preprocessedProductInfoToAdd,
                    "processedData": productInfoToAdd
                }
            }
        }
        return finalProductInfo

    # Отдельный кейс, когда товар hasConfigurationsWithDifferentImages, а добавляемая платформа != poizonNotFullApi: так как мы пока не можем адекватно связать такие товары, то мы передадим на повторное добавление данных с этой платформы, но уже
    if platformOfAddingProduct == "goat" and (sameProductFromSelloutBase["hasConfigurationsWithDifferentImages"] or set(
            sameProductFromSelloutBase["platformsInfo"].keys()) == {"poizonHK"}):
        addProductDataToSelloutBase(platformOfAddingProduct, productInfoToAdd, preprocessedProductInfoToAdd, {})
        return

    if platformOfAddingProduct == "poizonNotFullApi" and set(sameProductFromSelloutBase["platformsInfo"].keys()) == {
        "goat"} and productInfoToAdd["hasConfigurationsWithDifferentImages"]:
        addProductDataToSelloutBase(platformOfAddingProduct, productInfoToAdd, preprocessedProductInfoToAdd, {})
        return

    # Случай, если товар уже есть на платформе и с ним связаны также другие платформы (возможно, текущая тоже там есть)
    # На текущий момент мы располагаем 2-мя активными платформами (GOAT, API Dewu неполное) и старыми данными с платформы Poizon

    # region Начинаем с дополняемых полей (списки) и простых заменяемых полей

    # brands
    brands = [brand for brand in productInfoToAdd["brands"] if brand not in sameProductFromSelloutBase["brands"]]
    sameProductFromSelloutBase["brands"] = sameProductFromSelloutBase["brands"].extend(brands)

    # lines
    lines = [line for line in productInfoToAdd["lines"] if line not in sameProductFromSelloutBase["lines"]]
    sameProductFromSelloutBase["lines"] = sameProductFromSelloutBase["lines"].extend(lines)

    # categories
    categories = [category for category in productInfoToAdd["categories"] if
                  category not in sameProductFromSelloutBase["categories"]]
    sameProductFromSelloutBase["categories"] = sameProductFromSelloutBase["categories"].extend(categories)

    # collaborations
    if not sameProductFromSelloutBase["is_collab"] and productInfoToAdd["is_collab"]:
        sameProductFromSelloutBase["is_collab"] = True

    collab_names = [collab_name for collab_name in productInfoToAdd["collab_names"] if
                    collab_name not in sameProductFromSelloutBase["collab_names"]]
    sameProductFromSelloutBase["collab_names"] = sameProductFromSelloutBase["collab_names"].extend(collab_names)

    # manufacturer_skus
    allSkusSameProduct = [sameProductFromSelloutBase["manufacturer_sku"]] + sameProductFromSelloutBase[
        "other_manufacturer_skus"]
    allSkusProductToAdd = [productInfoToAdd["manufacturer_sku"]] + productInfoToAdd["other_manufacturer_skus"]
    skusToAdd = [sku for sku in allSkusProductToAdd if sku not in allSkusSameProduct]
    sameProductFromSelloutBase["other_manufacturer_skus"] = sameProductFromSelloutBase[
        "other_manufacturer_skus"].extend(skusToAdd)

    # custom
    if not sameProductFromSelloutBase["custom"] and productInfoToAdd["custom"]:
        sameProductFromSelloutBase["custom"] = True

    # Гендеры
    genders = [gender for gender in productInfoToAdd["gender"] if gender not in sameProductFromSelloutBase["gender"]]
    sameProductFromSelloutBase["gender"] = sameProductFromSelloutBase["gender"].extend(genders)
    baseGenders = [baseGender for baseGender in productInfoToAdd["baseGenders"] if
                   baseGender not in sameProductFromSelloutBase["baseGenders"]]
    sameProductFromSelloutBase["baseGenders"] = sameProductFromSelloutBase["baseGenders"].extend(baseGenders)
    extraGenders = [extraGender for extraGender in productInfoToAdd["extraGenders"] if
                    extraGender not in sameProductFromSelloutBase["extraGenders"]]
    sameProductFromSelloutBase["extraGenders"] = sameProductFromSelloutBase["extraGenders"].extend(extraGenders)

    # Даты
    dateSameProductFromSelloutBase = sameProductFromSelloutBase["approximate_date"]
    dateProductInfoToAdd = productInfoToAdd["approximate_date"]
    if get_precision_level(dateProductInfoToAdd) > get_precision_level(dateSameProductFromSelloutBase):
        sameProductFromSelloutBase["date"] = productInfoToAdd["date"]
        sameProductFromSelloutBase["approximate_date"] = productInfoToAdd["approximate_date"]

    # Ритейл
    if not sameProductFromSelloutBase["retailPrice"]["price"] or (
            sameProductFromSelloutBase["retailPrice"]["currency"] == "CNY" and
            productInfoToAdd["retailPrice"]["currency"] == "USD"):
        sameProductFromSelloutBase["retailPrice"]["price"] = productInfoToAdd["retailPrice"]["currency"]
        sameProductFromSelloutBase["retailPrice"]["price"] = productInfoToAdd["retailPrice"]["price"]

    # Описание
    if (sameProductFromSelloutBase["description"]["language"] != "RU" and
            productInfoToAdd["description"]["language"] == "USA"):
        sameProductFromSelloutBase["description"]["language"] = "USA"
        sameProductFromSelloutBase["description"]["description"] = productInfoToAdd["description"]["description"]

    # Названия
    if platformOfAddingProduct == "goat":
        sameProductFromSelloutBase["brandName"] = productInfoToAdd["brandName"]
        sameProductFromSelloutBase["model"] = productInfoToAdd["model"]
        sameProductFromSelloutBase["colorway"] = productInfoToAdd["colorway"]

    # Таблицы размеров
    if not any(bool(value) for value in sameProductFromSelloutBase["size_tables"].values()):
        sameProductFromSelloutBase["size_tables"] = productInfoToAdd["size_tables"]

    # parameters_to_use_in_filters
    for key, values in productInfoToAdd["parameters_to_use_in_filters"].items():
        if key in sameProductFromSelloutBase["parameters_to_use_in_filters"]:
            # Добавляем только уникальные значения
            for value in values:
                if value not in sameProductFromSelloutBase["parameters_to_use_in_filters"][key]:
                    sameProductFromSelloutBase["parameters_to_use_in_filters"][key].append(value)
        else:
            # Если ключа нет во втором словаре, просто добавляем его
            sameProductFromSelloutBase["parameters_to_use_in_filters"][key] = values

    # parameters_to_show_in_product
    for key, new_value in productInfoToAdd["parameters_to_show_in_product"]["parameters"].items():
        # Если ключ уже есть во втором словаре
        if key in sameProductFromSelloutBase["parameters_to_show_in_product"]["parameters"]:
            if key == "Основные цвета" or key == "Материалы" or key == "Материал верха":
                # Если это "Основные цвета", "Материалы" или "Материал верха", объединяем значения
                sameProductFromSelloutBase["parameters_to_show_in_product"]["parameters"][
                    key] = merge_values_with_comma(
                    sameProductFromSelloutBase["parameters_to_show_in_product"]["parameters"], new_value)
            elif key == "Цена на ритейле":
                # Проверяем особое условие для "Цена на ритейле"
                if platformOfAddingProduct == "goat" and productInfoToAdd.get("retailPrice.price",
                                                                              0) and productInfoToAdd.get(
                    "retailPrice.currency", "") == "USD":
                    sameProductFromSelloutBase["parameters_to_show_in_product"]["parameters"][
                        key] = f'{productInfoToAdd["retailPrice"]["price"]}$'
        else:
            # Добавляем новое поле, если его нет
            sameProductFromSelloutBase["parameters_to_show_in_product"]["parameters"][key] = new_value

    # platformsInfo
    sameProductFromSelloutBase["platformsInfo"][platformOfAddingProduct][
        "preprocessedData"] = preprocessedProductInfoToAdd
    sameProductFromSelloutBase["platformsInfo"][platformOfAddingProduct]["processedData"] = productInfoToAdd

    # Сложные поля
    # Если добавляем информацию от GOAT к товару, у которого есть информация только от неполной АПИ (то есть по сути нет точных цен).
    if platformOfAddingProduct == "goat" and "poizonNotFullApi" in sameProductFromSelloutBase[
        "platformsInfo"] and "poizonHK" not in sameProductFromSelloutBase["platformsInfo"] and not \
            sameProductFromSelloutBase["hasConfigurationsWithDifferentImages"]:
        for unit in productInfoToAdd["units"]:
            for unitExisting in sameProductFromSelloutBase["units"]:
                if unit["view_name"] == unitExisting["view_name"]:
                    unitExisting["offers"].extend(unit["offers"])
                    break
            else:
                unit["unitId"] = len(sameProductFromSelloutBase["units"]) + 1
                sameProductFromSelloutBase["units"].append(unit)
        for image in productInfoToAdd["images"]:
            image["unitsIds"] = list(range(1, len(sameProductFromSelloutBase["units"]) + 1))
        sameProductFromSelloutBase["images"] = productInfoToAdd["images"]
        return

    # endregion

    # region Получение верхне уровневой категории товара на английском языке: categoryEng
    categoryEng = ""
    for category in productInfoToAdd["categories"]:
        if "Обувь" in CATEGORY_NAMES[category]["path"]:
            categoryEng = "shoes"
            break
        elif "Одежда" in CATEGORY_NAMES[category]["path"]:
            categoryEng = "clothes"
            break
        elif "Сумки" in CATEGORY_NAMES[category]["path"]:
            categoryEng = "bags"
            break
        elif "Аксессуары" in CATEGORY_NAMES[category]["path"]:
            categoryEng = "accessories"
            break
    # endregion

    gender = productInfoToAdd["gender"][0]

    # Получается, что мы нашли товар с другим spuId, но таким же артикулом как у какого-то иного товара с пойзона. В таком случае мы не можем связать эти два товара и создаем новый товар
    if platformOfAddingProduct == "poizonNotFullApi" and sameProductFromSelloutBase["platformsInfo"].keys() == [
        "poizonHK"]:
        addProductDataToSelloutBase(platformOfAddingProduct, productInfoToAdd, preprocessedProductInfoToAdd, {})
        return

    # Товар, к которому был привязан ГК + у которого не hasConfigurationsWithDifferentImages.
    # Все, что надо сделать, это заменить все оферы от poizonNotFullApi на новые + картинки на всякий случай заменим.
    if platformOfAddingProduct == "poizonNotFullApi" and set(sameProductFromSelloutBase["platformsInfo"].keys()) == {
        "poizonHK", "poizonNotFullApi"}:
        for image in productInfoToAdd["images"]:
            image["unitsIds"] = list(range(1, len(sameProductFromSelloutBase["units"]) + 1))
        sameProductFromSelloutBase["images"] = productInfoToAdd["images"]

        for unit in sameProductFromSelloutBase["units"]:
            offersOfAddingProduct = []
            for unitOfAddingProduct in productInfoToAdd["units"]:
                if (" " + unitOfAddingProduct["view_name"] + " ") in (" " + unit["view_name"] + " "):
                    offersOfAddingProduct = unitOfAddingProduct["offers"]
            newOffers = []
            for offer in unit["offers"]:
                if "poizonNotFullApi" not in offer["platform_info"]:
                    newOffers.append(offer)
            newOffers.extend(offersOfAddingProduct)
            unit["offers"] = newOffers

        sameProductFromSelloutBase["platformsInfo"]["poizonNotFullApi"] = {
            "preprocessedData": preprocessedProductInfoToAdd,
            "processedData": productInfoToAdd
        }

        return

    # Товар, к которому был привязан ГК + у которого не hasConfigurationsWithDifferentImages. Добавляем GOAT.
    # Меняем картинки, добавляем platformsInfo и units.
    if platformOfAddingProduct == "goat" and set(sameProductFromSelloutBase["platformsInfo"].keys()) == {"poizonHK",
                                                                                                         "poizonNotFullApi"}:
        finalUnits = []
        # Пытаемся связать юниты из goat и из АПИ/poizonHK
        for unitGoat in productInfoToAdd["units"]:
            for unitSameProduct in sameProductFromSelloutBase["units"]:
                # Если есть GOAT название в sameProduct
                if (" " + unitGoat["view_name"] + " ") in (" " + unitSameProduct["view_name"] + " "):
                    unitSameProduct["unitId"] = len(finalUnits) + 1
                    unitSameProduct["offers"].extend(unitGoat["offers"])
                    finalUnits.append(copy.deepcopy(unitSameProduct))
                    break
            else:
                # Пробуем соединить по размеру из filter_size_table_info у юнита.
                table = unitGoat["filter_size_table_info"]["table_name"]
                row = unitGoat["filter_size_table_info"]["table_row_name"]
                allSizeRows = _.get(SIZE_TABLES_DEFAULT_FILTERS, f"{table}.allSizes", [])
                allSizes = []
                for row_ in allSizeRows:
                    if row_["filter_name"] == row:
                        allSizes = row_["sizes"]
                size = unitGoat["filter_size_table_info"]["sizes"][0] if unitGoat["filter_size_table_info"][
                    "sizes"] else ""
                indexSizeGoat = allSizes.index(size) if size in allSizes else -1

                for unitSameProduct in sameProductFromSelloutBase["units"]:
                    table = unitSameProduct["filter_size_table_info"]["table_name"]
                    row = unitSameProduct["filter_size_table_info"]["table_row_name"]
                    size = unitSameProduct["filter_size_table_info"]["sizes"][0] if \
                        unitSameProduct["filter_size_table_info"]["sizes"] else ""
                    allSizeRows = _.get(SIZE_TABLES_DEFAULT_FILTERS, f"{table}.allSizes", [])
                    allSizes = []
                    for row_ in allSizeRows:
                        if row_["filter_name"] == row:
                            allSizes = row_["sizes"]
                    indexSizeSameProduct = allSizes.index(size) if size in allSizes else -1
                    if indexSizeSameProduct == indexSizeGoat and indexSizeGoat != -1:
                        unitSameProduct["unitId"] = len(finalUnits) + 1
                        unitSameProduct["offers"].extend(unitGoat["offers"])
                        finalUnits.append(copy.deepcopy(unitSameProduct))
                        break
                else:
                    unitGoat["unitId"] = len(finalUnits) + 1
                    finalUnits.append(copy.deepcopy(unitGoat))

        for image in productInfoToAdd["images"]:
            image["unitsIds"] = list(range(1, len(sameProductFromSelloutBase["units"]) + 1))
        sameProductFromSelloutBase["images"] = productInfoToAdd["images"]

        sameProductFromSelloutBase["platformsInfo"]["goat"] = {
            "preprocessedData": preprocessedProductInfoToAdd,
            "processedData": productInfoToAdd
        }

        return

    # Не hasConfigurationsWithDifferentImages. Меняем картинки, добавляем platformsInfo и units: тут все просто.
    if platformOfAddingProduct == "goat" and set(sameProductFromSelloutBase["platformsInfo"].keys()) == {
        "poizonNotFullApi"}:
        finalUnits = []
        # Пытаемся связать юниты из goat и из АПИ
        for unitGoat in productInfoToAdd["units"]:
            for unitSameProduct in sameProductFromSelloutBase["units"]:
                # Если есть GOAT название в sameProduct
                if (" " + unitSameProduct["view_name"] + " ") in (" " + unitGoat["view_name"] + " "):
                    unitSameProduct["unitId"] = len(finalUnits) + 1
                    unitSameProduct["offers"].extend(unitGoat["offers"])
                    finalUnits.append(copy.deepcopy(unitSameProduct))
                    break
            else:
                unitGoat["unitId"] = len(finalUnits) + 1
                finalUnits.append(copy.deepcopy(unitGoat))

        sameProductFromSelloutBase["units"] = finalUnits

        for image in productInfoToAdd["images"]:
            image["unitsIds"] = list(range(1, len(sameProductFromSelloutBase["units"]) + 1))
        sameProductFromSelloutBase["images"] = productInfoToAdd["images"]

        sameProductFromSelloutBase["platformsInfo"]["goat"] = {
            "preprocessedData": preprocessedProductInfoToAdd,
            "processedData": productInfoToAdd
        }

        return

    # Не hasConfigurationsWithDifferentImages. Меняем картинки, добавляем platformsInfo и units (добавляем новые и удаляем старые GOAT): тут все просто.
    if platformOfAddingProduct == "goat" and set(sameProductFromSelloutBase["platformsInfo"].keys()) in [{
        "poizonNotFullApi", "goat"}, {"poizonHK", "poizonNotFullApi", "goat"}]:
        finalUnits = []
        # Пытаемся связать юниты из goat и из АПИ/poizonHK
        for unitGoat in productInfoToAdd["units"]:
            for unitSameProduct in sameProductFromSelloutBase["units"]:
                # Если есть GOAT название в sameProduct
                if (" " + unitGoat["view_name"] + " ") in (" " + unitSameProduct["view_name"] + " "):
                    unitSameProduct["unitId"] = len(finalUnits) + 1
                    newOffers = []
                    for offer in unitSameProduct["offers"]:
                        if "goat" not in offer["platform_info"]:
                            newOffers.append(offer)
                    newOffers.extend(unitGoat["offers"])
                    unitSameProduct["offers"] = newOffers
                    finalUnits.append(copy.deepcopy(unitSameProduct))
                    break
            else:
                # Пробуем соединить по размеру из filter_size_table_info у юнита.
                table = unitGoat["filter_size_table_info"]["table_name"]
                row = unitGoat["filter_size_table_info"]["table_row_name"]
                allSizeRows = _.get(SIZE_TABLES_DEFAULT_FILTERS, f"{table}.allSizes", [])
                allSizes = []
                for row_ in allSizeRows:
                    if row_["filter_name"] == row:
                        allSizes = row_["sizes"]
                size = unitGoat["filter_size_table_info"]["sizes"][0] if unitGoat["filter_size_table_info"][
                    "sizes"] else ""
                indexSizeGoat = allSizes.index(size) if size in allSizes else -1

                for unitSameProduct in sameProductFromSelloutBase["units"]:
                    table = unitSameProduct["filter_size_table_info"]["table_name"]
                    row = unitSameProduct["filter_size_table_info"]["table_row_name"]
                    size = unitSameProduct["filter_size_table_info"]["sizes"][0] if \
                        unitSameProduct["filter_size_table_info"]["sizes"] else ""
                    allSizeRows = _.get(SIZE_TABLES_DEFAULT_FILTERS, f"{table}.allSizes", [])
                    allSizes = []
                    for row_ in allSizeRows:
                        if row_["filter_name"] == row:
                            allSizes = row_["sizes"]
                    indexSizeSameProduct = allSizes.index(size) if size in allSizes else -1
                    if indexSizeSameProduct == indexSizeGoat and indexSizeGoat != -1:
                        unitSameProduct["unitId"] = len(finalUnits) + 1
                        newOffers = []
                        for offer in unitSameProduct["offers"]:
                            if "goat" not in offer["platform_info"]:
                                newOffers.append(offer)
                        newOffers.extend(unitGoat["offers"])
                        unitSameProduct["offers"] = newOffers
                        finalUnits.append(copy.deepcopy(unitSameProduct))
                        break
                else:
                    unitGoat["unitId"] = len(finalUnits) + 1
                    finalUnits.append(copy.deepcopy(unitGoat))

        for image in productInfoToAdd["images"]:
            image["unitsIds"] = list(range(1, len(sameProductFromSelloutBase["units"]) + 1))
        sameProductFromSelloutBase["images"] = productInfoToAdd["images"]

        sameProductFromSelloutBase["platformsInfo"]["goat"] = {
            "preprocessedData": preprocessedProductInfoToAdd,
            "processedData": productInfoToAdd
        }

        return

    # Не hasConfigurationsWithDifferentImages. Добавляем оферы от poizonNotFullApi если есть и platformsInfo
    if platformOfAddingProduct == "poizonNotFullApi" and set(sameProductFromSelloutBase["platformsInfo"].keys()) == {
        "goat"}:
        for unit in sameProductFromSelloutBase["units"]:
            for unitOfAddingProduct in productInfoToAdd["units"]:
                if (" " + unitOfAddingProduct["view_name"] + " ") in (" " + unit["view_name"] + " "):
                    unit["offers"].extend(unitOfAddingProduct["offers"])
                    break

        sameProductFromSelloutBase["platformsInfo"]["poizonNotFullApi"] = {
            "preprocessedData": preprocessedProductInfoToAdd,
            "processedData": productInfoToAdd
        }

        return

    # Не hasConfigurationsWithDifferentImages. Заменяем оферы от poizonNotFullApi если есть и platformsInfo
    if platformOfAddingProduct == "poizonNotFullApi" and set(sameProductFromSelloutBase["platformsInfo"].keys()) in [{
        "poizonHK", "poizonNotFullApi", "goat"}, {"poizonNotFullApi", "goat"}]:
        for unit in sameProductFromSelloutBase["units"]:
            offersOfAddingProduct = []
            for unitOfAddingProduct in productInfoToAdd["units"]:
                if (" " + unitOfAddingProduct["view_name"] + " ") in (" " + unit["view_name"] + " "):
                    offersOfAddingProduct = unitOfAddingProduct["offers"]
                    break
            newOffers = []
            for offer in unit["offers"]:
                if "poizonNotFullApi" not in offer["platform_info"]:
                    newOffers.append(offer)
            newOffers.extend(offersOfAddingProduct)
            unit["offers"] = newOffers

        sameProductFromSelloutBase["platformsInfo"]["poizonNotFullApi"] = {
            "preprocessedData": preprocessedProductInfoToAdd,
            "processedData": productInfoToAdd
        }

        return


# Функция для объединения значений по запятым
def merge_values_with_comma(existing_value, new_value):
    existing_set = set(existing_value.split(", "))
    new_set = set(new_value.split(", "))
    # Объединяем уникальные значения
    merged_values = ", ".join(existing_set.union(new_set))
    return merged_values


# Присваиваем вес точности каждому формату даты
def get_precision_level(date_str):
    # Проверяем на формат DD.MM.YYYY
    if re.match(r'\d{2}\.\d{2}\.\d{4}', date_str):
        return 3  # Самый точный уровень

    # Проверяем на формат MM.YYYY
    elif re.match(r'\d{2}\.\d{4}', date_str):
        return 2  # Средний уровень

    # Проверяем на формат Сезон + Год (например, Весна 2022)
    elif re.match(r'(Весна|Лето|Осень|Зима) \d{4}', date_str):
        return 1  # Менее точный уровень

    # Если формат не распознан, возвращаем 0 (невалидный формат)
    return 0
