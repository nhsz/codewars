# http://www.codewars.com/kata/56170e844da7c6f647000063/


def people_with_age_drink(age):
    kids = xrange(14)
    teens = xrange(14, 18)
    young_adults = xrange(18, 21)

    if age in kids:
        return "drink toddy"
    elif age in teens:
        return "drink coke"
    elif age in young_adults:
        return "drink beer"
    else:
        return "drink whisky"
