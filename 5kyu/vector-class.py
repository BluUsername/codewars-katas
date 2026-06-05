import math

class Vector:
    def __init__(self, coordinates: list):
        self.coordinates = coordinates

    def _check_length(self, other):
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError("Vectors must be the same length")

    def add(self, other):
        self._check_length(other)
        return Vector([a + b for a, b in zip(self.coordinates, other.coordinates)])

    def subtract(self, other):
        self._check_length(other)
        return Vector([a - b for a, b in zip(self.coordinates, other.coordinates)])

    def dot(self, other):
        self._check_length(other)
        return sum(a * b for a, b in zip(self.coordinates, other.coordinates))

    def norm(self):
        return math.sqrt(sum(a ** 2 for a in self.coordinates))

    def equals(self, other):
        return self.coordinates == other.coordinates

    def __str__(self):
        return '(' + ','.join(str(a) for a in self.coordinates) + ')'
