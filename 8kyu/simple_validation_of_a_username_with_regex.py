# http://www.codewars.com/kata/56a3f08aa9a6cc9b75000023/

def allowed_name_length(name):
    return len(name) >= 4 and len(name) <= 16


def allowed_name_characters(name):
    valid_char = True
    for char in name:
        valid_char = valid_char and (char.islower() or char.isdigit() or char == '_')
    return valid_char


def validate_usr(name):
    return allowed_name_length(name) and allowed_name_characters(name)
