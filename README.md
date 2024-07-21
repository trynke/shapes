# shapes
Библиотека на Python для работы с геометрическими фигурами. 
Позволяет создать объект класса Круг или Треугольник, посчитать площадь созданной фигуры, для треугольника - определить, прямоугольный он или нет.

## :computer: Использование
Библиотека написана на чистом Python. Для начала работы необходимо загрузить файлы из репозитория к себе локально.
После этого, находясь в каталоге с данной библиотекой, устанавливаем её с помощью pip:
```bash
$ pip install .
```
Пример использования:
```python
from shapes.shapes import Circle, Triangle
circle = Circle(5)
print(circle.get_area())
triangle = Triangle(3, 4, 5)
print(triangle.get_area())
print(triangle.check_if_right_angled())
```

## :mortar_board: Изменения и тестирование
Легко добавить новую фигуру, например прямоугольник. Дописываем следующий код в файл shapes.py:
```python
class Rectangle(Shape):
    def __init__(self, a, b):
        validate_dimensions(a, b)
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b
```

Тесты запускаются следующим образом:
```bash
$ python -m tests.test
```
