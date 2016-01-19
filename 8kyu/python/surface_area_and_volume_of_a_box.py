# http://www.codewars.com/kata/565f5825379664a26b00007c/


def get_size(w,h,d):
    area = 2 * w * h + 2 * h * d + 2 * w * d
    volume = w * h * d
    return [area, volume]
