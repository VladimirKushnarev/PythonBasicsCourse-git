# Task 6

a = int(input('Введите a -первый результат спортсмена в км: '))
b = int(input('Введите b - поставленную перед спортсменом цель в км: '))

cur_res = float(a)
day_num = 1
print("Результат:")
print(f'{day_num}-й день: {cur_res: .2f}')
while cur_res < b:
    cur_res = cur_res * 1.1
    day_num += 1
    print(f'{day_num}-й день: {cur_res: .2f}')
