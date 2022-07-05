#How to delete elements from a dictionary?

dict = {'a':1,'b':2,'c':3,'d':'4'}
#We are going to use the reserved word del

print(len(dict))
del dict['a']
print(dict) #The element 'a' has been deleted
print(len(dict))

#Second way to delete
key = dict.pop('b') #This method return the value of the key
print(key)
print(dict)
print(len(dict))

#Lets see this error
#del dict['z']
"""
Traceback (most recent call last):
  File "c:/Users/Usuario", line 18, in <module>
    del dict['z']
KeyError: 'z'
"""

#key = dict.pop('z')
"""
Traceback (most recent call last):
  File "c:/Users/Usuario", line 26, in <module>
    key = dict.pop('z')
KeyError: 'z'
"""
#To avoid this error you have to make sure the key exists before trying to delete it.

#How to clear a dict?

print(1,dict) 
dict.clear()
print(2, dict)