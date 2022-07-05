dict = {'a':1,'b':2,'c':3,'d':4}

#Methods to implement here: keys(), values(), items()
#This print an elements dict_keys
keys = dict.keys()
print(keys)

keys = tuple(dict.keys()) #It is safer to manipulate the dict's keys in a tuple.
print(keys)

values = tuple(dict.values())
print(values)

#The values and the keys are obtained respectively to its order

#This print an elements dict_items
items = dict.items()
print(items)