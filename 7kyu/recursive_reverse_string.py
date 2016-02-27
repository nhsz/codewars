# http://www.codewars.com/kata/536a9f94021a76ef0f00052f/

def reverse(word):
    return word[-1] + reverse(word[:-1]) if len(word) > 1 else word
