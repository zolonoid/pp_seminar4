# Написать скрипт для расчета корреляции Пирсона между
# двумя случайными величинами (двумя массивами).

from statistics import mean
import operator
from math import sqrt
from random import randint
from itertools import repeat


# Pearson correlation coefficient
def pcc(rx: list, ry: list) -> float:
    i_dx = lambda: map(lambda x, mx: x - mx, rx, repeat(mean(rx)))
    i_dy = lambda: map(lambda y, my: y - my, ry, repeat(mean(ry)))
    i_dx2 = map(lambda dx: dx * dx, i_dx())
    i_dy2 = map(lambda dy: dy * dy, i_dy())
    i_dxdy = map(operator.mul, i_dx(), i_dy())
    return sum(i_dxdy) / sqrt(sum(i_dx2) * sum(i_dy2))


print(pcc([randint(1, 99) for i in range(50)], [randint(1, 99) for i in range(50)]))
