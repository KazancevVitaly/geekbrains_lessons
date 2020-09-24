# создать (не программно) текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

with open('text_7.txt', 'r', encoding='utf-8') as firms:
    firms_dict = {}
    i = 0
    all_profit = 0
    for el in firms:
        el = el.split()
        # print(el)
        i += 1
        for elm in el:
            key = f'{el[1]} {el[0]}'
            value = float(el[2]) - float(el[3])
            # print(f'{key} - {value}')
            break
        firms_dict.update({key: value})
        all_profit += value
average_dict = {'average_profit': value / i}
# print(average_dict)
# print(firms_dict)
firms_list = [firms_dict, average_dict]
print(firms_list)

import json

with open('json_firms.json', 'w', encoding='utf-8') as firms_json:
    json.dump(firms_list, firms_json)
