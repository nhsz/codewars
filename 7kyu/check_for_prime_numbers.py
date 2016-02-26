# http://www.codewars.com/kata/53daa9e5af55c184db00025f/

def is_prime(n):
    if n <= 1:
        return False
    else:
        for div in xrange(2, n):
            if n % div == 0 and n != div:
                return False
        return True
