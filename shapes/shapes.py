import math
from abc import ABC, abstractmethod

class Shape(ABC):
    '''Абстрактный класс для геометрической фигуры'''

    @abstractmethod
    def get_area(self):
        '''Абстрактный метод для получения площади фигуры'''


class Circle(Shape):
    '''
    Класс для представления круга

    Атрибуты
    --------
    radius : int или float
        радиус круга

    Методы
    ------
    get_area():
        возвращает площадь круга
    '''

    def __init__(self, r):
        '''
        Параметры
        ---------
        r: int или float
            радиус круга
        '''

        self.radius = r

    def get_area(self) -> float:
        '''
        Считает площадь круга по его радиусу

        Возвращает: 
            float: площадь круга 
        '''

        return math.pi * self.radius ** 2
    

class Triangle(Shape):
    '''
    Класс для представления треугольника

    Атрибуты
    --------
    a : int или float
        длина стороны a треугольника
    b : int или float
        длина стороны b треугольника
    c : int или float
        длина стороны c треугольника

    Методы
    ------
    get_area():
        возвращает площадь треугольника
    check_if_right_angled():
        проверяет, является ли треугольник прямоугольным
    '''

    def __init__(self, a, b, c):
        '''
        Параметры
        ---------
        a : int или float
            длина стороны a треугольника
        b : int или float
            длина стороны b треугольника
        c : int или float
            длина стороны c треугольника
        '''

        self.a = a
        self.b = b
        self.c = c

    def get_area(self) -> float:
        '''
        Считает площадь треугольника по трём его сторонам

        Возвращает: 
            float: площадь треугольника 
        '''

        half_p = (self.a + self.b + self.c) / 2 # полупериметр
        # площадь считаем по формуле Герона
        return (half_p * (half_p - self.a) * (half_p - self.b) * (half_p - self.c)) ** 0.5

    def check_if_right_angled(self) -> bool:
        '''
        Проверяет, является ли треугольник прямоугольным

        Возвращает: 
            bool: True, если прямоугольный, False - если нет
        '''

        # после сортировки первыми будут катеты, последней - гипотенуза
        sides = sorted(list((self.a, self.b, self.c)))
        return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2 # проверяем по теореме Пифагора
    

'''
Легко добавить новую фигуру, например прямоугольник:
class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        selb.b = b

    def get_area(self):
        return self.a * self.b
'''
