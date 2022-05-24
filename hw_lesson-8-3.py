# Task 8-3

# Сторонняя Библиотека fastnumbers. Функция isfloat() - самый быстрый и эффективный способ проверки на float
# https://pypi.org/project/fastnumbers/
# pip install fastnumbers
# from fastnumbers import isfloat, fast_float

class InputStrNotNumberError(Exception):

    @staticmethod
    def validate_if_float(value):
        # isfloat(value, allow_nan=True)   # Такой способ быстрее. Но нужно подключать стороннюю библиотеку.
        try:
            float(value)
            return True
        except ValueError:
            return False


if __name__ == '__main__':
    DIRECTION_STOP = 'stop'
    list_of_numbers = []
    go = True
    while go:
        direction = input('Write numbers (For Exit write "stop"): ')
        if direction == DIRECTION_STOP:
            go = False
            break
        try:
            if InputStrNotNumberError.validate_if_float(direction):
                list_of_numbers.append(float(direction))
            else:
                raise InputStrNotNumberError(f'Your input "{direction}" is not a number. Try again.')
        except InputStrNotNumberError as err:
            print(err)
    print(list_of_numbers)
