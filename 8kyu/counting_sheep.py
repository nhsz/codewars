# http://www.codewars.com/kata/54edbc7200b811e956000556

def count_sheeps(array_of_sheeps):
    counter_of_present_sheeps = 0
    for sheep in array_of_sheeps:
        if sheep:
            counter_of_present_sheeps += 1
    return counter_of_present_sheeps
