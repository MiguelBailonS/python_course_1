#Lets see Heritage in classes

class Pet:
    
    def eat(self):
        print('Eating')

    def sleep(self):
        print('Sleeping')



class Dog(Pet): #The class dog heritage all methods and attributes inside Pet's class.
    pass

#A class can be a "Father class" n-times.

Marley = Dog()

Marley.eat()
Marley.sleep()

print("")
class Cat(Pet):
    pass

Milagro = Cat()
Milagro.eat()
Milagro.sleep()
