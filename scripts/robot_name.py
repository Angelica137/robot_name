import string
import random


used = set()


def generate_name():
    name_parts = []
    name_parts.append(
        ''.join(random.SystemRandom().choices(string.ascii_uppercase, k=2)))
    name_parts.append(
        str(random.SystemRandom().randint(100, 999)))
    random_name = ''.join(name_parts)
    return random_name


class Robot:
    def __init__(self):
        self.name = self.get_name()

    def reset(self):
        self.name = generate_name()
        self.name = self.check_name()
        return self.name

    def check_name(self):
        while self.name in used:
            self.name = generate_name()
        used.add(self.name)
        return self.name

    def get_name(self):
        self.name = generate_name()
        self.name = self.check_name()
        return self.name
