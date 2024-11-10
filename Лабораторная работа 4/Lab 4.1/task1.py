# TODO решите задачу
import json

def task() -> float:
    # Чтение данных из JSON файла
    with open("input.json", "r") as file:
        # Открываем JSON файл и загружаем его содержимое в переменную data
        data = json.load(file)
        # Вычисляем сумму произведений значений "score" и "weight" для каждого словаря в списке data
        result = sum(item["score"] * item["weight"] for item in data)
        # Округляем результат до 3 знаков после запятой
        return round(result, 3)

# Вызов функции и вывод результата
print(task())

