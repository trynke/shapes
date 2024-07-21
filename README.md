# shapes
A Python library for working with geometrical shapes

Легко добавить новую фигуру, например прямоугольник:
```python
class Rectangle(Shape):
    def __init__(self, a, b):
        validate_dimensions(a, b)
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b
```