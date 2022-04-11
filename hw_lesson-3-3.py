# Task 3-3

def my_func(var_1, var_2, var_3):
    return var_1 + var_2 + var_3 - min(var_1, var_2, var_3)


if __name__ == '__main__':
    x = int(input('Введите число x: '))
    y = int(input('Введите число y: '))
    z = int(input('Введите число z: '))
    print(my_func(x, y, z))
