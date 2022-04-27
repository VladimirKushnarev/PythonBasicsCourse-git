# Task 6-3

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income  # {"wage": wage, "bonus": wage}


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


if __name__ == '__main__':
    director = Position('Vladimir', 'Kushnarev', 'director', {"wage": 1000000, "bonus": 5000000})
    manager = Position('Gabi', 'Kushnareva', 'manager', {"wage": 300000, "bonus": 3000000})

    print(f'Full Name: {director.get_full_name()} Total income: {director.get_total_income()}')
    print(f'Full Name: {manager.get_full_name()} Total income: {manager.get_total_income()}')
