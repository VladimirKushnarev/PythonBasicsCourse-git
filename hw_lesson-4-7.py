# Task 4-7

def my_factorial(f_num):  # Конечный Генератор
    fact = 1
    for i in range(1, f_num + 1):
        fact *= i
        yield fact


def my_factorial_infinity():  # Бесконечный Генератор
    i = 2
    fact = 1
    while True:
        yield fact
        fact = fact * i
        i += 1


if __name__ == '__main__':
    num = int(input('Введите n: '))

    print('Проверяем конечный Генератор')
    for el in my_factorial(num):
        print(el, end=' ')
    print('')
    print(f'Прведение к списку: {list(my_factorial(num))}')

    # Бесконечный Генератор
    print('---------------------------------------')
    print('Проверяем бесконечный Генератор')
    gen_fact = my_factorial_infinity()
    for num in range(num):
        print(next(gen_fact), end=' ')
