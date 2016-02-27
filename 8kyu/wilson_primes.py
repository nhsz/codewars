# http://www.codewars.com/kata/55dc4520094bbaf50e0000cb/

from math import factorial


def am_i_wilson(n):
    return 1 < n <= 563 and (factorial(n - 1) + 1) % (n * n) == 0
