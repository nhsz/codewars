# http://www.codewars.com/kata/54dba07f03e88a4cec000caf/

class Dog(object):
    def __init__(self, breed):
        self.breed = breed

    @staticmethod
    def bark():
        return "Woof"


snoopy = Dog("Beagle")
scoobydoo = Dog("Great Dane")
