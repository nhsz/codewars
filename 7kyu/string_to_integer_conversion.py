# http://www.codewars.com/kata/54fdadc8762e2e51e400032c/

def my_parse_int(s):
    try:
        return int(s)
    except ValueError:
        return "NaN"
