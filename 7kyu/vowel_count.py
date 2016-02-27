# http://www.codewars.com/kata/54ff3102c1bad923760001f3/

def get_count(input_string):
    num_vowels = 0
    for letter in input_string:
        if letter in {'a', 'e', 'i', 'o', 'u'}:
            num_vowels += 1
    return num_vowels
