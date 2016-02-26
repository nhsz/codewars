# http://www.codewars.com/kata/552ab0a4db0236ff1a00017a/

def sillycase(silly):
    middle = (len(silly) + 1) / 2
    return silly[:middle].lower() + silly[middle:].upper()
