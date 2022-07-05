dict = {'a':1,'b':2,'c':3,'d':4}
#Get values stored in Keys
value = dict['d']
print(value)

value = dict['a']
print(value)

value = dict['b']
print(value)

value = dict['c']
print(value)

#If we want to obtain a value of a key that doesnt exist we obtain an error.
#value = dict['z']
"""
Traceback (most recent call last):
    File c:/Users/Usuario", line 16, in <module>
    value = dict['z']
KeyError: 'z'
"""
#First validate if the Key exists
print('z' in dict)

#Safer method to obtain a value of a dict
value = dict.get('d')
print(value)

value = dict.get('z')
print(value)#None -> The Key 'z' doesnt exists

#Method get has another parameter.
value = dict.get('z','The key/value doesnt exists in the dict')
print(value)

value = dict.get('z',False)
print(value)

value = dict.get('z',2)
print(value)

#Get the value of the Key. In case the Key doesnt exists, add the key with a new value.
value = dict.setdefault('e',5)
print(value)
print(dict)

value = dict.setdefault('a',2)
print(value)
print(dict)