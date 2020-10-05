#  Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
#  практических и лабораторных занятий по этому предмету и их количество.
#  Важно, чтобы для каждого предмета не обязательно были все типы занятий.
#  Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
#  Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

with open('text_6.txt', 'r', encoding='utf-8') as lessons:
    lessons_dict = {}
    for el in lessons:
        el = el.split()
        for i in el:
            key = el[0].replace(':', '')
            value = f'{el[1]} {el[2]} {el[3]}'
            dict_ = {key: value}
            break
        lessons_dict.update(dict_)

import re
new_l_dict = {}
for key, value in lessons_dict.items():
    nums = re.findall(r'\d+', value)
    sum_ = 0
    for i in nums:
        i = int(i)
        sum_ += i
    new_dict = {key: sum_}
    new_l_dict.update(new_dict)
print(new_l_dict)
