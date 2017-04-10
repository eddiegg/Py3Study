class Animal:

    def __init__(self,species):
        self.species=species

    def eat(self):
        print("Animal can eat")

class People(Animal):

    def __init__(self):
        super().__init__('human')
        self.rights='human'

    def eatfood(self):
        print("People can prepare food to eat")

if __name__ == '__main__':
    eddie = People()
    eddie.eat()
    eddie.eatfood()
    print(eddie.species)


