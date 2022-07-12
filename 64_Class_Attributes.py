
#Exist two types of attributes:
#  Class Attributes             - To use them, we have to use that class. We can create them in the class.
#  Instance Attributes          - To use them, we have to use the Object.

class User:
    userName = 'userName'
    password = ''

print(User.userName) #We visualize in console the default value. //Read 


User.userName = 'userName_2' #Write

print(User.userName) 

User.password = 'password' #Write

print(User.password)
