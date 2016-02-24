# http://www.codewars.com/kata/56a4addbfd4a55694100001f/


def validate_hello(greetings):
    return any(x in greetings.lower() for x in ['hello','ciao','salut','hallo','hola','ahoj','czesc'])
