# http://www.codewars.com/kata/5648b12ce68d9daa6b000099


def number(bus_stops):
    get_into_the_bus, get_off_the_bus = 0, 0

    for bus_stop in bus_stops:
        get_into_the_bus += bus_stop[0]
        get_off_the_bus += bus_stop[1]

    return get_into_the_bus - get_off_the_bus
