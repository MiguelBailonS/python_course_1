# Method Overwrite
# It consist that a child class could modify the methods of the heritage's class.

# More Hierarchical levels, more abstract
# Less Hierarchical leves, less abstract

class livingBeing():
    
    def sleep(self):
        print('Living Being Sleeping')

class Animal(livingBeing):        
    def eat(self): 
        print('Eating')

#    def sleep(self):
#        print('Sleeping')

    pass

class Pet(Animal):
    def eat(self): #To Overwrite a method it is enough to defines it in a lower hierarchical level.
        print("Pet Eating.")
 
class Feline:
    def hunt(self):
        print('Hunting')

class Cat(Pet,Feline): #Multiple Heritage
    def __init__(self, catName):
        self.catName = catName
    
    def eat(self):
        print(f'{self.catName} eating.') #Overwriting method eat.

#    def sleep(self):
#        print(f'{self.catName} sleeping.')    #OverWriting method sleep.

Cat_1 = Cat('Milagro')
print(Cat_1.catName)

#In the execution of the methods, Python will search eat() method in Cat, if it doesnt finds it.
# Python will search in the upper hierarchical level.
# First, it will Look in Pet Class, if it doesnt finds it. Then, will be looing in Feline.
# Searching order: From Left to Rigth
# When the method is finded, it will be executed. 
Cat_1.eat()
Cat_1.sleep() #Now, it will look until LivingBeing class where sleep method is defined
