# http://www.codewars.com/kata/54ff3102c1bad923760001f3/

def getCount(inputStr):
    num_vowels = 0
    for letter in inputStr:
        if letter in {'a', 'e', 'i', 'o', 'u'}:
            num_vowels += 1
    return num_vowels
