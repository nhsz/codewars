# http://www.codewars.com/kata/55cb854deb36f11f130000e1/

def weather_info(temp):
    celsius = convert_to_celsius(temp)

    if (celsius <= 0):
        return (str(celsius) + " is freezing temperature")
    else:
        return (str(celsius) + " is above freezing temperature")


def convert_to_celsius(fahrenheit):
  return (fahrenheit - 32) * (5 / 9.)
