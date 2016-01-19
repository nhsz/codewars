# http://www.codewars.com/kata/548ef5b7f33a646ea50000b2/


def char_freq(message):

    return { character : message.count(character) for character in message }
