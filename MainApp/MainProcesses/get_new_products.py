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

    all_spus = list(set(range(0, 7_000_000)) - set(processed_spus))
    # all_spus = list(set(range(3_980_000, 4_000_000)) - set(processed_spus))
    random.shuffle(all_spus)

    relevance_update_logger.info("Getting new products from api")
    results = list()
    step = 20_000

    for i in range(0, len(all_spus), step):
        relevance_update_logger.info(f"Processing {i}:{i + step}")

        for result in await process_api_and_filter_batch(all_spus[i:i + step]):
            results.append(result)

    relevance_update_logger.info("Getting new products from api done")

    return list(map(lambda result: result[0], filter(lambda result: result[1], results)))


async def start_get_new_products_process():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    result = await get_new_products()

    return result
