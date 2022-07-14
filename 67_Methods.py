#It is recommended to standarize the attributes to avoid problems between objects

class User:

    """
    Nevetheless, this is not the best way

    Python use the method __init__

    We can initialize the attributes of the object at the moment to instance them.
    """


    #The parameter self it is referencing the object that is calling the method.
    def init(self): #To declare this function as a method. Must has a parameter to instance itself.
        self.userName = 'default'
        self.password = '123'

    def init_values(self, username,password):
        self.userName = username
        self.password = password

firstUser = User()
secondUser = User()

print(firstUser.__dict__)
print(secondUser.__dict__)

firstUser.init()#In this way, we add the new atrributes to the object.
secondUser.init()

print(firstUser.__dict__)
print(secondUser.__dict__)

firstUser.init_values('User_1',"Pw_1")
secondUser.init_values('User_2',"Pw_2")

print(firstUser.__dict__)
print(secondUser.__dict__)
