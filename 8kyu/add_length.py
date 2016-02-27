# http://www.codewars.com/kata/559d2284b5bb6799e9000047/

def add_length(str_):
    lst = str_.split()
    new_list = []

    for word in lst:
        new_word = word + " " + str(len(word))
        new_list.append(new_word)
    return new_list
