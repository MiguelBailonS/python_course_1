number_list = [1,2,3,4,5]

number_tuple = (10,20,30,40,50)

result = zip(number_tuple,number_list) #-> Type 'zip'
print(result)
print(type(result))

#Obtain a tuple from the result

result = tuple(result)

#The order is different due to the order in arguments in zip function
print(result)

result = zip(number_list,number_tuple) #-> Type 'zip'
result = tuple(result)
print(result)

#Add a new list
list_2 = [100,200,300,400,500]

result = zip(number_list,number_tuple,list_2) #-> Type 'zip'
result = tuple(result)
print(result)



#Add a new tuple

tuple_2 = (1000,2000,3000,4000,5000)
result = zip(number_list,number_tuple,tuple_2) #-> Type 'zip'
result = tuple(result)
print(result)
#What happen if the lengths are different?

tuple_3 = (100,200)
result = zip(number_list,number_tuple,tuple_3) #-> Type 'zip'
result = tuple(result)
print(result)
#The values that exceeded the minimun length of lists or tuples are omitted.
