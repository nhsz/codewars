# http://www.codewars.com/kata/56a3f08aa9a6cc9b75000023/


def allowed_username_length(username):
    return len(username) >= 4 and len(username) <= 16
    

def allowed_username_characters(username):
    valid_char = True
    for char in username:
        valid_char = valid_char and (char.islower() or char.isdigit() or char == '_')
        
    return valid_char


def validate_usr(username):
    return allowed_username_length(username) and allowed_username_characters(username)
