#The Dictionaries can store different kind of data:
# List, Tuples, Bool, Int, Float, String
# A dictionary can be declared as follow
# A dicionary is mutable
diccionario = []
diccionario = dict()

#To store data

diccionario = {"total":55}
diccionario = {"total":55, "Discount": True, "Subtotal": 15}
print(diccionario)


#Another example

diccionario = {"Total":55 , 10: "Python Course", (1,2,3): True}
print(diccionario)

#We can use classes as keys for dictionaries

user = {
    'Name':'User name',
    'Age': 23,
    'Course':'Python',
    'Skills':{
        'Programming':True,
        'Databse': False
    },
    'Awards': ['Basic','Intermediate']
} 
#The equivalent of Json format is a Dictionary

#To modfify values we can use []

diccionario = {'A':1,'B':2,'C':3}
print(diccionario['A'])
diccionario['A'] = 2
print(diccionario['A'])

#Add new value
diccionario['D'] = 4
print(diccionario)
#Obtain value thorugh key
print(diccionario['B'])


# We can obtain the values
diccionario = {'Eduardo':1, 'Miguel':2,'Alejandro':3}

diccionario.keys()

diccionario.values()


for key, value in diccionario.items():
    print(key,value)


#With get method we can get an empty value in order to avoid errors/exception

user = {
    'Name':'Miguel',
    'Age':23,
    'Job':'Firmware Developer'
}

grades = user.get('Grades',[])
if grades:
    for grade in grades:
        print(grade)

# We can use comprenhension. In thiss case: Dict Comprenhension

users = ['Miguel','Alejandro','Eduardo']
dict = {users:position +1 for position, users in enumerate(users)}
print(dict)