# http://www.codewars.com/kata/55147ff29cd40b43c600058b/

def char_concat(word):
    middle = len(word) / 2
    if len(word) % 2 == 1:
        word = word[0:middle] + word[middle + 1:len(word)]
    new_word = ""
    i = 0
    j = len(word) - 1
    while i < middle and j > middle - 1:
        new_word += word[i] + word[j] + str(i + 1)
        i += 1
        j -= 1
    return new_word
