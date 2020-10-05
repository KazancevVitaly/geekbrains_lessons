# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

test = open('test.txt', 'r', encoding='utf-8')

i = 0
words = 0
null_str = 0
for el in test:
    print(el, end='')
    n = el.strip().count(' ')
    if n == 0:
        print('В этой строке нет слов')
        null_str += 1
    else:
        print(f'В этой строке {n+1} слов(а)')
    i += 1
    words += n

print(f'В данном файле всего {i} строк(и) (из них {null_str} пустых),\nи '
      f'{words} слов(а)')
test.close()
