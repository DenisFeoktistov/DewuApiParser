import multiprocessing

from functions.main_functions.process_spu import process_spu
from MainApp.MainProcesses.get_new_products import start_get_new_products_process


class MainApp:
    def __init__(self):
        self.get_new_products_spus_process = None

    @staticmethod
    async def process_spu(spu_id):
        result = await process_spu(spu_id)

        return result

    def get_new_products_spus(self):
        try:
            if self.get_new_products_spus_process:
                self.get_new_products_spus_process.terminate()
                self.get_new_products_spus_process.close()

            self.get_new_products_spus_process = multiprocessing.Process(target=start_get_new_products_process)
            self.get_new_products_spus_process.start()
        except:
            pass

        return "OK"
