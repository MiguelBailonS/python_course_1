#Create a dictionary

elements = {}
print(elements)

#Add an element
#Inmutable Objects that are inside the braquets[]

#If the Key doesnt exists, it creates a new Key with its corresponding value.
elements['Name'] = 'Marley'
print(elements)

#The dictionary has an element now.
# How to know the length of the dictionary?

print(len(elements))

#Add a tupple key

elements[(1,2,3)] = 'The key is a tuple'
print(elements)

#How to modify the stored value of a Key?
#If the Key exists, then, the value stored its modified.
elements['Name'] = 'Marley2'
print(elements)

#what happen if we repeat a Key?

#The value of the repeated Key it is ignored.
#The corresponding value of the repeteaded Key will be the last.
elements_2 = {'a':1,'b':2,'c':3,'a':4}
print(elements_2)
print(len(elements_2))
#Since Python 3.7, the order of the in the dictionary will remain. 