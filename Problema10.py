#10) Escriba un programa para imprimir una lista específica después de eliminar los elementos que se encuentran en la 
# posición 0, 4 y 5.
# lista de muestra: ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
# Resultado esperado: ['Verde', 'Blanco', 'Negro']

lista1=['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']  #Lista de muestra
lista2=[]                                                        #Resultado esperado

del lista1[0]
del lista1[3]
del lista1[3]
lista2=lista1[1:3]
for i in range(len(lista1)):
    if lista1 [i] not in lista2:
     lista2.append(lista1[i])
     print(lista2[::-1])