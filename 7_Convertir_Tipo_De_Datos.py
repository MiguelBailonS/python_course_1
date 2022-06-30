nombre_completo = input('Ingresa tu nombre completo: ')

edad = input('Ingresa tu edad: ')

edad = int(edad)

#print(edad)
#print(type(edad))

altura = input('Ingresa tu altura: ')
altura = float(altura)

#print(altura)
#print(type(altura))

autorizacion = input('Autorizas el programa? Y/N ')
autorizacion = autorizacion == 'Y'

print(autorizacion)



#Otra forma de hacerlo

nombre_completo = input('Ingresa tu nombre completo: ')
edad = int(input('Ingresa tu edad: '))
altura = float(input('Ingresa tu altura: '))
autorizacion = input('¿Autorizas el programa? Y/N ') == 'Y'

print(nombre_completo)
print(edad)
print(altura)
print(autorizacion)