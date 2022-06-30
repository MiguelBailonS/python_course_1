lista = [8,90,1,5,44,132,600,3,4]

# Ordenar una lista
# Utilizar un algoritmo de alineamiento
# O utilizar la funcion sort

lista.sort() #Ordenar la lista de menor a mayor
print(lista)

lista.sort(reverse = True) #Ordenar la lista de mayor a menor
print(lista)

#Imprimir numero mayor
lista.sort()
print(lista[0]) #numero menor
print(lista[-1]) #numero mayor

#Otra forma de obtener el numero menor y mayor

print(min(lista))
print(max(lista)) 

#Expreson booleana con la palabra reservada 'In'

print(10 in lista)
print(5 in lista)

#Si deseamos negar la sentencia

print(11 not in lista)
print(8 not in lista)