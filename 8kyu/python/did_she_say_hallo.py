# http://www.codewars.com/kata/56a4addbfd4a55694100001f/


def validate_hello(greetings):
    different_greetings = ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"]
    
    valid_greeting = False
    i = 0
    while not valid_greeting and i < len(different_greetings):
        valid_greeting = different_greetings[i] in greetings.lower()
        i += 1
        
    return valid_greeting
