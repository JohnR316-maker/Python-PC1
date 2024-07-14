#2) En los Estados Unidos, se acostumbra a dejar una propina a su mesero después de cenar en un restaurante, generalmente una 
# restaurante cantidad igual al 15% o más del costo de su comida. Escriba un programa que pregunte al usuario cuánto
# fue su consumo y que porcentaje de propina desea dejar al mesero. Su programa debe devolver la cantidad de dinero a dejar 
#como propina

comida=float(input("Costo de comida: $"))
porcentaje_propina=float(input("Porcentaje de propina: "))
valor_propina=(porcentaje_propina*comida)/100
print("Valor de propina: $", valor_propina)
#Se hizo la prueba con Comida = $ 150 , Porcentaje de propina =15%