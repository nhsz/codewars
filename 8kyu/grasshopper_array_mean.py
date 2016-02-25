# http://www.codewars.com/kata/55d277882e139d0b6000005d/


def find_average(nums):
    try:
        return float(sum(nums)) / len(nums)
    except ZeroDivisionError:
        return 0
