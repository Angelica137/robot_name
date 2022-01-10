used = set() -> time complexity O(1)


def generateName():
    name_parts = [] -> O(1)
    name_parts.append(
        ''.join(random.SystemRandom().choices(string.ascii_uppercase, k=2)))  -> O(1) + O(1) + O(n) + O(1)
    name_parts.append(
        str(random.SystemRandom().randint(100, 999))) -> O(1) + O(1)
    randomName = ''.join(name_parts) -> O(n)
    return randomName -> O(1)
    -> TOTAL O(n)



class Robot:
    def __init__(self):
        self.name = self.get_name()

    def reset(self):
        self.name = generateName() -> O(n)
        self.name = self.check_name()
        return self.name
        -> TOTAL O(n)

    def check_name(self):
        while self.name in used: -> O(1); *in* for set is constant
            self.name = generateName() -> O(n)
        used.add(self.name) -> O(1); *add* for set is
        return self.name -> O(1)
        -> Total time complexity: O(n)

    def get_name(self):
        self.name = generateName() -> O(n)
        self.name = self.check_name()  -> O(n)
        return self.name -> O(1)
        -> Total time complexity: O(n)

Robot() time compelxity = O(n)
