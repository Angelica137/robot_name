import string
import random


def generateName():
    #names_used = set()
    characters = []
    for j in range(0, 2):
        characters.append(random.choice(string.ascii_uppercase))
    for i in range(0, 3):
        characters.append(str(random.randint(0, 9)))
    separator = ''
    randomName = separator.join(characters)
    # if randomName not in names_used:
    #    names_used.add(randomName)

    return randomName


taken_names = {}


class Robot:
    def __init__(self):
        self.name = generateName()
        self.used = {}

    def reset(self):
        self.name = generateName()

    def check_name(self):
        while self.name in self.used:
            self.name = generateName()
        self.used.add(self.name)
        return self.used


def check_name(str, set_names):
    while str in set_names:
        str = generateName()
    set_names.add(str)
    return set_names


s = {'a', 'b', 'angelica'}
word = "angelica"

print(check_name(word, s))

r = Robot()
name = r.name
r.reset()
name2 = r.name
print(name)
print(r.used)
print(name2)

r2 = Robot()
print(r2.name)
