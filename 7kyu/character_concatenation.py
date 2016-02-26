# http://www.codewars.com/kata/55147ff29cd40b43c600058b/

def char_concat(word):
    n = len(word)
    middle = n / 2
    if n % 2 == 1:
        word = word[0:middle] + word[middle + 1:n]
    new_word = ""
    i = 0
    j = n - 1
    while i < middle and j > middle - 1:
        new_word += word[i] + word[j] + str(i + 1)
        i += 1
        j -= 1
    return new_word
