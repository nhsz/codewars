# http://www.codewars.com/kata/5547929140907378f9000039/


def shortcut(s):
    t = ""

    for char in s:
        if char not in ('a', 'e', 'i', 'o', 'u'):
            t += char

    return t
