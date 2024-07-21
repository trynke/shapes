import unittest
from shapes.shapes import Circle, Triangle, InvalidDimensionError


class TestAddFunction(unittest.TestCase):
    def test_circle_get_area(self):
        """Проверяет, правильно ли метод get_area() класса Circle считает площадь"""
        circle = Circle(3)
        self.assertEqual(circle.get_area(), 28.274333882308138)

    def test_circle_init_non_valid(self):
        """Проверяет, вызывается ли исключение при неверно введённом радиусе круга"""
        with self.assertRaises(InvalidDimensionError):
            wrong_circle = Circle("f")

        with self.assertRaises(InvalidDimensionError):
            wrong_circle = Circle(-1)

    def test_triangle_get_area(self):
        """Проверяет, правильно ли метод get_area() класса Triangle считает площадь"""
        triangle = Triangle(2, 5, 6)
        self.assertEqual(triangle.get_area(), 4.683748498798798)

    def test_triangle_init_non_valid(self):
        """Проверяет, вызывается ли исключение при неверно введённых размерах сторон треугольника"""
        with self.assertRaises(InvalidDimensionError):
            wrong_triangle = Triangle(1, 2, "f")

        with self.assertRaises(InvalidDimensionError):
            wrong_triangle = Triangle(1, -7, 3)

    def test_triangle_init_not_exists(self):
        """Проверяет, вызывается ли исключениеа, если заданный треугольник не существует"""
        with self.assertRaises(InvalidDimensionError):
            wrong_triangle = Triangle(1, 2, 3)

    def test_triangle_check_if_right_angled(self):
        """
        Правильно ли метод check_if_right_angled() класса Triangle 
        проверяет треугольники на прямоугольность
        """
        right_triangle = Triangle(3, 4, 5)
        self.assertTrue(right_triangle.check_if_right_angled())

        not_right_triangle = Triangle(3, 4, 6)
        self.assertFalse(not_right_triangle.check_if_right_angled())


if __name__ == '__main__':
    unittest.main()
