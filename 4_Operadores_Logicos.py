#And
resultado_final = True and True
print(resultado_final)

resultado_final = True and True and False
print(resultado_final)

resultado_final = True and True and (10 > 20)
print(resultado_final)

resultado_final = True and True and (100 > 20)
print(resultado_final)

#Or

resultado_final = False and False and (100 > 20)
print(resultado_final)

resultado_final = False and False and (10 > 20)
print(resultado_final)

resultado_final = True and (False or 5>10)
print(resultado_final)

resultado_final = True and (False or 50 > 10)
print(resultado_final)



#Not

resultado_final = not True
print(resultado_final)

resultado_final = not False
print(resultado_final)

