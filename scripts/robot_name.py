import string
import random


used = set()


def generateName():
    characters = []
    for j in range(0, 2):
        characters.append(random.choice(string.ascii_uppercase))
    for i in range(0, 3):
        characters.append(str(random.randint(0, 9)))
    separator = ''
    randomName = separator.join(characters)
    return randomName


def check_name(str, set_names):
    while str in set_names:
        str = generateName()
    set_names.add(str)
    return set_names


class Robot:
    def __init__(self):
        self.name = self.get_name()

    def reset(self):
        self.name = generateName()
        self.name = self.check_name()
        return self.name

    def check_name(self):
        while self.name in used:
            self.name = generateName()
        used.add(self.name)
        return self.name

    def get_name(self):
        self.name = generateName()
        self.name = self.check_name()
        return self.name


r = Robot()
print(r.name)
print(r.reset())
name2 = r.name
print(name2)

r2 = Robot()
print(r2.name)


print(used)
