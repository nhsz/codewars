# http://www.codewars.com/kata/55e4c52ad58df7509c00007e/

def validate(username, password):
    validator = Validator()
    return validator.login(username, password)
