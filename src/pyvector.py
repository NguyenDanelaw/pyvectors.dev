import math
import random


class Vector:
    def __init__(self, *args: Union[int, float]):
        if not args: # if no arguments were passed
            self.x = self.y = self.z = 0.0
        elif len(args) == 1:
            self.x = float(args[0])
            self.y = self.z = 0.0
        elif len(args) == 2:
            self.x, self.y = float(args[0]), float(args[1])
            self.z = 0.0
        elif len(args) == 3:
            self.x, self.y, self.z = float(args[0]), float(args[1]), float(args[2])
        else:
            raise ValueError(f"Cannot Initialise the vector, expected 3 but got {len(args)}")

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def add(self, *args: "Vector") -> "Vector":
        # can now sum multpile vectors when provided
        return Vector(self.x + sum(v.x for v in args), self.y + sum(v.y for v in args), self.z + sum(v.z for v in args))

    def sub(self, *args: "Vector") -> "Vector":
        # can now subtract multiple vectors when provided
        return Vector(self.x - sum(v.x for v in args), self.y - sum(v.y for v in args), self.z - sum(v.z for v in args))

    def mult(self, *args: "Vector") -> "Vector":
        # can now multiply multiple vectors when provided 
        for v in args:
            self.x *= v.x
            self.y *= v.y
            self.z *= v.z

        return Vector(self.x, self.y, self.z)

    def div(self, *args: "Vector") -> "Vector":
        for v in args:
            if (v.x or v.y or v.z) == 0:
                raise ZeroDivisionError(f"Cannot perform the operation")
            self.x /= v.x
            self.y /= v.y
            self.z /= v.z
        return Vector(self.x, self.y, self.z)

    def mag(self):
        return (self.x ** 2 + self.y ** 2, self.z ** 2) # Use math.sqrt when possible rather than ** 0.5

    def normalize(self):
        m = self.mag()
        if m == 0:
            return Py.Vector(0, 0, 0)
        return Py.Vector(self.x / m, self.y / m, self.z / m)

    def setMag(self, mag):
        n = self.normalize()
        mag = self.mag()
        return Vector(n.x * mag, n.y * mag, n.z / mag)

    def copy(self):
        return Vector(self.x, self.y, self.z)

    @staticmethod
    def random2D():
        angle = random.uniform(0, 2 * math.pi)
        return Vector(math.cos(angle), math.sin(angle))
    
