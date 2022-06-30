lista_cursos = ['Python','Django','Flask','Ruby','Java','Rust']
#                   01      1       2       3       4       5
# Conocer el tamaño de la lista
print(len(lista_cursos))
#Add a new element to the list (at the end)
lista_cursos.append('MongoDB')
lista_cursos.append('C#')
lista_cursos.append('JavaScript')

print(len(lista_cursos))
print(lista_cursos)

#Ad a new element by index

lista_cursos.insert(1,'Rails')
lista_cursos.insert(0,'PyGame')
print(lista_cursos)


#How to extend our lists?

lista_cursos_2 = ['C','C++','Docker']
lista_cursos.extend(lista_cursos_2) #Todos los elementos de la nueva lista se agregan en la lista anterior
print(lista_cursos)

#Remover un elemento de la lista

lista_cursos.remove('MongoDB')
print(lista_cursos)


#Otra forma de eliminar elementos, es utilizar los indices mediante la palabra reservada Del

del lista_cursos[0]
print(lista_cursos)

#Eliminar utilizando el ultiumo indice


del lista_cursos[-1]
print(lista_cursos)

#Vaciar las listas
lista_cursos.clear()
print(len(lista_cursos))
print(lista_cursos)






