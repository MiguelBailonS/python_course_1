# Method Overwrite pt2
#What if I want to execute a more Hierarchical level of a method?, Lets see


class livingBeing():
    
    def sleep(self):
        print('Living Being Sleeping')

class Animal(livingBeing):        
    def eat(self): 
        print('Eating')
    pass

class Pet(Animal):
    def eat(self):
        super().eat()
        print("Pet Eating.")
 
class Feline:
    def hunt(self):
        print('Hunting')

class Cat(Pet,Feline): #Multiple Heritage
    def __init__(self, catName):
        self.catName = catName
    
    def eat(self):
        super().eat()
        print(f'{self.catName} eating.') #Overwriting method eat.

Cat_1 = Cat('Milagro')
print(Cat_1.catName)

Cat_1.eat()
Cat_1.sleep() 
