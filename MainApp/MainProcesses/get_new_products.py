import asyncio
import random
import aiohttp

from functions.fetch_functions.api_and_filter import api_and_filter
from logger import relevance_update_logger

from functions.fetch_functions.get_response_stable import response_stable


async def process_api_and_filter_batch(to_process_list):
    async with aiohttp.ClientSession() as session:
        tasks = []

        for spu in to_process_list:
            task = asyncio.create_task(api_and_filter(spu, session))
            tasks.append(task)

        return await asyncio.gather(*tasks)


async def get_new_products():
    relevance_update_logger.info("Starting updating cycle")

    relevance_update_logger.info("Getting current product in db")
    async with aiohttp.ClientSession() as session:
        processed_spus = set(
            await response_stable("https://sellout.su/api/v1/product/dewu_info_list", call_function=session.get,
                                  return_value=True))

    all_spus = list(set(range(0, 15_000_000)) - set(processed_spus))
    # all_spus = list(set(range(3_940_000, 3_960_000)) - set(processed_spus))
    # all_spus = list(set(range(2_500_000, 7_000_000)) - set(processed_spus))
    random.shuffle(all_spus)

    relevance_update_logger.info("Getting new products from api")
    results = list()
    step = 20_000

    for i in range(0, len(all_spus), step):
        relevance_update_logger.info(f"Processing {i}:{i + step}")

        for result in await process_api_and_filter_batch(all_spus[i:i + step]):
            results.append(result)

    relevance_update_logger.info("Getting new products from api done")

    new_spus = list(map(lambda result: result[0], filter(lambda result: result[1], results)))

    await send_to_update(new_spus)


async def send_to_update(new_products_list):
    relevance_update_logger.info("Sending request for adding new products")
    relevance_update_logger.info(len(new_products_list))
    async with aiohttp.ClientSession() as session:
        async with session.post("https://sellout.su/parser_intermediate_api/update_new_products_list",
                                json=new_products_list) as response:
            relevance_update_logger.info(response.status)
            relevance_update_logger.info(await response.text())

            if response.status == 200:
                print("OK")


def start_get_new_products_process():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(get_new_products())
