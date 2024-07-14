# 7) Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:
# - Mostrar una suma de los dos números 
# - Mostrar una resta de los dos números (el primero menos el segundo) 
# - Mostrar una multiplicación de los dos números 
# - En caso de introducir una opción inválida, el programa informará de que no es correcta

# Solución:
#  Sean las variables n1 y n2

n1 = float(input("Introduce un número: ") )
n2 = float(input("Introduce otro número: ") )
opción = 0        
print("¿Qué operación quieres hacer? \n1) Sumar los dos números\n2) Restar los dos números\n3) Multiplicar los dos números")
opción = int(input("Introduce un número: ") )     

if opción == 1:
    print("La suma de",n1,"+",n2,"es",n1+n2)
elif opción == 2:
    print("La resta de",n1,"-",n2,"es",n1-n2)
elif opción == 3:
    print("El producto de",n1,"*",n2,"es",n1*n2)
else:
    print("Opción incorrecta")