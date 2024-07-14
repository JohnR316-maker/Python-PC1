#4) Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en pantalla la suma de
#  todos los enteros desde 1 hasta N. La suma de los N primeros enteros positivos puede ser calculada de la siguiente forma:
#n(n+1)/2

N = int(input("Introduce un número entero: "))
suma = N*(N+1)/2
print("La suma de los primeros números enteros desde 1 hasta " + str(N) + " es " + str(suma))
#Se hizo la prueba con N = 20