# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

rating_list = []

while True:
    rating_el = input('Укажите новый элемент рейтинга (значение рейтинга от 1 до 10).'
                      ' Для завершения наберите стоп.   ')
    if rating_el == 'стоп':
        break
    else:
        rating_el = int(rating_el)
        if rating_el > 10 or rating_el < 1:
            print('Значение рейтиинга должно быть от 1 до 10')
            continue
        else:
            rating_list.append(rating_el)
            rating_list = sorted(rating_list)
            rating_list = rating_list[::-1]
            print(rating_list)

print(rating_list)
