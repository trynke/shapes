"""
shapes.py

Модуль содержит инструменты для моделирования геометрических фигур. 

Ключевые особенности:
    - Абстрактный базовый класс для геометрических фигур.
    - Конкретные реализации для круга 'Circle' и треугольника 'Triangle'.
    - Методы для вычисления площади фигур, а для треугольника - проверки, является ли он прямоугольным.
    - Служебная функция 'validate_dimensions(*args)' для валидации размеров фигур.
    - Пользовательское исключение 'InvalidDimensionError' для ошибок, связанных с размерами фигур.

Пример использования:
    >>> from shapes import Circle, Triangle
    >>> circle = Circle(5)
    >>> print(circle.get_area())
    >>> triangle = Triangle(3, 4, 5)
    >>> print(triangle.get_area())
    >>> print(triangle.check_if_right_angled())
"""

import math
from abc import ABC, abstractmethod


class InvalidDimensionError(Exception):
    """Исключение вызывается, когда переданы неверные размеры для фигуры"""


def validate_dimensions(*args):
    """
    Проверяет, являются ли переданные размеры фигуры положительными числами.
    В противном случае вызывает ошибку InvalidDimensionError
    """
    for arg in args:
        if not isinstance(arg, (int, float)) or arg <= 0:
            raise InvalidDimensionError("Размеры фигуры должны быть положительными числами")


class Shape(ABC):
    """Абстрактный класс для геометрической фигуры"""

    @abstractmethod
    def get_area(self):
        """Абстрактный метод для получения площади фигуры"""


class Circle(Shape):
    """
    Класс для представления круга

    Атрибуты
    --------
    radius : int или float
        радиус круга

    Методы
    ------
    get_area():
        возвращает площадь круга
    """

    def __init__(self, r):
        """
        Параметры
        ---------
        r: int или float
            радиус круга
        """
        validate_dimensions(r)
        self.radius = r


    def get_area(self) -> float:
        """
        Считает площадь круга по его радиусу

        Возвращает: 
        ---------
            float: площадь круга 
        """
        return math.pi * self.radius ** 2
    

class Triangle(Shape):
    """
    Класс для представления треугольника

    Атрибуты
    --------
    a, b и с : int или float
        длины сторон  треугольника

    Методы
    ------
    get_area():
        возвращает площадь треугольника
    check_if_right_angled():
        проверяет, является ли треугольник прямоугольным
    """

    def __init__(self, a, b, c):
        """
        Параметры
        ---------
        a, b и с : int или float
            длины сторон  треугольника
        """
        validate_dimensions(a, b, c)
        if not(a + b > c and a + c > b and b + c > a):
            raise InvalidDimensionError("Треугольник с такими сторонами не может существовать")
        
        self.a = a
        self.b = b
        self.c = c

    def get_area(self) -> float:
        """
        Считает площадь треугольника по трём его сторонам

        Возвращает: 
        ---------
            float: площадь треугольника 
        """
        half_p = (self.a + self.b + self.c) / 2 # полупериметр
        # площадь считаем по формуле Герона
        return (half_p * (half_p - self.a) * (half_p - self.b) * (half_p - self.c)) ** 0.5

    def check_if_right_angled(self) -> bool:
        """
        Проверяет, является ли треугольник прямоугольным

        Возвращает: 
        ---------
            bool: True, если прямоугольный, False - если нет
        """
        # после сортировки первыми будут катеты, последней - гипотенуза
        sides = sorted(list((self.a, self.b, self.c)))
        return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2 # проверяем по теореме Пифагора
