# http://www.codewars.com/kata/568d0dd208ee69389d000016/

def rental_car_cost(d):
    total = 40 * d
    
    if d >= 7:
        return total - 50
    elif d >= 3:
        return total - 20
    else:
        return total
