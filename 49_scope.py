#Scope
animal = 'Lion' #Global Variables

def print_zoo():
    print(animal)

def print_zoo_2():
    animal = 'Whale' #Does not modify the original valuie of animal in Line 2
    #Loval variable 'animal' 
    print(animal)


print_zoo() #print 'Lion'
print_zoo_2() #Print 'Whale'
print(animal) #Print 'Lion'

#How to differentiate variables? 
#We can use the id function

def print_zoo_3():
    animal = 'Cat' #Local Variable
    destroyed_local_variable = 'Hello'
    print(animal, id(animal))
    #After the function is executed, the local variables are destroyed

print_zoo_3()
print(animal,id(animal))
#print(destroyed_local_variable)
'''
Traceback (most recent call last):
  File , line 28, in <module>        
    print(destroyed_local_variable)
NameError: name 'destroyed_local_variable' is not defined
'''

def print_zoo_4(): 
    global animal#With this declaration, we are refering to the global variable in Line 2
    animal = 'Whale'
    print(animal,id(animal))

print_zoo_4()
print(animal,id(animal))

