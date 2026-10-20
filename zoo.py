from menagerie import *

class Zoo(object):
    def __init__(self):
        self.animals = {}

    def add(self, animal):
        if self.animals.get(animal.animal_type()) != None:
            current_amount = self.animals[animal.animal_type()]
            self.animals[animal.animal_type()] = current_amount + 1
        else:
            self.animals[animal.animal_type()] = 1

    def migrate(self):
        # for each animal, print their move() output.
        pass

    def remove_animal(self, animal_type, animal_name):
        pass

    def print_roster(self):
        total_animals = 0
        for creature in self.animals:
            count = self.animals[creature]
            print(f'{creature}\t\t{count}')
            total_animals += 1
        print(f'There are a total of {total_animals} animals at the zoo.')