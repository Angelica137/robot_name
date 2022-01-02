import string
import random


"stores the names currenlty in use"
active_robots = ()


def generateName():
    characters = []
    for j in range(0, 2):
        characters.append(random.choice(string.ascii_uppercase))
    for i in range(0, 3):
        characters.append(str(random.randint(0, 9)))
    separator = ''
    randomName = separator.join(characters)
    return randomName


class Robot:
    def __init__(self):
        self.name = generateName()

    def reset(self):
        self.name = generateName()

    def name_avail(self):
        "checks is the name generated is available"
        if self.name in active_robots:
            self.name = generateName()
        else:
            active_robots.add(self.name)


r = Robot()
name = r.name
r.reset()
name2 = r.name
print(name)
print(name2)

r2 = Robot()
print(r2.name)

print(active_robots)
