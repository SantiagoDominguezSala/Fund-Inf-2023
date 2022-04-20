##Desafio IV 
##Manipulacion de archivos
archivo = "/Users/lucho/Desktop/Informatica/Fundamentos_de_informatica-master/Python_intro/manipulacion_archivos.txt"
with open(archivo, "r") as archivo:
    for linea in archivo:
        print(linea)