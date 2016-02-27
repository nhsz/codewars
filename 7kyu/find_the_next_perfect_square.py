# http://www.codewars.com/kata/56269eb78ad2e4ced1000013/

def is_perfect_square(n):
    return (n ** 0.5).is_integer()


def find_next_square(sq):
    if not is_perfect_square(sq):
        return -1
    else:
        next_perfect_square = sq + 1
        while True:
            if is_perfect_square(next_perfect_square):
                return next_perfect_square
            else:
                next_perfect_square += 1
