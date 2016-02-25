# http://www.codewars.com/kata/54edbc7200b811e956000556

def count_sheeps(arrayOfSheeps):
    counterOfPresentSheeps = 0
    for sheep in arrayOfSheeps:
        if(sheep):
            counterOfPresentSheeps += 1
    return counterOfPresentSheeps
