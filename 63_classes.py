#Lets create a class that can represent an user

#Class <CamelCase> -> e.g. class <NewUser>

#For convention, the class' name will be in singular.

class User: #We can't leave the block empty, but we can use pass.
    pass #In this way, we avoid errors.

Code = User() #We can initialize it with the atributtes of the class. But User doesnt have any.
print(Code)
print(type(Code))