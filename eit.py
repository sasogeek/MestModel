import random
from person import Person


class Eit(Person):
    def __init__(self, **kwargs):
        nationalities = ["ghana", "kenya", "nigeria", "ivory coast", "south africa"]
        if kwargs:
            self.name = kwargs['name']
            self.nationality = kwargs['nationality']
        else:
            super().__init__()

        if self.nationality.lower() not in nationalities:
            raise ValueError('Invalid nationality.')

    def say_fun_fact_about_tech_class(self):
        fun_facts = ['Tech class is fun', 'Andrew is beautiful']
        print(random.choice(fun_facts))
