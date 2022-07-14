#How to add attributes to our objects?

class User:
    username = 'Default name'
    email = ''

firstUser = User()

firstUser.username = 'Cody' #Add an attribute to the object - Instance Attributte
firstUser.password = '123' #Second attribute added. If the attribute doesnt exist, will be created.
print(firstUser.username)
print(firstUser.password)
print(firstUser.__dict__)

secondUser = User()
#print(secondUser.password) #We obtain an error because password attribute doesnt exist in secondUser.
print(secondUser.__dict__)