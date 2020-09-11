# Для списка реализовать обмен значений соседних элементов,
# т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

user_list = []
print(type(user_list))
el = None

while el != 'end':
    el = input('Добавьте один  элемент списка и нажмите enter. Для завершения наберите "end" и нажмите enter.    ')
    if el == 'end':
        break
    else:
        user_list.append(el)
        print(user_list)

print(user_list)

index = 0
for i in range(len(user_list) // 2):
    user_list[index], user_list[index+1] = user_list[index+1], user_list[index]
    index += 2

print(user_list)
print('end')
