# Task 3-4

def rais_to_power(var, power):
    if var == 0:
        print('Неправильно введены данные, x не может быть равен 0.')
        return None
    if power == 0:
        return 1
    if power > 0 or var < 0:
        print('Неправильно введены данные.')
        return None
    res = 1 / var
    for i in range(abs(power) - 1):
        res *= res
    return res


if __name__ == '__main__':
    x = float(input('Введите действительное положительное число x: '))
    y = int(input('Введите целое отрицательное число y: '))
    print(rais_to_power(x, y))
