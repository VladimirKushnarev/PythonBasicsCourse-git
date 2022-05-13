# Task 7-1

class Matrix:
    def __init__(self, matrix):
        if isinstance(matrix, list):
            self.__rows = len(matrix)
            if isinstance(matrix[0], list):
                line_size = len(matrix[0])
            else:
                raise AttributeError('All lines in matrix must be lists')
        else:
            raise AttributeError('Matrix must be a list of rows. The instance of matrix is not a list now.')
        self.__columns = line_size

        for line in matrix:
            if (not isinstance(line, list)) or len(line) != line_size:
                raise AttributeError('All lines in matrix must be lists and have the same length. Rectangular matrix')
        self.__matrix = matrix  # The list of lists of int

    # @property
    # def matrix(self):
    #     return self.__matrix
    #
    # @property.setter
    # def matrix(self, matrix):
    #     self.__matrix = matrix

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.__matrix) + '\n'

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError('Not class Matrix')
        if self.__rows != other.__rows or self.__columns != other.__columns:
            raise ValueError('The size of matrixes is not the same.')
        result = [[self.__matrix[i][j] + other.__matrix[i][j] for j in range(0, self.__columns)]
                  for i in range(0, self.__rows)]
        return Matrix(result)

    def __radd__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError('Not class Matrix')
        return self.__add__(other)


if __name__ == '__main__':
    # m1 = Matrix([1, 3, 15])   # raise Error. Matrix must be a list from lists.
    # m2 = Matrix([[1, 2], [3], [10, 15]])   # Must raise Error. Rows must be with the same length.
    m3 = Matrix([[1, 2], [3, -6], [10, 15]])
    print(m3)
    m4 = Matrix([[1, 1], [1, 1], [10, 10]])
    print(m4)
    m5 = m3 + m4
    print(m5)

    m6 = Matrix([[1], [2], [3]])
    print(m6)
    # m7 = m6 + m3   # Different sizes of matrixes
