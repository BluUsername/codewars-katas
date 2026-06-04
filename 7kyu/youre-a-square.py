import math

def is_square(n):
    if n < 0:
        return False
    return math.isqrt(n) ** 2 == n