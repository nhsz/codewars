# http://www.codewars.com/kata/563b74ddd19a3ad462000054

def stringy(size):
    result = ""
    for i in xrange(size):
        if i % 2 == 0:
            result += '1'
        else:
            result += '0'
    return result
