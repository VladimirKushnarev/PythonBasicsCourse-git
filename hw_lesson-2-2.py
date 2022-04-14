# Task 2-2

length = int(input('Сколько элементов будет в спимке? '))
my_list = []

for i in range(length):
    el = input(f'Введите элемент {i + 1}: ')
    my_list.append(el)

print('Искомый список: ', my_list)

len_for = len(my_list) if len(my_list) % 2 == 0 else len(my_list) - 1
for i in range(0, len_for, 2):
    tmp = my_list[i + 1]
    my_list[i + 1] = my_list[i]
    my_list[i] = tmp

print('Искомый список: ', my_list)
