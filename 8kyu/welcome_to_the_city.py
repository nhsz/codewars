# http://www.codewars.com/kata/5302d846be2a9189af0001e4/

def say_hello(name, city, state):
    name = " ".join(name)
    return "Hello, {}! Welcome to {}, {}!".format(name, city, state)
