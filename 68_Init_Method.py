class User:
    def __init__(self): #Redefining the method __init__
        #print('Create an user')
        self.userName = 'default'
        self.password = 'def' 

firstUser = User() 
#We see the print  because the method __init__ executes when we create an object of the type
print(firstUser.__dict__) #We can see that the object firstUser has the default attributes from __init__

class User_obj:
    def __init__(self, username = '',password = ''): #We can define and initialize attributes to our objects.
        self.username = username
        self.password = password

#Initialy, the object could have more attributes.
#In this part, we can see that when we instance an attribute we could ask for the initial values 
firstUser = User_obj('Miguel','123')
print(firstUser.__dict__)

secondUser = User_obj()
print(secondUser.__dict__) #Attribute as dictionary