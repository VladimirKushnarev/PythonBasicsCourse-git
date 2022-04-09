# Task 2-5

my_list = [7, 5, 3, 3, 2]

print(f'Result: {my_list}')
num = int(input('Введите рейтинг: '))

place_index = 0
for i, item in enumerate(my_list):
    if num <= item:
        place_index = i + 1
    else:
        break
my_list.insert(place_index, num)

print(f'Result: {my_list}')
