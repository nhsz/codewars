# http://www.codewars.com/kata/54ba84be607a92aa900000f1/

def is_isogram(string):
    string = string.lower()
    return all(string.count(letter) == 1 for letter in string) or not string
