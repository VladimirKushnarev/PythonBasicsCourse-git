# Task 2-3

dict_months = {12: 'winter', 1: 'winter', 2: 'winter',
               3: 'spring', 4: 'spring', 5: 'spring',
               6: 'summer', 7: 'summer', 8: 'summer',
               9: 'autumn', 10: 'autumn', 11: 'autumn'
               }

list_months = ['winter', 'winter', 'spring',
               'spring', 'spring', 'summer',
               'summer', 'summer', 'autumn',
               'autumn', 'autumn', 'winter'
               ]

month_num = int(input('Введите месяц (числом): '))
print('Решение через словарь.')
print(f'Время года - {dict_months.get(month_num)}')

if month_num < 1 or month_num > 12:
    print('Месяц должен быть от 1 до 12. ')
else:
    print('Решение через список.')
    print(f'Время года - {(list_months[month_num - 1])}')
