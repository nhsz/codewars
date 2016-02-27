# http://www.codewars.com/kata/529eef7a9194e0cbc1000255/

def is_anagram(test, original):
    return sorted(original.lower()) == sorted(test.lower())
