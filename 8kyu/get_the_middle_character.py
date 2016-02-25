# http://www.codewars.com/kata/56747fd5cb988479af000028/

def get_middle(s):
    if len(s) % 2 == 1:
        return s[len(s) / 2]
    else:
        return s[len(s) / 2 - 1 : len(s) / 2 + 1]
