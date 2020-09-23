# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

numbers = open('text_4.txt', 'r', encoding='utf-8')

numbers_list = []
for el in numbers:
    el = list(el.split())
    el.remove('-')
    numbers_list.append(el)

trans_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
number_dict = dict(numbers_list)
numbers.close()

numbers_two = open('text_4_2.txt', 'a', encoding='utf-8')
for key, value in number_dict.items():
    key = trans_dict.get(key)
    print(f'{key} - {value}', file=numbers_two)
numbers_two.close()
