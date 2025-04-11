# 🐍📈 PyVector

A lightweight 2D vector math library for Python.

## Features

- Vector addition, subtraction, multiplication, and division
- Magnitude and normalization
- Set magnitude
- Copy and random 2D unit vectors

## Usage

```python
from pyvector import *

v1 = createVector(3, 4)
v2 = createVector(1, 2)

print(v1.add(v2))       # (4, 6)
print(v1.mag())         # 5.0
print(v1.normalize())   # (0.6, 0.8)
print(Py.Vector.random2D())  # (random unit vector)
