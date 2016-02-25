# http://www.codewars.com/kata/563cf89eb4747c5fb100001b/

def remove_smallest(numbers):
    if numbers:
        numbers.remove(min(numbers))
    return numbers
