# http://www.codewars.com/kata/53f1015fa9fe02cbda00111a/

import random


def get_color():
    return random.choice(["white", "yellow", "purple", "red"])

class Ghost(object):
    def __init__(self):
        self.color = get_color()
