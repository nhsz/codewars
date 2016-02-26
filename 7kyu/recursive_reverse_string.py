# http://www.codewars.com/kata/536a9f94021a76ef0f00052f/

def reverse(str):
  return str[-1] + reverse(str[:-1]) if len(str) > 1 else str
