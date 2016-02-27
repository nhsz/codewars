# http://www.codewars.com/kata/554b4ac871d6813a03000035/

def high_and_low(numbers):
    lst = [int(num) for num in numbers.split()]
    return "{0} {1}".format(max(lst), min(lst))
