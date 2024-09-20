import os
import json

from pureApiParser.main import mainProcess
from pureApiParser.preprocessApiData import preprocess_dewu_api


def preprocessData():
    # Пути к папкам
    input_folder = r'C:\Users\HP\PycharmProjects\DewuApiParser\examples\preprocessedData'

    # Список для хранения путей к файлам, которые нужно удалить
    files_to_remove = []

    # Проход по всем файлам в папке 1
    for filename in os.listdir(input_folder):
        if filename.endswith('.json') and not filename.startswith('preprocessedData_'):
            input_file_path = os.path.join(input_folder, filename)

            # Открываем и загружаем JSON из файла
            with open(input_file_path, 'r', encoding='utf-8') as input_file:
                data = json.load(input_file)

            # Обрабатываем данные через preprocess_dewu_api
            processed_data = preprocess_dewu_api(data)

            # Формируем новое имя файла, заменяя 'preprocessed' на 'processed'
            new_filename = "preprocessedData_" + filename
            output_file_path = os.path.join(input_folder, new_filename)

            # Сохраняем результат в папку 2
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                json.dump(processed_data, output_file, ensure_ascii=False, indent=4)

            # Добавляем путь к старому файлу в список для последующего удаления
            files_to_remove.append(input_file_path)

    # Удаляем все старые файлы после завершения обработки
    for file_path in files_to_remove:
        os.remove(file_path)

    print("Все файлы успешно обработаны и сохранены в папку preprocessedData")


def processData():
    # Пути к папкам
    input_folder = r'C:\Users\HP\PycharmProjects\DewuApiParser\examples\preprocessedData'
    output_folder = r'C:\Users\HP\PycharmProjects\DewuApiParser\examples\processedData'

    # Список для хранения путей к файлам, которые нужно удалить
    files_to_remove = []

    # Проход по всем файлам в папке preprocessedData
    for filename in os.listdir(input_folder):
        if filename.endswith('.json') and filename.startswith('preprocessedData_'):
            input_file_path = os.path.join(input_folder, filename)

            # Открываем и загружаем JSON из файла
            with open(input_file_path, 'r', encoding='utf-8') as input_file:
                data = json.load(input_file)

            print(f"Starting to process {filename}")
            # Обрабатываем данные через preprocess_dewu_api
            processedData = mainProcess(data, True)
            print(f"Successfully processed {filename}")

            # Формируем новое имя файла, заменяя 'preprocessed' на 'processed'
            new_filename = filename.replace("preprocessedData", "processedData")
            output_file_path = os.path.join(output_folder, new_filename)

            # Сохраняем результат в папку 2
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                json.dump(processedData, output_file, ensure_ascii=False, indent=4)

    print("Все файлы успешно обработаны и сохранены в папку processedData")


# preprocessData()
processData()
