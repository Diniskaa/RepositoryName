# TODO Напишите функцию find_common_participants

def find_common_participants(str1, str2, det=','):
    set1 = set(str1.split(det))
    set2 = set(str2.split(det))
    common_participants = sorted(set1.intersection(set2))
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

spisok = find_common_participants(participants_first_group, participants_second_group, det='|')
print(spisok)
