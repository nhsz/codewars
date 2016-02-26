# http://www.codewars.com/kata/552ab0a4db0236ff1a00017a/

def sillycase(silly):
    n = len(silly)
    middle = n / 2
    if n % 2 == 1:
        middle += 1
    return silly[0:middle].lower() + silly[middle:n].upper()
