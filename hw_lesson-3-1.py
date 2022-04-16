# Task 3-1

def divide(numerator, denominator):
    try:
        res = numerator / denominator
    except ZeroDivisionError:
        print('Ошибка деления на ноль. Будьте внимательны.')
        return None
    return res


if __name__ == '__main__':
    num = int(input('Введите числитель: '))
    div = int(input('Введите знаменатель: '))
    print(divide(num, div))
