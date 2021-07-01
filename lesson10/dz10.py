# Задание 1


class Matrix:
    def __init__(self, input_list):
        self.input = input_list

    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.input])

    def __add__(self, other):
        add_str = ''
        for line_1, line_2 in zip(self.input, other.input):
            add_func = [x + y for x, y in zip(line_1, line_2)]
            add_str += ' '.join(map(str, add_func)) + '\n'
        return add_str


matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)
print(matrix + matrix_2)

# Задание 2
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def computation(self):
        pass


class Coat(Clothes):
    @property
    def computation(self):
        return self.value / 6.5 + 0.5


class Costume(Clothes):
    @property
    def computation(self):
        return 2 * self.value + 0.3


coat = Coat(20)
costume = Costume(25)
print(coat.computation)
print(costume.computation)


# Задание 3

class Cell:
    def __init__(self, num_cell):
        self.num_cell = num_cell

    def __add__(self, other):
        return str(self.num_cell + other.num_cell)

    def __sub__(self, other):
        check_sub = str(self.num_cell - other.num_cell)
        if int(check_sub) < 0:
            print('Вол-во меньше нуля')
        else:
            return check_sub

    def __mul__(self, other):
        return str(self.num_cell * other.num_cell)

    def __floordiv__(self, other):
        return str(self.num_cell // other.num_cell)

    def make_order(self, size):
        make_cell = '\n'.join(['[]' * size for _ in range(self.num_cell // size)]) \
                    + '\n' + '[]' * (self.num_cell % size)
        return make_cell


cell = Cell(12)
cell2 = Cell(8)
print(cell.__add__(cell2))
print(cell.__sub__(cell2))
print(cell.__mul__(cell2))
print(cell.__floordiv__(cell2))
print(cell.make_order(4))
