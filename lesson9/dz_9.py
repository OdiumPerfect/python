from time import sleep


# Задание 1

class TrafficLight:
    def __init__(self):
        self.__color = {'Red': 7, 'Yellow': 2, 'Green': 5}

    def running(self):
        for color in self.__color:
            print(color)
            sleep(self.__color[f'{color}'])


start_light = TrafficLight()
start_light.running()


# Задание 2

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def func(self):
        print(f'Масса асфальта = {(self._length * self._width * 25 * 5) / 1000} т')


road = Road(120, 320)
road.func()


# Задание 3

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income['wage']
        self._income_bonus = income['bonus']


class Position(Worker):
    def get_full_name(self):
        print(f'ФИО: {self.name} {self.surname} {self.position}')

    def get_total_income(self):
        print(f'Зарплата: Оклад {self._income_wage} + премия {self._income_bonus}')


position_worker = Position('Иван', 'Иванович', 'Менеджер', {'wage': 120, 'bonus': 30})
position_worker.get_full_name()
position_worker.get_total_income()
position_worker1 = Position('Игорь', 'Иванович', 'Строитель', {'wage': 70, 'bonus': 18})
position_worker1.get_full_name()
position_worker1.get_total_income()


# Задание 4

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.show_speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.color} автомобиль {self.name} начал движение, разгоняясь до {self.show_speed} км.ч.')

    def stop(self):
        print(f'{self.color} автомобиль {self.name} тормозит до полной остановки')

    def turn(self, direction):
        print(f'{self.color} автомобиль {self.name} поворачивает {direction}')


class TownCar(Car):
    def go(self):
        if self.show_speed > 60:
            print(
                f'{self.color} автомобиль {self.name} начал движение, разгоняясь до {self.show_speed} км.ч. ' +
                f'Внимание! Превышение скорости'
            )
        else:
            super().go()


class WorkCar(Car):
    def go(self):
        if self.show_speed > 40:
            print(
                f'{self.color} автомобиль {self.name} начал движение, разгоняясь до {self.show_speed} км.ч. ' +
                f'Внимание! Превышение скорости'
            )
        else:
            super().go()


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


car = Car(70, 'Желтый', 'Reno')
car.go()
town_car = TownCar(90, 'Черный', 'BMW')
town_car.go()
work_car = WorkCar(50, 'Белый', 'Газель')
work_car.go()
police_car = PoliceCar(120, 'Белый', 'Toyota', is_police=True)
police_car.turn('налево')


# Задание 5

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'{self.title}. Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title}. Рисуем ручкой')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title}. Рисуем карандашем')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title}. Рисуем маркером')


stationery = Stationery('Портрет')
stationery.draw()
pencil = Pencil('Пейзаж')
pencil.draw()
