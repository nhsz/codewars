# http://www.codewars.com/kata/51675d17e0c1bed195000001/

def solution(digits):
    start = 0
    end = 4
    largest_number_found = digits[:end + 1]

    while end < len(digits):
        current_number = digits[start:end + 1]
        if current_number > largest_number_found:
            largest_number_found = current_number
        start += 1
        end += 1
    return int(largest_number_found)
