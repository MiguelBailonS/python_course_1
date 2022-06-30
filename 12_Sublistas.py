lista_cursos = ['Python','Django','Flask','Ruby','Java','Rust']
#                   01      1       2       3       4       5

sub_lista = lista_cursos[0:3]
print(sub_lista)

sub_lista = lista_cursos[1:4]
print(sub_lista)

#Error?
sub_lista = lista_cursos[1:100]
print(sub_lista)

#Obtener todos los elementos a partir del indice 1
sub_lista = lista_cursos[1:]
print(sub_lista)

#Obtener los primeros elementos de la lista hasta el indice final (4) No tendra en cuenta el indice 4
sub_lista = lista_cursos[:4]
print(sub_lista)

#Obtener los indices con saltos de dos en dos
sub_lista = lista_cursos[1:5:2]
print(sub_lista)

#Generar una sublista con todos los elementos
sub_lista = lista_cursos[:]
print(sub_lista)

#Generar una sublista con todos los elementos de dos en dos
sub_lista = lista_cursos[::2]
print(sub_lista)

#Generar una sublista con todos los elementos a la inversa
sub_lista = lista_cursos[::-1]
print(sub_lista)
