class Figure:

    def __init__(self, l):
        self.lenght = l

    def calc_perimiter(self):
        pass

    def calc_squre(self):
        pass


class Triangle(Figure):

    def __init__(self, a, b, c, h):
        self.first_side = a
        self.second_side = b
        self.third_side = c
        self.height = h

    def calc_perimiter(self):
        return self.first_side + self.second_side + self.third_side

    def calc_square(self):
        return self.third_side * self.height / 2


class Rectangle(Figure):

    def __init__(self, a, b):
        self.first_side = a
        self.second_side = b

    def calc_perimiter(self):
        return 2 * (self.first_side + self.second_side)

    def calc_squre(self):
        return self.first_side * self.second_side


class Squre(Figure):

    def calc_perimiter(self):
        return 4 * self.lenght

    def calc_squre(self):
        return self.lenght ** 2


triangle = Triangle(4, 3, 2, 3)
print(triangle.calc_perimiter())
print(triangle.calc_square())