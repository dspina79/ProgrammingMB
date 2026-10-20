from animal import Animal

class Giraffe(Animal):
    def animal_type(self):
        return 'Giraffe'

    def move(self):
        print(f'{self.name} trots along')

class Lion(Animal):
    def animal_type(self):
        return 'Giraffe'

class Elephant(Animal):
    def animal_type(self):
        return 'Elephant'

    def remember(self):
        print(f'An elephant like {self.name} never forgets.')

class Panda(Animal):
    def move(self):
        print(f'The cuddly panda, {self.name} walks along the bamboo branches.')

class Tiger(Animal):
    def animal_type(self):
        return 'Tiger'

