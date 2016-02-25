# http://www.codewars.com/kata/56aed32a154d33a1f3000018/


def my_first_kata(a, b):
    if type(a) == int and type(b) == int:
        return a % b + b % a
    else:
        return False
