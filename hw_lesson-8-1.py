# Task 8-1

import string


class Date:
    DELIMITER_DASH = '-'

    def __init__(self, date_string):
        self._date_string = date_string  # Этот Атрибут не нужен
        day, month, year = self.conversion_to_tuple(date_string)
        if self.validate_date(day, month, year):
            self._day = day
            self._month = month
            self._year = year
        else:
            raise ValueError(f"The date {day}.{month}.{year} cannot be.")

    @classmethod
    def conversion_to_tuple(cls, date_string):
        # Удалим все виды пробелов и разделим строку по '-'
        date_in_list = date_string.translate({ord(c): None for c in string.whitespace}).split(cls.DELIMITER_DASH)
        if (not date_in_list) or (len(date_in_list) != 3) or (not date_in_list[0].isdigit()) \
                or (not date_in_list[1].isdigit()) or (not date_in_list[2].isdigit()):
            raise ValueError(f"Wrong input data: {date_string}. Conversion impossible.")
        return int(date_in_list[0]), int(date_in_list[1]), int(date_in_list[2])

    @staticmethod
    def validate_date(day, month, year):
        if month < 1 or month > 12:
            return False
        # Проверка на валидность.
        if Date.is_leap(year):
            days_in_month = (31, 29, 31, 30, 31, 30, 31, 31, 29, 31, 30, 31)
        else:
            days_in_month = (31, 28, 31, 30, 31, 30, 31, 31, 29, 31, 30, 31)
        if day < 1 or day > days_in_month[month - 1]:
            return False
        return True

    # Проверка на високосный год
    @staticmethod
    def is_leap(year):
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

    def __str__(self):
        return f'{self._day:02d}.{self._month:02d}.{self._year:4d}'


if __name__ == '__main__':
    d1 = Date('4-   01 -1983')
    print(d1)
    # d2 = Date('  -   01 -1983')  # Неправильные входные данные. Проверка
    # print(d2)
    # d3 = Date('32-   01 -1983')    # Такой даты не может быть. Проверка
    # print(d3)
    # d4 = Date('14-   0 -1000')       # Такой даты не может быть. Проверка
    # print(d4)
    d5 = Date('14-   12 -1000')
    print(d5)
    print('Високосный год?', Date.is_leap(1000))
    print('Високосный год?', Date.is_leap(4000))
    print('Високосный год?', Date.is_leap(2000))
    print('Високосный год?', Date.is_leap(2100))
    print('Високосный год?', Date.is_leap(2020))
    d6 = Date('29-02-2020')  # Ok, т.к это високосный год
    print(d6)
    # d6 = Date('29-02-2022')  # Такой даты не может быть, т.к это не високосный год
    # print(d6)
