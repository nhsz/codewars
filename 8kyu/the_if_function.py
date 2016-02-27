# http://www.codewars.com/kata/the-if-function/

def _if(bool, func1, func2):
    return func1() if bool else func2()
