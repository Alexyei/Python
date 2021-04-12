from stdlib_python import stddraw


class Rectangle:
    def __init__(self, x0, y0, x1, y1):
        self._x0 = min(x0, x1)
        self._y0 = min(y0, y1)
        self._x1 = max(x0, x1)
        self._y1 = max(y0, y1)

    def area(self):
        return (self._x1 - self._x0) * (self._y1 - self._y0)

    def perimeter(self):
        return ((self._x1 - self._x0) + (self._y1 - self._y0)) * 2

    def intersects(self, other):
        return other._x1 >= self._x0 and other._x0 <= self._x1 and other._y1 >= self._y0 and other._y0 <= self._y1

    def contains(self, other):
        return other._x0 >= self._x0 and other._y0 >= self._y0 and other._x1 <= self._x1 and other._y1 <= self._y1

    def draw(self):
        stddraw.filledRectangle(self._x0, self._y0, self._x1 - self._x0, self._y1 - self._y0)
