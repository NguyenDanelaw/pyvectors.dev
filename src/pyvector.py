import math
import random

class Py:
    class Vector:
        def __init__(self, x: float, y: float):
            self.x = x
            self.y = y

        def __str__(self):
            return f"({self.x}, {self.y})"

        def add(self, v):
            return Py.Vector(self.x + v.x, self.y + v.y)

        def sub(self, v):
            return Py.Vector(self.x - v.x, self.y - v.y)

        def mult(self, v):
            return Py.Vector(self.x * v.x, self.y * v.y)

        def div(self, v):
            return Py.Vector(self.x / v.x, self.y / v.y)

        def mag(self):
            return (self.x ** 2 + self.y ** 2) ** 0.5

        def normalize(self):
            m = self.mag()
            if m == 0:
                return Py.Vector(0, 0)
            return Py.Vector(self.x / m, self.y / m)

        def setMag(self, mag):
            n = self.normalize()
            return Py.Vector(n.x * mag, n.y * mag)

        def copy(self):
            return Py.Vector(self.x, self.y)

        @staticmethod
        def random2D():
            angle = random.uniform(0, 2 * math.pi)
            return Py.Vector(math.cos(angle), math.sin(angle))

def createVector(x, y):
    return Py.Vector(x, y)
