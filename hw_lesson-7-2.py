# Task 7-2

from abc import ABC, abstractmethod


class Clothes(ABC):
    total_material_consumption = 0.0

    @abstractmethod
    def material_consumption(self, size):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v_size = v
        self.__material_for_coat = self.material_consumption(self.v_size)
        Clothes.total_material_consumption += self.__material_for_coat

    @property
    def v_size(self):
        return self.__v_size

    @v_size.setter
    def v_size(self, size):
        if size < 0:
            raise AttributeError('Size must be greater then 0.')
        self.__v_size = size

    def material_consumption(self, size):
        return size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, h):
        self.h_size = h
        self.__material_for_suit = self.material_consumption(self.h_size)
        Clothes.total_material_consumption += self.__material_for_suit

    @property
    def h_size(self):
        return self.__h_size

    @h_size.setter
    def h_size(self, size):
        if size < 0:
            raise AttributeError('Size must be greater then 0.')
        self.__h_size = size

    def material_consumption(self, size):
        return 2 * size + 0.3


if __name__ == '__main__':
    # cl = Clothes()  # You shouldn't create an object from Abstract class

    print('Total material consumption = ', Clothes.total_material_consumption)

    new_coat = Coat(13)
    print('Coat v_size = ', new_coat.v_size)
    print('Total material consumption = ', Clothes.total_material_consumption)

    new_suit = Suit(4)
    print('Suit h_size = ', new_suit.h_size)
    print('Total material consumption = ', Clothes.total_material_consumption)

    # second_coat = Coat(-26)  # The property setter is working Ok
