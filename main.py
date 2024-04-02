import asyncio
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

from MainApp.MainAppClass import MainApp

main_app = MainApp()
api_app = FastAPI()


@api_app.get("/parser_dewu_api/process_spu_id")
async def process_spu(spu_id: int):
    result = await MainApp.process_spu(spu_id)

    print(result)

    return result


@api_app.get("/parser_dewu_api/get_new_products_spus")
async def get_new_products_spus():
    new_products_spus = main_app.get_new_products_spus()

    return new_products_spus


if __name__ == "__main__":
    uvicorn.run(api_app, host='0.0.0.0', port=5000)
