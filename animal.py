class Animal(object):
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f'{self.name} moves.')

    def animal_type(self):
        return 'Animal'