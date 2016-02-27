# http://www.codewars.com/kata/539ee3b6757843632d00026b/

def capitals(word):
    return [i for i in range(0, len(word)) if word[i].isupper()]
