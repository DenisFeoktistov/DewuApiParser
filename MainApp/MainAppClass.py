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
        if not self.get_new_products_spus_process:
            result_queue = multiprocessing.Queue()

            self.get_new_products_spus_process = multiprocessing.Process(target=start_get_new_products_process, args=(result_queue,))

            self.get_new_products_spus_process.start()
            self.get_new_products_spus_process.join()

            result = result_queue.get()

            self.get_new_products_spus_process = None

            return result

        return "New products process already in use"
