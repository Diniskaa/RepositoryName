# TODO импортировать необходимые молули
import csv # Модуль для работы с CSV файлами
import json # Модуль для работы с JSON файлами

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # TODO считать содержимое csv файла
    # Чтение данных из CSV файла
    with open(INPUT_FILENAME, newline='') as csvfile:
        # Используем DictReader, чтобы прочитать каждую строку как словарь,
        # где ключами будут названия столбцов, а значениями - данные из строки
        reader = csv.DictReader(csvfile)
        # Создаем список словарей, который будет содержать все строки из CSV
        data = [row for row in reader]

    # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w') as jsonfile:
        # Преобразуем список словарей в JSON и записываем его в файл
        # Параметр indent указывает использовать отступ, по заданию он равен 4
        json.dump(data, jsonfile, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
