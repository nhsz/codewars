# http://www.codewars.com/kata/56a946cd7bd95ccab2000055/train/python


def lowercase_count(strng):
    total = 0
    for letter in strng:
        if ord(letter) >= 97 and ord(letter) <= 122:
            total += 1
    
    return total
