# Task 7-3


class Cell:
    def __init__(self, particles_input=0):
        self.particles = particles_input  # Количество Ячеек в Клетке

    @property
    def particles(self):
        return self.__particles

    @particles.setter
    def particles(self, particles_num):
        if particles_num < 1 or type(particles_num) != int:
            raise AttributeError('Particles num must be Integer and greater then 0.')
        self.__particles = particles_num

    def __str__(self):  # возвращает строку
        return f"In this cell Particles number = {self.particles}"

    def __add__(self, other):  # self + other
        if not isinstance(other, Cell):
            raise AttributeError('Operand must have class Cell.')
        return Cell(self.__particles + other.__particles)

    def __radd__(self, other):  # other + self
        return self.__add__(other)

    def __sub__(self, other):  # self - other
        if not isinstance(other, Cell):
            raise AttributeError('Operand must have class Cell.')
        sub_res = self.__particles - other.__particles
        if sub_res < 0:
            raise ValueError('Result of subtraction < 0.')
        else:
            return Cell(sub_res)

    def __rsub__(self, other):  # other - self
        if not isinstance(other, Cell):
            raise AttributeError('Operand must have class Cell.')
        sub_res = other.__particles - self.__particles
        if sub_res < 0:
            raise ValueError('Result of subtraction < 0.')
        else:
            return Cell(sub_res)

    def __mul__(self, other):  # self * other
        if not isinstance(other, Cell):
            raise AttributeError('Operand must have class Cell.')
        return Cell(self.__particles * other.__particles)

    def __rmul__(self, other):  # other * self
        return self.__mul__(other)

    def __floordiv__(self, other):  # self // other
        if not isinstance(other, Cell):
            raise AttributeError('Operand must have class Cell.')
        return Cell(self.__particles // other.__particles)

    def make_order(self, nums_in_row):
        (quotient, remainder_of_division) = divmod(self.__particles, nums_in_row)
        return ('*' * nums_in_row + '\n') * quotient + '*' * remainder_of_division + '\n'


if __name__ == '__main__':
    # c1 = Cell(0)  # Particles num must be Integer and greater than 0.
    # c2 = Cell(2.1)  # Particles num must be Integer and greater than 0.

    c3 = Cell(1)
    print('c3 = ', c3)
    c4 = Cell(15)
    print('c4 = ', c4)

    # Test sum
    print('sum c3 + c4 = ', c3 + c4)

    # Test subtraction
    # c5 = c3 - c4    # We raise exception here  c3 < c4
    # print('c5 = ', c5)
    c6 = c4 - c3
    print('subtraction  c4 - c3 = ', c6)

    # Test mult
    c8 = Cell(2)
    print('c8 = ', c8)
    print('c4 * c8 = ', c4 * c8)

    # Test floordiv
    print('c4 // c8 = ', c4 // c8)

    # Test make_order
    print()
    print(c4.make_order(4))
    print((c4 * c8).make_order(13))
