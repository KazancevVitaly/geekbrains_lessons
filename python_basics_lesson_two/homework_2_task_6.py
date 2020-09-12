# Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]

goods_list = []
i = 0

while True:
    name = input('Введите название товара:   ')
    cost = input('Укажите стоимость товара:  ')
    sum_ = input('Укажите количество товара:  ')
    unit = input('Укажите единицу измерения:  ')
    goods_dict = {'название': name, 'цена': cost, 'количество': sum_, 'ед': unit}
    i += 1
    goods_tuple = (i, goods_dict)
    print(goods_tuple)
    goods_list.append(goods_tuple)
    print(goods_list)
    pass

# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

