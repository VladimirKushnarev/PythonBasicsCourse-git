# Task 6-5

class Stationery:
    def __init__(self, title):
        self._title = title
        self._color = None

    def draw(self):
        print(f"Start Drawing")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
        self._color = 'blue'

    def draw(self):
        print(f"{self._title} is drawing with {self._color} color")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
        self._color = 'gray'

    def draw(self):
        print(f"Pencil is Ok to draw. {self._title} is drawing with {self._color} color")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
        self._color = 'yellow'

    def draw(self):
        print(f"Handle is Ok to mark. {self._title} is marking with {self._color} color")


if __name__ == '__main__':
    pen = Pen('Pen')
    pencil = Pencil('Pencil')
    handle = Handle('Handle')
    pen.draw()
    pencil.draw()
    handle.draw()
