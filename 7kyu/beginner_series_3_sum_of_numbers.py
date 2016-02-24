# http://www.codewars.com/kata/55f2b110f61eb01779000053/


def get_sum(a,b):
    if a == b:
        return a
    elif a < b:
        return sum(range(a, b + 1))
    else:
        return sum(range(b, a + 1))
