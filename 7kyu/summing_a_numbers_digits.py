# http://www.codewars.com/kata/52f3149496de55aded000410/

def sum_digits(number):
    return sum(int(digit) for digit in str(abs(number)))
