# http://www.codewars.com/kata/the-if-function/

def _if(boolean_value, func1, func2):
    return func1() if boolean_value else func2()
