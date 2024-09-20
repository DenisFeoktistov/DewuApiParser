import json

from infrastructure.addProductDataToSelloutBase import addProductDataToSelloutBase

platformOfAddingProduct = "goat"
productInfoToAdd = {
    "brands": [
        "UGG"
    ],
    "is_collab": False,
    "collab_names": [],
    "lines": [],
    "categories": [
        "Пляжные сандалии",
        "Шлёпки и тапки"
    ],
    "brandName": "UGG",
    "model": "Tazz Slipper Kids",
    "colorway": "'Sand Sand'",
    "gender": [
        "F",
        "K",
        "M"
    ],
    "baseGenders": [
        "F",
        "K"
    ],
    "extraGenders": [
        "M"
    ],
    "custom": False,
    "manufacturer_sku": "1143776K SAN",
    "date": "30.11.2023",
    "approximate_date": "30.11.2023",
    "retailPrice": {
        "currency": "USD",
        "price": 90
    },
    "description": {
        "language": "ENG",
        "description": ""
    },
    "images": [
        {
            "url": "https://image.goat.com/1000/attachments/product_template_pictures/images/097/104/905/original/1341930_00.png.png",
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
                38,
                39,
                40,
                41,
                42,
                43,
                44,
                45,
                46
            ]
        },
        {
            "url": "https://image.goat.com/attachments/product_template_additional_pictures/images/097/009/535/medium/1341930_02.jpg.jpeg?1705115321",
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
                38,
                39,
                40,
                41,
                42,
                43,
                44,
                45,
                46
            ]
        },
        {
            "url": "https://image.goat.com/attachments/product_template_additional_pictures/images/097/009/537/medium/1341930_03.jpg.jpeg?1705115323",
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
                38,
                39,
                40,
                41,
                42,
                43,
                44,
                45,
                46
            ]
        },
        {
            "url": "https://image.goat.com/attachments/product_template_additional_pictures/images/097/009/536/medium/1341930_04.jpg.jpeg?1705115323",
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
                38,
                39,
                40,
                41,
                42,
                43,
                44,
                45,
                46
            ]
        },
        {
            "url": "https://image.goat.com/attachments/product_template_additional_pictures/images/097/009/538/medium/1341930_05.jpg.jpeg?1705115323",
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
                38,
                39,
                40,
                41,
                42,
                43,
                44,
                45,
                46
            ]
        },
        {
            "url": "https://image.goat.com/attachments/product_template_additional_pictures/images/097/009/093/medium/1341930_06.jpg.jpeg?1705114870",
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
                38,
                39,
                40,
                41,
                42,
                43,
                44,
                45,
                46
            ]
        },
        {
            "url": "https://image.goat.com/attachments/product_template_additional_pictures/images/097/009/541/medium/1341930_07.jpg.jpeg?1705115327",
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
                38,
                39,
                40,
                41,
                42,
                43,
                44,
                45,
                46
            ]
        },
        {
            "url": "https://image.goat.com/attachments/product_template_additional_pictures/images/097/009/543/medium/1341930_08.jpg.jpeg?1705115327",
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
                38,
                39,
                40,
                41,
                42,
                43,
                44,
                45,
                46
            ]
        }
    ],
    "size_tables": {
        "main_regular_table": {},
        "main_measurements_table": {},
        "default_table": {
            "rows_order": [
                "EU",
                "RU",
                "US",
                "CM (JP)",
                "mm (CHN)"
            ],
            "values": {
                "EU": [
                    "16",
                    "16.5",
                    "17",
                    "17.5",
                    "18",
                    "18.5",
                    "19",
                    "19.5",
                    "20",
                    "21",
                    "22",
                    "23",
                    "23.5",
                    "24",
                    "25",
                    "26",
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
                    "40",
                    "40.5",
                    "41",
                    "41.5",
                    "42",
                    "42.5",
                    "43",
                    "43.5",
                    "44",
                    "44.5",
                    "Один размер"
                ],
                "RU": [
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
                    "21",
                    "22",
                    "23",
                    "23.5",
                    "24",
                    "25",
                    "26",
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
                    "40",
                    "40.5",
                    "41",
                    "41.5",
                    "42",
                    "42.5",
                    "43",
                    "43.5",
                    "Один размер"
                ],
                "US": [
                    "1C",
                    "1.5C",
                    "2C",
                    "2.5C",
                    "3C",
                    "3.5C",
                    "4C",
                    "4.5C",
                    "5C",
                    "5.5C",
                    "6C",
                    "6.5C",
                    "7C",
                    "7.5C",
                    "8C",
                    "8.5C",
                    "9C",
                    "9.5C",
                    "10C",
                    "10.5C",
                    "11C",
                    "11.5C",
                    "12C",
                    "12.5C",
                    "13C",
                    "13.5C",
                    "1Y",
                    "1.5Y",
                    "1.5Y",
                    "2Y",
                    "2.5Y",
                    "3Y",
                    "3Y",
                    "3.5Y",
                    "4Y",
                    "4.5Y",
                    "5Y",
                    "5Y",
                    "5.5Y",
                    "6Y",
                    "6.5Y",
                    "6.5Y",
                    "7Y",
                    "7.5Y",
                    "8Y",
                    "8Y",
                    "8.5Y",
                    "9Y",
                    "9.5Y",
                    "9.5Y",
                    "10Y",
                    "10.5Y",
                    "Один размер"
                ],
                "CM (JP)": [
                    "9",
                    "9.5",
                    "10",
                    "10.5",
                    "11.75",
                    "11",
                    "11.5",
                    "12",
                    "12.5",
                    "13",
                    "13.5",
                    "14",
                    "14.25",
                    "14.5",
                    "15",
                    "15.5",
                    "15.75",
                    "16",
                    "16.5",
                    "17",
                    "17.5",
                    "18",
                    "18.25",
                    "18.5",
                    "19",
                    "19.5",
                    "20",
                    "20.25",
                    "20.5",
                    "21",
                    "21.5",
                    "22",
                    "22.5",
                    "23",
                    "23.25",
                    "23.5",
                    "24",
                    "24.5",
                    "25",
                    "25.25",
                    "25.5",
                    "26",
                    "26.5",
                    "27",
                    "27.25",
                    "27.5",
                    "28",
                    "28.5",
                    "28.75",
                    "29",
                    "29.25",
                    "29.5",
                    "Один размер"
                ],
                "mm (CHN)": [
                    "90",
                    "95",
                    "100",
                    "105",
                    "117.5",
                    "110",
                    "115",
                    "120",
                    "125",
                    "130",
                    "135",
                    "140",
                    "142.5",
                    "145",
                    "150",
                    "155",
                    "157.5",
                    "160",
                    "165",
                    "170",
                    "175",
                    "180",
                    "182.5",
                    "185",
                    "190",
                    "195",
                    "200",
                    "202.5",
                    "205",
                    "210",
                    "215",
                    "220",
                    "225",
                    "230",
                    "232.5",
                    "235",
                    "240",
                    "245",
                    "250",
                    "252.5",
                    "255",
                    "260",
                    "265",
                    "270",
                    "272.5",
                    "275",
                    "280",
                    "285",
                    "287.5",
                    "290",
                    "292.5",
                    "295",
                    "Один размер"
                ]
            },
            "table_name": "Основная таблица",
            "table_title": "Детская обувь UGG",
            "table_description": "Обратите внимание, представленная таблица является таблицей по умолчанию. Для разных брендов размеры могут отличаться. Рекомендуем сверять размер конкретно для данного бренда. Вы всегда можете обратиться в службу поддержки, и мы обязательно поможем подобрать вам подходящий размер!"
        },
        "tables_recommendations": {}
    },
    "parameters_to_show_in_product": {
        "parameters": {
            "Основные цвета": "Нейтральный",
            "Материал верха": "Suede",
            "Технология подошвы": "EVA",
            "Цена на ритейле": "90$"
        },
        "parameters_order": [
            "Основные цвета",
            "Материал верха",
            "Материалы",
            "Цена на ритейле",
            "Дизайнер",
            "Технология подошвы"
        ]
    },
    "parameters_to_use_in_filters": {
        "colors": [
            "neutrals",
            "white"
        ],
        "material": [
            "suede"
        ]
    },
    "units": [
        {
            "view_name": "1C US-Kids",
            "unitId": 1,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "1C"
                ]
            },
            "offers": [],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "1.5C US-Kids",
            "unitId": 2,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "1.5C"
                ]
            },
            "offers": [],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "2C US-Kids",
            "unitId": 3,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "2C"
                ]
            },
            "offers": [],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "2.5C US-Kids",
            "unitId": 4,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "2.5C"
                ]
            },
            "offers": [],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "3C US-Kids",
            "unitId": 5,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "3C"
                ]
            },
            "offers": [],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "3.5C US-Kids",
            "unitId": 6,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "3.5C"
                ]
            },
            "offers": [],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "4C US-Kids",
            "unitId": 7,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "4C"
                ]
            },
            "offers": [],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "4.5C US-Kids",
            "unitId": 8,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "4.5C"
                ]
            },
            "offers": [],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "5C US-Kids",
            "unitId": 9,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "5C"
                ]
            },
            "offers": [],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "5.5C US-Kids",
            "unitId": 10,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "5.5C"
                ]
            },
            "offers": [],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "6C US-Kids",
            "unitId": 11,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "6C"
                ]
            },
            "offers": [],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "6.5C US-Kids",
            "unitId": 12,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "6.5C"
                ]
            },
            "offers": [],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "7C US-Kids",
            "unitId": 13,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "7C"
                ]
            },
            "offers": [],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "7.5C US-Kids",
            "unitId": 14,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "7.5C"
                ]
            },
            "offers": [],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "8C US-Kids",
            "unitId": 15,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "8C"
                ]
            },
            "offers": [],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "8.5C US-Kids",
            "unitId": 16,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "8.5C"
                ]
            },
            "offers": [],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "9C US-Kids",
            "unitId": 17,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "9C"
                ]
            },
            "offers": [],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "9.5C US-Kids",
            "unitId": 18,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "9.5C"
                ]
            },
            "offers": [],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "10C US-Kids",
            "unitId": 19,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "10C"
                ]
            },
            "offers": [],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "10.5C US-Kids",
            "unitId": 20,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "10.5C"
                ]
            },
            "offers": [],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "11C US-Kids",
            "unitId": 21,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "11C"
                ]
            },
            "offers": [],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "11.5C US-Kids",
            "unitId": 22,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "11.5C"
                ]
            },
            "offers": [],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "12C US-Kids",
            "unitId": 23,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "12C"
                ]
            },
            "offers": [],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "12.5C US-Kids",
            "unitId": 24,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "12.5C"
                ]
            },
            "offers": [],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "13C US-Kids",
            "unitId": 25,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "13C"
                ]
            },
            "offers": [
                {
                    "price": 206.0,
                    "currency": "USD",
                    "days_min_to_international_warehouse": 10000,
                    "days_max_to_international_warehouse": 10000,
                    "delivery_type": "standard",
                    "platform_info": {
                        "goat": {
                            "delivery_type": "lowestPrice",
                            "shoeCondition": "new_no_defects",
                            "boxCondition": "good_condition"
                        }
                    }
                }
            ],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "13.5C US-Kids",
            "unitId": 26,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "13.5C"
                ]
            },
            "offers": [],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "1Y US-Kids",
            "unitId": 27,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "1Y"
                ]
            },
            "offers": [
                {
                    "price": 171.0,
                    "currency": "USD",
                    "days_min_to_international_warehouse": 10000,
                    "days_max_to_international_warehouse": 10000,
                    "delivery_type": "standard",
                    "platform_info": {
                        "goat": {
                            "delivery_type": "lowestPrice",
                            "shoeCondition": "new_no_defects",
                            "boxCondition": "good_condition"
                        }
                    }
                }
            ],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "1.5Y US-Kids",
            "unitId": 28,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "1.5Y"
                ]
            },
            "offers": [],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "2Y US-Kids",
            "unitId": 29,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "2Y"
                ]
            },
            "offers": [
                {
                    "price": 206.0,
                    "currency": "USD",
                    "days_min_to_international_warehouse": 10000,
                    "days_max_to_international_warehouse": 10000,
                    "delivery_type": "standard",
                    "platform_info": {
                        "goat": {
                            "delivery_type": "lowestPrice",
                            "shoeCondition": "new_no_defects",
                            "boxCondition": "good_condition"
                        }
                    }
                }
            ],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "2.5Y US-Kids",
            "unitId": 30,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "2.5Y"
                ]
            },
            "offers": [],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "3Y US-Kids",
            "unitId": 31,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "3Y"
                ]
            },
            "offers": [
                {
                    "price": 192.0,
                    "currency": "USD",
                    "days_min_to_international_warehouse": 10000,
                    "days_max_to_international_warehouse": 10000,
                    "delivery_type": "standard",
                    "platform_info": {
                        "goat": {
                            "delivery_type": "lowestPrice",
                            "shoeCondition": "new_no_defects",
                            "boxCondition": "good_condition"
                        }
                    }
                }
            ],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "3.5Y US-Kids",
            "unitId": 32,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "3.5Y"
                ]
            },
            "offers": [],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "4Y US-Kids",
            "unitId": 33,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "4Y"
                ]
            },
            "offers": [
                {
                    "price": 151.0,
                    "currency": "USD",
                    "days_min_to_international_warehouse": 1000,
                    "days_max_to_international_warehouse": 1000,
                    "delivery_type": "express",
                    "platform_info": {
                        "goat": {
                            "delivery_type": "instantShipLowestPrice",
                            "shoeCondition": "new_no_defects",
                            "boxCondition": "good_condition"
                        }
                    }
                },
                {
                    "price": 127.0,
                    "currency": "USD",
                    "days_min_to_international_warehouse": 10000,
                    "days_max_to_international_warehouse": 10000,
                    "delivery_type": "standard",
                    "platform_info": {
                        "goat": {
                            "delivery_type": "lowestPrice",
                            "shoeCondition": "new_no_defects",
                            "boxCondition": "good_condition"
                        }
                    }
                }
            ],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "4.5Y US-Kids",
            "unitId": 34,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "4.5Y"
                ]
            },
            "offers": [],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "5Y US-Kids",
            "unitId": 35,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "5Y"
                ]
            },
            "offers": [
                {
                    "price": 136.0,
                    "currency": "USD",
                    "days_min_to_international_warehouse": 1000,
                    "days_max_to_international_warehouse": 1000,
                    "delivery_type": "express",
                    "platform_info": {
                        "goat": {
                            "delivery_type": "instantShipLowestPrice",
                            "shoeCondition": "new_no_defects",
                            "boxCondition": "good_condition"
                        }
                    }
                },
                {
                    "price": 123.0,
                    "currency": "USD",
                    "days_min_to_international_warehouse": 10000,
                    "days_max_to_international_warehouse": 10000,
                    "delivery_type": "standard",
                    "platform_info": {
                        "goat": {
                            "delivery_type": "lowestPrice",
                            "shoeCondition": "new_no_defects",
                            "boxCondition": "good_condition"
                        }
                    }
                }
            ],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "5.5Y US-Kids",
            "unitId": 36,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "5.5Y"
                ]
            },
            "offers": [],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "6Y US-Kids",
            "unitId": 37,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "6Y"
                ]
            },
            "offers": [
                {
                    "price": 150.0,
                    "currency": "USD",
                    "days_min_to_international_warehouse": 1000,
                    "days_max_to_international_warehouse": 1000,
                    "delivery_type": "express",
                    "platform_info": {
                        "goat": {
                            "delivery_type": "instantShipLowestPrice",
                            "shoeCondition": "new_no_defects",
                            "boxCondition": "good_condition"
                        }
                    }
                },
                {
                    "price": 127.0,
                    "currency": "USD",
                    "days_min_to_international_warehouse": 10000,
                    "days_max_to_international_warehouse": 10000,
                    "delivery_type": "standard",
                    "platform_info": {
                        "goat": {
                            "delivery_type": "lowestPrice",
                            "shoeCondition": "new_no_defects",
                            "boxCondition": "good_condition"
                        }
                    }
                }
            ],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "6.5Y US-Kids",
            "unitId": 38,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "6.5Y"
                ]
            },
            "offers": [],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "7Y US-Kids",
            "unitId": 39,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "7Y"
                ]
            },
            "offers": [],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "7.5Y US-Kids",
            "unitId": 40,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "7.5Y"
                ]
            },
            "offers": [],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "8Y US-Kids",
            "unitId": 41,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "8Y"
                ]
            },
            "offers": [],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "8.5Y US-Kids",
            "unitId": 42,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "8.5Y"
                ]
            },
            "offers": [],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "9Y US-Kids",
            "unitId": 43,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "9Y"
                ]
            },
            "offers": [],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "9.5Y US-Kids",
            "unitId": 44,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "9.5Y"
                ]
            },
            "offers": [],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "10Y US-Kids",
            "unitId": 45,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "10Y"
                ]
            },
            "offers": [],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        },
        {
            "view_name": "10.5Y US-Kids",
            "unitId": 46,
            "imagesIds": [
                0
            ],
            "showImage": False,
            "filter_size_table_info": {
                "table_name": "Shoes_Kids",
                "table_row_name": "Американский(US)",
                "sizes": [
                    "10.5Y"
                ]
            },
            "offers": [],
            "weight": 1.25,
            "height": 0,
            "width": 0,
            "length": 0
        }
    ],
    "slug": "tazz-slipper-kids-sand-1143776k-san",
    "id": 1341930
}
preprocessedProductInfoToAdd = {
    "brandName": "UGG",
    "careInstructions": "",
    "color": "Cream",
    "composition": "",
    "designer": "",
    "details": "Sand",
    "fit": "",
    "forAuction": False,
    "gender": [
        "youth"
    ],
    "id": 1341930,
    "internalShot": "taken",
    "maximumOfferCents": 200000,
    "midsole": "EVA",
    "minimumOfferCents": 2500,
    "modelSizing": "",
    "name": "Tazz Slipper Kids 'Sand'",
    "nickname": "Sand",
    "productCategory": "shoes",
    "productType": "sneakers",
    "releaseDate": "2023-11-29T23:59:59.999Z",
    "releaseDateName": "",
    "season": "",
    "silhouette": "Tazz",
    "sizeBrand": "ugg",
    "sizeRange": [
        13,
        1,
        2,
        3,
        4,
        5,
        6
    ],
    "sizeType": "numeric_sizes",
    "sizeUnit": "us",
    "sku": "1143776K SAN",
    "slug": "tazz-slipper-kids-sand-1143776k-san",
    "specialDisplayPriceCents": 9000,
    "specialType": "standard",
    "status": "active",
    "upperMaterial": "Suede",
    "availableSizesNew": [],
    "availableSizesNewV2": [],
    "availableSizesNewWithDefects": [],
    "availableSizesUsed": [],
    "sizeOptions": [
        {
            "presentation": "13",
            "value": 13
        },
        {
            "presentation": "1",
            "value": 1
        },
        {
            "presentation": "2",
            "value": 2
        },
        {
            "presentation": "3",
            "value": 3
        },
        {
            "presentation": "4",
            "value": 4
        },
        {
            "presentation": "5",
            "value": 5
        },
        {
            "presentation": "6",
            "value": 6
        }
    ],
    "lowestPriceCents": 0,
    "newLowestPriceCents": 0,
    "usedLowestPriceCents": 0,
    "productTaxonomy": [],
    "featuredIn": [],
    "localizedSpecialDisplayPriceCents": {
        "currency": "USD",
        "amount": 9000,
        "amountUsdCents": 9000
    },
    "category": [
        "Sandal"
    ],
    "micropostsCount": 0,
    "sellingCount": 0,
    "usedForSaleCount": 0,
    "withDefectForSaleCount": 0,
    "isWantable": True,
    "isOwnable": True,
    "isResellable": True,
    "isOfferable": True,
    "isAvailabilityRestricted": False,
    "directShipping": False,
    "isFashionProduct": False,
    "isRaffleProduct": False,
    "renderImagesInOrder": False,
    "applePayOnlyPromo": False,
    "singleGender": "youth",
    "story": "",
    "pictureUrl": "https://image.goat.com/1000/attachments/product_template_pictures/images/097/104/905/original/1341930_00.png.png",
    "mainGlowPictureUrl": "https://image.goat.com/glow-4-5-25/750/attachments/product_template_pictures/images/097/104/905/original/1341930_00.png.png",
    "mainPictureUrl": "https://image.goat.com/750/attachments/product_template_pictures/images/097/104/905/original/1341930_00.png.png",
    "gridGlowPictureUrl": "https://image.goat.com/glow-4-5-25/375/attachments/product_template_pictures/images/097/104/905/original/1341930_00.png.png",
    "gridPictureUrl": "https://image.goat.com/375/attachments/product_template_pictures/images/097/104/905/original/1341930_00.png.png",
    "robotAssets": [],
    "productTemplateExternalPictures": [
        {
            "mainPictureUrl": "https://image.goat.com/attachments/product_template_additional_pictures/images/097/009/534/medium/1341930_01.jpg.jpeg?1705115319",
            "gridPictureUrl": "https://image.goat.com/attachments/product_template_additional_pictures/images/097/009/534/grid/1341930_01.jpg.jpeg?1705115319",
            "dominantColor": "#000000",
            "sourceUrl": "https://www.goat.com",
            "attributionUrl": "GOAT",
            "aspect": 1.5,
            "order": 1
        },
        {
            "mainPictureUrl": "https://image.goat.com/attachments/product_template_additional_pictures/images/097/009/535/medium/1341930_02.jpg.jpeg?1705115321",
            "gridPictureUrl": "https://image.goat.com/attachments/product_template_additional_pictures/images/097/009/535/grid/1341930_02.jpg.jpeg?1705115321",
            "dominantColor": "#000000",
            "sourceUrl": "https://www.goat.com",
            "attributionUrl": "GOAT",
            "aspect": 1.5,
            "order": 2
        },
        {
            "mainPictureUrl": "https://image.goat.com/attachments/product_template_additional_pictures/images/097/009/537/medium/1341930_03.jpg.jpeg?1705115323",
            "gridPictureUrl": "https://image.goat.com/attachments/product_template_additional_pictures/images/097/009/537/grid/1341930_03.jpg.jpeg?1705115323",
            "dominantColor": "#000000",
            "sourceUrl": "https://www.goat.com",
            "attributionUrl": "GOAT",
            "aspect": 1.5,
            "order": 3
        },
        {
            "mainPictureUrl": "https://image.goat.com/attachments/product_template_additional_pictures/images/097/009/536/medium/1341930_04.jpg.jpeg?1705115323",
            "gridPictureUrl": "https://image.goat.com/attachments/product_template_additional_pictures/images/097/009/536/grid/1341930_04.jpg.jpeg?1705115323",
            "dominantColor": "#000000",
            "sourceUrl": "https://www.goat.com",
            "attributionUrl": "GOAT",
            "aspect": 1.5,
            "order": 4
        },
        {
            "mainPictureUrl": "https://image.goat.com/attachments/product_template_additional_pictures/images/097/009/538/medium/1341930_05.jpg.jpeg?1705115323",
            "gridPictureUrl": "https://image.goat.com/attachments/product_template_additional_pictures/images/097/009/538/grid/1341930_05.jpg.jpeg?1705115323",
            "dominantColor": "#000000",
            "sourceUrl": "https://www.goat.com",
            "attributionUrl": "GOAT",
            "aspect": 1.5,
            "order": 5
        },
        {
            "mainPictureUrl": "https://image.goat.com/attachments/product_template_additional_pictures/images/097/009/093/medium/1341930_06.jpg.jpeg?1705114870",
            "gridPictureUrl": "https://image.goat.com/attachments/product_template_additional_pictures/images/097/009/093/grid/1341930_06.jpg.jpeg?1705114870",
            "dominantColor": "#000000",
            "sourceUrl": "https://www.goat.com",
            "attributionUrl": "GOAT",
            "aspect": 1.5,
            "order": 6
        },
        {
            "mainPictureUrl": "https://image.goat.com/attachments/product_template_additional_pictures/images/097/009/541/medium/1341930_07.jpg.jpeg?1705115327",
            "gridPictureUrl": "https://image.goat.com/attachments/product_template_additional_pictures/images/097/009/541/grid/1341930_07.jpg.jpeg?1705115327",
            "dominantColor": "#000000",
            "sourceUrl": "https://www.goat.com",
            "attributionUrl": "GOAT",
            "aspect": 1.5,
            "order": 7
        },
        {
            "mainPictureUrl": "https://image.goat.com/attachments/product_template_additional_pictures/images/097/009/543/medium/1341930_08.jpg.jpeg?1705115327",
            "gridPictureUrl": "https://image.goat.com/attachments/product_template_additional_pictures/images/097/009/543/grid/1341930_08.jpg.jpeg?1705115327",
            "dominantColor": "#000000",
            "sourceUrl": "https://www.goat.com",
            "attributionUrl": "GOAT",
            "aspect": 1.5,
            "order": 8
        }
    ],
    "prices": [
        {
            "sizeOption": {
                "presentation": "13",
                "value": 13
            },
            "shoeCondition": "new_no_defects",
            "boxCondition": "good_condition",
            "lowestPriceCents": {
                "currency": "USD",
                "amount": 20600,
                "amountUsdCents": 20600
            },
            "instantShipLowestPriceCents": {
                "currency": "USD"
            },
            "lastSoldPriceCents": {
                "currency": "USD",
                "amount": 11200,
                "amountUsdCents": 11200
            },
            "stockStatus": "single_in_stock"
        },
        {
            "sizeOption": {
                "presentation": "1",
                "value": 1
            },
            "shoeCondition": "new_no_defects",
            "boxCondition": "good_condition",
            "lowestPriceCents": {
                "currency": "USD",
                "amount": 17100,
                "amountUsdCents": 17100
            },
            "instantShipLowestPriceCents": {
                "currency": "USD"
            },
            "lastSoldPriceCents": {
                "currency": "USD",
                "amount": 13100,
                "amountUsdCents": 13100
            },
            "stockStatus": "single_in_stock"
        },
        {
            "sizeOption": {
                "presentation": "2",
                "value": 2
            },
            "shoeCondition": "new_no_defects",
            "boxCondition": "good_condition",
            "lowestPriceCents": {
                "currency": "USD",
                "amount": 20600,
                "amountUsdCents": 20600
            },
            "instantShipLowestPriceCents": {
                "currency": "USD"
            },
            "lastSoldPriceCents": {
                "currency": "USD",
                "amount": 0,
                "amountUsdCents": 0
            },
            "stockStatus": "single_in_stock"
        },
        {
            "sizeOption": {
                "presentation": "3",
                "value": 3
            },
            "shoeCondition": "new_no_defects",
            "boxCondition": "good_condition",
            "lowestPriceCents": {
                "currency": "USD",
                "amount": 19200,
                "amountUsdCents": 19200
            },
            "instantShipLowestPriceCents": {
                "currency": "USD"
            },
            "lastSoldPriceCents": {
                "currency": "USD",
                "amount": 19100,
                "amountUsdCents": 19100
            },
            "stockStatus": "single_in_stock"
        },
        {
            "sizeOption": {
                "presentation": "4",
                "value": 4
            },
            "shoeCondition": "new_no_defects",
            "boxCondition": "good_condition",
            "lowestPriceCents": {
                "currency": "USD",
                "amount": 12700,
                "amountUsdCents": 12700
            },
            "instantShipLowestPriceCents": {
                "currency": "USD",
                "amount": 15100,
                "amountUsdCents": 15100
            },
            "lastSoldPriceCents": {
                "currency": "USD",
                "amount": 11600,
                "amountUsdCents": 11600
            },
            "stockStatus": "single_in_stock"
        },
        {
            "sizeOption": {
                "presentation": "5",
                "value": 5
            },
            "shoeCondition": "new_no_defects",
            "boxCondition": "good_condition",
            "lowestPriceCents": {
                "currency": "USD",
                "amount": 12300,
                "amountUsdCents": 12300
            },
            "instantShipLowestPriceCents": {
                "currency": "USD",
                "amount": 13600,
                "amountUsdCents": 13600
            },
            "lastSoldPriceCents": {
                "currency": "USD",
                "amount": 10700,
                "amountUsdCents": 10700
            },
            "stockStatus": "single_in_stock"
        },
        {
            "sizeOption": {
                "presentation": "5",
                "value": 5
            },
            "shoeCondition": "new_no_defects",
            "boxCondition": "badly_damaged",
            "lowestPriceCents": {
                "currency": "USD"
            },
            "instantShipLowestPriceCents": {
                "currency": "USD"
            },
            "lastSoldPriceCents": {
                "currency": "USD",
                "amount": 12500,
                "amountUsdCents": 12500
            },
            "stockStatus": "not_in_stock"
        },
        {
            "sizeOption": {
                "presentation": "5",
                "value": 5
            },
            "shoeCondition": "used",
            "boxCondition": "good_condition",
            "lowestPriceCents": {
                "currency": "USD"
            },
            "instantShipLowestPriceCents": {
                "currency": "USD"
            },
            "lastSoldPriceCents": {
                "currency": "USD",
                "amount": 7200,
                "amountUsdCents": 7200
            },
            "stockStatus": "not_in_stock"
        },
        {
            "sizeOption": {
                "presentation": "6",
                "value": 6
            },
            "shoeCondition": "new_no_defects",
            "boxCondition": "good_condition",
            "lowestPriceCents": {
                "currency": "USD",
                "amount": 12700,
                "amountUsdCents": 12700
            },
            "instantShipLowestPriceCents": {
                "currency": "USD",
                "amount": 15000,
                "amountUsdCents": 15000
            },
            "lastSoldPriceCents": {
                "currency": "USD",
                "amount": 11600,
                "amountUsdCents": 11600
            },
            "stockStatus": "single_in_stock"
        }
    ]
}
sameProductFromSelloutBase = {}

print(json.dumps(addProductDataToSelloutBase(platformOfAddingProduct, productInfoToAdd, preprocessedProductInfoToAdd,
                                             sameProductFromSelloutBase), ensure_ascii=False))
