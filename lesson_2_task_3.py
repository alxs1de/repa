import math


def square(a):
    area = a * a
    return math.ceil(area)


result = square(3.4)
print(result)
