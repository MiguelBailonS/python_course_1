name = 'Miguel Alejandro'
last_name = 'Bailon'

#Lest introduce to place holders

full_name = 'Mr. {} {}.'.format(name,last_name)
print(full_name)

#Add a new last name

full_name = 'Mr. {} {} {}.'.format(name,last_name, 'Silva')
print(full_name)

#Lets add names to the place holder

full_name = 'Mr. {name} {first_last_name} {second_last_name}...'.format(
    name = name,
    first_last_name = last_name, 
    second_last_name ='Silva')
print(full_name)

#It is good to use name in the placeholder in this way you can  change the order


full_name = 'Mr. {first_last_name} {name} {second_last_name}...'.format(
    name = name,
    first_last_name = last_name, 
    second_last_name ='Silva')
print(full_name)
