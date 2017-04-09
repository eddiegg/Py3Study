class Animal:
    def eat(self):
        print("Animal can eat")

class People(Animal):
    def eatfood(self):
        print("People can prepare food to eat")

if __name__ == '__main__':
    eddie = People()
    eddie.eat()
    eddie.eatfood()


