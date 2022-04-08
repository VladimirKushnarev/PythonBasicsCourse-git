#  5 и 6 задание
revenue = int(input("Введите сумму выручки: "))  # Выручка
costs = int(input("Введите величину издержек: "))  # Издержки
earnings = revenue - costs  # Прибыль
if earnings >= 0:
    print(f"Фирма получила ПРИБЫЛЬ: {earnings}$")
    if revenue != 0:
        profitability = earnings / revenue  # Рентабельность
        print(f'Рентабельность: {profitability: .2f}')
        num_employees = int(input("Введите колличество сторудников: "))
        print(f'Прибыль в расчёте на одного сотрудника = {earnings / num_employees: .2f}')
    else:
        print('Выручка равно 0. Рентабельность не рассчитываем.')  # Сюда попдём если и Выручка = 0 и Издержки = 0
else:
    print(f"Фирма получила УБЫТОК: {earnings}$")
