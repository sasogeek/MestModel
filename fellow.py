from person import Person


class Fellow(Person):
    def __init__(self):
        super().__init__()
        self.happiness_level = 0

    def eat(self):
        self.happiness_level += 1
        print('{fellow} just ate, happiness leveled up to {happiness_level}'.
              format(fellow=self.name, happiness_level=self.happiness_level))

    def teach(self):
        self.happiness_level -= 1
        print('{fellow} just taught, happiness leveled down to {happiness_level}'.
              format(fellow=self.name, happiness_level=self.happiness_level))
