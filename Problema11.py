# 11) Escriba un programa Python que se encargue de eliminar los elementos duplicados de la siguiente lista. Su programa 
# debe retornar otra lista sin los duplicados.
# Lista original: [1, 1, 2, 3, 4, 4, 5, 1]
# Lista procesada: [1, 2, 3, 4,, 5]

lista1=[1, 1, 2, 3, 4, 4, 5, 1]  #Original
lista2=[]                        #Procesada

lista2=lista1[1:5]
for i in range(len(lista1)):
    if lista1 [i] not in lista2:
     lista2.append(lista1[i])
     print(lista2)