#Lets see Multiple Heritage in classes

class Animal():        
    def eat(self):
        print('Eating')

    def sleep(self):
        print('Sleeping')

    pass

class Pet(Animal):
    pass

class Feline:
    def hunt(self):
        print('Hunting')

class Cat(Pet,Feline): #Multiple Heritage
    pass

Milagro = Cat()
Milagro.eat()
Milagro.sleep()

print("")
Milagro.hunt()