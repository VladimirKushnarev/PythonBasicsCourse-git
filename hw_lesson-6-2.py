# Task 6-2

class Road:
    __mass_per_m2 = 25   # 25 kg/m2 for 1 cm
    def __init__(self, width, length):
        self.__length = length
        self.__width = width

    def mass(self, thickness):
        return self.__length * self.__width * thickness * Road.__mass_per_m2


if __name__ == '__main__':
    thickness_input = float(input('Введите толщину дороги в сантиметрах: '))
    road = Road(20, 5000)
    mass_asphalt = float(road.mass(thickness_input) / 1000)
    print(f'Масса асфальта толщиной {thickness_input} = {mass_asphalt:.2f} тонн')
