import string
import random


used = set()


def generateName():
    name_parts = []
    name_parts.append(
        ''.join(random.SystemRandom().choices(string.ascii_uppercase, k=2)))
    name_parts.append(
        ''.join(random.SystemRandom().choices(string.digits, k=3)))
    randomName = ''.join(name_parts)
    return randomName


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
