# Task 6-4

class Car:
    def __init__(self, color, name, is_police=False):
        self._speed = 0
        self._color = color
        self._name = name
        self._is_police = is_police

    @property
    def name(self):
        return self._name

    def go(self, speed):
        self._speed = speed
        print(f"The Car {self._name} is moving with speed = {self._speed} ")

    def stop(self):
        self._speed = 0
        print(f"The Car {self._name} stopped, speed = {self._speed} ")

    def turn(self, direction):
        print(f"The Car {self._name} turned {direction} ")

    def set_speed(self, speed):
        self._speed = speed
        print(f"The Car {self._name} speed =  {self._speed} ")

    def show_speed(self):
        print(f"The Car {self._name} speed =  {self._speed} ")


class TownCar(Car):
    def __init__(self, color, name, passenger_capacity, is_police=False):
        super().__init__(color, name, is_police)
        self.passenger_capacity = passenger_capacity

    def show_speed(self):
        if self._speed <= 60:
            print(f"The Car {self._name} speed =  {self._speed} ")
        else:
            print(f"Caution!!!! The Car {self._name} exceeded the speed limit. Car speed =  {self._speed} ")


class SportCar(Car):
    def go_to_club(self):
        print(f"We are going to the club this Saturday night in my Sport Car {self._name} on speed =  {self._speed} ")

    def won_the_race(self):
        print(f"We Won the Races in my Sport Car {self._name}!!!!! ")


class WorkCar(Car):
    def __init__(self, color, name, load_capacity, is_police=False):
        super().__init__(color, name, is_police)
        self.__load_capacity = load_capacity
        self.__loaded_cur = 0  # In tons

    def load_cargo(self, load_tons):
        if self.__loaded_cur + load_tons > self.__load_capacity:
            print(f"Warning!!! Overload!!! The Car {self._name} loading operation CANCELED! Current Loading = "
                  f"{self.__loaded_cur} tons")
        else:
            self.__loaded_cur += load_tons
            print(f"The Car {self._name} LOADED. Car Current Loading =  {self.__loaded_cur} tons")

    def unload_cargo(self):
        self.__loaded_cur = 0
        print(f"The Car {self._name} UNLOADED. Car Current Loading =  {self.__loaded_cur} tons")

    def show_speed(self):
        if self._speed <= 40:
            print(f"The Car {self._name} speed =  {self._speed} ")
        else:
            print(f"Caution!!!! The Car {self._name} exceeded the speed limit. Car speed =  {self._speed} ")


class PoliceCar(Car):
    def chase(self, car):
        print(f"{self._name}. We want to catch Car {car.name}!!!!! ")


if __name__ == '__main__':
    my_car = TownCar('silver', 'My Mers', 5)
    police_car = PoliceCar('white', 'BMW Police', True)
    my_sport_car = SportCar('white', 'My Ferrari')
    lorry = WorkCar('pink', 'DAF', 20)
    print(vars(my_car))
    print(vars(police_car))
    print(vars(my_sport_car))
    print(vars(lorry))
    my_car.go(380)
    my_car.turn('left')
    my_car.turn('right')
    my_car.show_speed()
    my_car.stop()
    police_car.go(500)
    police_car.show_speed()
    police_car.turn('left')
    police_car.stop()
    my_sport_car.go(800)
    my_sport_car.won_the_race()
    my_sport_car.go_to_club()
    police_car.chase(my_sport_car)
    lorry.go(30)
    lorry.load_cargo(10)
    lorry.go(80)
    lorry.load_cargo(25)
    lorry.unload_cargo()
