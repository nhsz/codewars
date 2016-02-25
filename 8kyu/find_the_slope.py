# http://www.codewars.com/kata/55a75e2d0803fea18f00009d/

def find_slope(points):
    x1, y1, x2, y2 = points[0], points[1], points[2], points[3]
    slope = (y2 - y1) / (x2 - x1)

    try:
        return str(slope)
    except ZeroDivisionError:
        return "undefined"
