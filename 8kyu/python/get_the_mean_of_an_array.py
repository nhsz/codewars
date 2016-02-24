# http://www.codewars.com/kata/563e320cee5dddcf77000158/


from math import floor


def get_average(marks):
    return floor(sum(marks) / len(marks))
