# 12)Implemente un programa que solicite al usuario el nombre de un archivo y luego genere el tipo de archivo MIME correspondiente.
# si el nombre del archivo termina en cualquiera de estos sufijos (sin importar el uso de mayúsculas y minúsculas): 
# - .gif 
# - .jpg
# - .jpeg
# - .png
# - .pdf
# - .txt
# - .zip 
# Si el nombre del archivo termina con algún otro sufijo que no se encuentra en la lista o no tiene ningún 
# sufijo, en su lugar su programa deberá devolver application/octet-stream.

nombre_archivo = input("Ingrese el nombre del archivo": ”)
# main.py
partes_nombre_archivo  = nombre_archivo.split(",")
print(partes_nombre_archivo)
print(partes_nombre_archivo[-1])