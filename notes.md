used = set() -> time complexity O(1)


def generateName():
    char = ''.join(random.SystemRandom().choices(string.ascii_uppercase, k=2)) -> does not take any input, O(1) + O(1) + O(n); n = the elements we are looking to join. => O(n)
    num = ''.join(random.SystemRandom().choices(string.digits, k=3)) -> does not take any input, O(1) + O(1) + O(n) n = the elements we are looking to join. => O(n)
    randomName = char + num -> O(n^2) 🔥 Concatenating strings is not efficient, it is better to leverage the str.join which is O(n)
    return randomName O(1)

    -> Total time complexity O(n^2)


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
