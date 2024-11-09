# TODO Напишите функцию find_common_participants

def find_common_participants(str1, str2, det=','):
    # Разбиваем первую строку по разделителю и преобразуем в множество
    set1 = set(str1.split(det))
    # Разбиваем вторую строку по разделителю и преобразуем в множество
    set2 = set(str2.split(det))
    # Находим пересечение множеств
    common_participants = list(set1.intersection(set2))
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

spisok = find_common_participants(participants_first_group, participants_second_group, det='|')
print(spisok)
