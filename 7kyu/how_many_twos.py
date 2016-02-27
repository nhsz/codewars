# http://www.codewars.com/kata/56aed5db9d5cb55de000001c/

def two_count(n):
    if n % 2 == 1:
        return 0
    else:
        return 1 + two_count(n / 2)
