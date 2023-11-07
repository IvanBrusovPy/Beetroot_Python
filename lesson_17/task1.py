class Animal:
    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        print("woof woof")


class Cat(Animal):
    def talk(self):
        print("meow")
        return "meow"


def talk(anim: Animal()):
    anim.talk()


matroskin = Cat()
sharik = Dog()

animals = [matroskin, sharik]
for a in animals:
    a.talk()




