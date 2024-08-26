import copy
import pydash as _

from constants import BACKEND_UPDATE_URL
from functions.fetch_functions.get_from_api_async import get_from_api_async
from functions.fetch_functions.get_response_stable import response_stable
from functions.process_data_functions.category_simplify import category_simplify
from functions.process_data_functions.preprocess_dewu_api import preprocess_dewu_api
from functions.process_data_functions.process_preprocessed_api_data import process_preprocessed_api_data


async def process_spu(spu_id):
    try:
        dewu_api_data = await get_from_api_async(spu_id)
        dewu_preprocessed_data = preprocess_dewu_api(dewu_api_data)
        dewu_processed_data = process_preprocessed_api_data(dewu_preprocessed_data)
        # result = await response_stable(BACKEND_UPDATE_URL, call_function=session.post, json=dewu_processed_data)

        result = dict()

        for key, value in dewu_processed_data.items():
            result[key] = value

        result = add_bags_price(result, dewu_api_data)
        result = add_deliveries_indent(result, dewu_api_data)

        return result
    except:
        return dict()


def add_bags_price(result, dewu_api_data):
    result_with_prices = copy.deepcopy(result)
    category_simplified = category_simplify(result["categories"][0])

    if category_simplified == "Сумки":
        result_with_prices["many_sku_api_price"] = int(_.get(dewu_api_data, "data.item.floorPrice", 0)) // 100

    if category_simplified in ["Головные уборы", "Ремни", "Оправы для очков", "Солнцезащитные очки", "Аксессуары",
                               "Сумки"] \
            and len(_.get(dewu_api_data, "data.skus", list())) == 1:
        result_with_prices["one_sku_api_price"] = int(_.get(dewu_api_data, "data.item.floorPrice", 0)) // 100

    return result_with_prices


def add_deliveries_indent(result, dewu_api_data):
    result_with_deliveries_indent = copy.deepcopy(result)

    if _.get(dewu_api_data, "data.item.includeTax", False):
        result_with_deliveries_indent["deliveries_indent"] = 7

    return result_with_deliveries_indent
