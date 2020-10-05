#  Создать программно файл в текстовом формате,
#  записать в него построчно данные, вводимые пользователем.
#  Об окончании ввода данных свидетельствует пустая строка.

while True:
    user_file = (open('user_text.txt', 'a', encoding='utf-8'))
    text = input('Набирайте текст, для записи в файл нажимайте enter:    ')
    if text == '':
        user_file.close()
        break
    else:
        user_file.write(f'{text}\n')

print(user_file)
