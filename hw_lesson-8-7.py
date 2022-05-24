# Task 8-7

from math import sqrt


class ComplexNum:
    """ A class of complex number, a+bj. """

    j = 'j'  # symbol of imaginary

    def __init__(self, re, im):
        if not self.validate_complex_num(re, im):
            raise ValueError("Error. Arguments of complex num must be int or float.")
        self.re = re  # Real number
        self.im = im  # Imaginary number

    @staticmethod
    def validate_complex_num(re, im):
        """ Проверяем что обе части создаваемого комплексного числа int или float  """
        if isinstance(re, (int, float)) and isinstance(im, (int, float)):
            return True
        else:
            return False

    @staticmethod
    def validate_operand(value):
        """ Проверяем что операнд: Либо комплексное число, Либо int, Либо float  """
        if isinstance(value, (ComplexNum, int, float)):
            return True
        else:
            return False

    def __abs__(self):
        """
        Корень суммы квадратов действительного и мнимого коэффициента
        Return:
            float
        """
        return sqrt((self.re * self.re) + (self.im * self.im))

    def __repr__(self):
        """
        Возвращает строку вида: 'ComplexNum(Re, Im)
        Return:
            str
        """
        return f"ComplexNum({self.re}, {self.im})"

    def __str__(self):
        """
        Возвращает строку вида "a+bj"
        Return:
            str
        """
        return f"({self.re}{self.im:+}{self.j})"

    def __add__(self, other):
        """
        Возвращает сумму комплексных чисел.
        other - может быть int, float или ComplexNum
        Return:
            ComplexNum
        """
        if isinstance(other, float) or isinstance(other, int):
            return ComplexNum(self.re + other, self.im)
        if isinstance(other, ComplexNum):
            return ComplexNum(self.re + other.re, self.im + other.im)
        else:
            raise ValueError(f"Error. Argument '{other}' must be ComplexNum, int or float.")

    def __sub__(self, other):
        """
        Возвращает разность комплексных чисел.
        other - может быть int, float или ComplexNum
        Return:
            ComplexNum
        """
        if isinstance(other, float) or isinstance(other, int):
            return ComplexNum(self.re - other, self.im)
        if isinstance(other, ComplexNum):
            return ComplexNum(self.re - other.re, self.im - other.im)
        else:
            raise ValueError(f"Error. Argument '{other}' must be ComplexNum, int or float.")

    def __mul__(self, other):
        """
        Произведение 2-х комплексных чисел.
        int, float or another complex number
        Return:
            ComplexNum
        """
        if isinstance(other, int) or isinstance(other, float):
            return ComplexNum(self.re * other, self.im * other)
        if isinstance(other, ComplexNum):
            return ComplexNum((self.re * other.re - self.im * other.im), (self.re * other.im + self.im * other.re))
        else:
            raise ValueError(f"Error. Argument '{other}' must be ComplexNum, int or float.")

    def __radd__(self, other):
        return self.__add__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __rsub__(self, other):
        """
        Операция вычитания не симметрична. Так что перепишем её для правостороннего варианта.
        Return:
            CustomComplex
        """
        if isinstance(other, float) or isinstance(other, int):
            return ComplexNum(other - self.re, -self.im)
        if isinstance(other, ComplexNum):
            return ComplexNum(other.re - self.re, other.im - self.im)
        else:
            raise ValueError(f"Error. Argument '{other}' must be ComplexNum, int or float.")

    # Внимание!!! Сравнение двух чисел float может привести к ошибкам. Из-за проблемы сравнений
    # чисел с плавающей точкой и их точностью.
    def __eq__(self, other):
        """
        Проверка на равенство комплексных чисел
        Return:
            bool
        """
        return (self.re == other.re) and (self.im == other.im)

    # Т.к. мы переопределим hash-функцию и eq (==), то сможем создавать словари, в которых ключом будет сам объект.
    # Считаем числа одинаковыми, если у них совпадает и действительная и мнимая часть.
    def __hash__(self):
        return hash((self.re, self.im))  # !!!! Здесь передаётся кортеж. Поэтому нужны вторые скобки.

    def __ne__(self, other):
        """
        Проверка на НЕ равенство комплексных чисел
        Return:
            bool
        """
        return (self.re != other.re) or (self.im != other.im)

    def conjugate(self):  # Возврат сопряжённого комплексного числа
        return ComplexNum(self.re, -self.im)


if __name__ == '__main__':
    a = ComplexNum(1, 1)
    b = ComplexNum(1, 0)
    c = ComplexNum(0, 1)
    d = ComplexNum(1, -1)
    e = ComplexNum(-5, 5)
    f = ComplexNum(10, -10)

    print(a + 1)
    print(a + 1.2)
    print(10.5 + a)
    print(1 - a)
    print(b - a)
    print(5 * e)
    print(a * 5 == ComplexNum(5, 5))
    print(a * 5 != ComplexNum(5, 5))
    #l = a + '111'   # ValueError: Error. Argument '111' must be ComplexNum, int or float.
    #m = ComplexNum('string', 8)  # ValueError: Error. Arguments of complex num must be int or float.

    print(a * f)

    print(e.conjugate())
    print(abs(e))






