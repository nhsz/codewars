# http://www.codewars.com/kata/56aed5db9d5cb55de000001c/

def two_count(n):
    return 0 if n % 2 == 1 else 1 + two_count(n / 2)
