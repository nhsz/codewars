# http://www.codewars.com/kata/5583090cbe83f4fd8c000051/


def digitize(n):
    answer = []
    for each in str(n):
        answer.insert(0, int(each))
    return answer
