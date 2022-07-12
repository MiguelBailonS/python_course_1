
class User:
    userName = 'Miguel'
    password = ''


#__dict__ In this attributte we will find all the attributes that our Object has
user_M = User()
# 1.- Verift if the  attribute exist in out object.
# 2.- Verify if the attribute exist inside a class (Just for Reading)
# 3.- Throws an error
print(user_M.userName) #As the attribute exitst, Python we return the default value.


print(user_M.__dict__) #The object does not have any attribute. This will allows us to know all the attributes that the object has.

#print(user_M.userNames) # <-- Error throwed because the attribute doest exist neither in the object or class

"""
Traceback (most recent call last):
  File "", line 15, in <module>
    print(user_M.userNames)
AttributeError: 'User' object has no attribute 'userNames'. Did you mean: 'userName'?
"""

print(id(user_M.userName))
print(id(User.userName)) #The IDs are equal.