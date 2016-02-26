# http://www.codewars.com/kata/5500d54c2ebe0a8e8a0003fd/

def mygcd(x, y):
    remainder = max(x, y) % min(x, y)
    if remainder == 0:
        return min(x, y)
    else:
        return mygcd(min(x, y), remainder)
