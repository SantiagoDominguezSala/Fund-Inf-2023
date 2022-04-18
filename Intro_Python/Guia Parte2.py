#Ejercicio 1
# Creá un programa que lea una cadena por teclado y compruebe si la primer letra es mayúscula o minúscula.

s1 = input("Mayuscula o Minuscula?: ")

if str.upper(s1[0]) == s1[0]:
    print ("Mayuscula")
elif str.lower(s1[0]) == s1[0]:
    print("Minuscula")

#Ejercicio 2
# Escribí un programa que pida un número y diga si es positivo, negativo o 0 y además informe si es par o impar (el 0 es un número par).

s2 = input("Numero: ")

if (int(s2) % 2) == 0:
    print ("Par")
elif int(s2) % 2 == 1:
    print ('Impar')

if int(s2) == 0:
    print ("0") 
elif int(s2) > 0:
    print ("Positivo")
elif int(s2) < 0:
    print ("Negativo")

#Ejercicio 3
#Escribí un programa que dado un número del 1 al 6, ingresado por teclado, muestre cuál es el número que está en la cara opuesta de un dado. 
# Si el número es menor a 1 y mayor a 6 se debe mostrar un mensaje indicando que es incorrecto el número ingresado.

s3 = input('Dado: ')

if s3 == "1":
    print(6)
elif s3 =="2":
    print (5)
elif s3 =="3":
    print(4)
elif s3 =="4":
    print(3)
elif s3 =="5":
    print (2)
elif s3 =="6":
    print (1)
else:
    print ("Incorrecto el numero ingresado")

#Ejercicio 4
#Una compañía de transporte internacional tiene servicio en algunos países de América del Sur, América Central, América del Norte, Europa y Asia. 
# El costo por el servicio de transporte se basa en el peso del paquete y la zona a la que va dirigido, tal como se muestra en la tabla:

#Zona	Ubicación	        Costo/gramo
#1	América del Sur	        10.00 dólares
#2	América Central	1       5.00 dólares
#3	América del Norte	    18.00 dólares
#4	Europa	                24.00 dólares
#5	Asia	                30.00 dólares

#Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, esto por cuestiones de logística y de seguridad. 
#Realizá un programa para determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega.

s4 = input("Zona: ")
s4a = input('Peso en kg: ')

if int(s4a) >= 5:
    print ("Rechazo de la entrega")
else:
    if s4 == "1":
        print (int(s4a) * 1000 * 10)
        print ("Dolares")
    elif s4 == "2":
        print (int(s4a) * 1000 * 5)
        print ("Dolares")
    elif s4 == "3":
        print (int(s4a) * 1000 * 18)
        print ("Dolares")
    elif s4 == "4":
        print (int(s4a) * 1000 * 24)
        print ("Dolares")
    elif s4 == "5":
        print (int(s4a) * 1000 * 30)
        print ("Dolares")

#Ejercicio 5
#Creá un programa que pida el número de día de la semana (del 1 al 7) e imprima el nombre correspondiente. 
#Si se ingresa un número fuera de rango tiene que imprimir un mensaje indicando que el número es incorrecto.

s5 = input("Numero de la semana: ")

if s5 == "1":
    print ("Lunes")
elif s5 == "2":
    print ("Martes")
elif s5 == "3":
    print ("Miercoles")
elif s5 == "4":
    print ("Jueves")
elif s5 == "5":
    print ("Viernes")
elif s5 == "6":
    print ("Sabado")
elif s5 == "7":
    print ("Domingo")
else:
    print ("Numero incorrecto.")

#Ejercicio 6
#Creá una lista e inicializala con 5 cadenas de caracteres leídas por teclado. 
#Copiá los elementos de la lista en otra lista pero en orden inverso, imprimí los elementos de esta última lista.

lista_cadena = []
lista_cadena_inversa = []

i = 4

while i >= len(lista_cadena):
    lista_cadena.append(input("Cadena de Caracteres: "))
    if i < len(lista_cadena):
        lista_cadena_inversa = (list(reversed(lista_cadena)))

print(lista_cadena_inversa)


#Ejercicio 7
#Creá un programa que declare una lista y la vaya llenando de números leídos por teclado hasta que se introduzca un número negativo. 
#Una vez hecho esto se deben imprimir los elementos de la lista.
listanumeros = []
numero = int(input("Escribe un numero: "))

while numero >= 0:
    listanumeros.append(numero)
    numero = int(input("Escribe un numero: "))
    if  numero < 0:
        print (listanumeros)
 
#Ejercicio 8
#Realizá un programa que declare tres listas lista1, lista2 y lista3, donde las dos primeras listas deben tener cinco enteros cada una, 
#ingresados por teclado y asigne para cada elemento de la lista3 la suma de los elementos de la lista1 y la lista2 
#(es decir, el primer elemento de la lista3 tiene que ser la suma del primer elemento de la lista1 y el primero de la lista2)



#Ejercicio 9
#Hacé un programa que guarde los nombres y la edades de los alumnos de un curso. 
# Se debe introducir el nombre y la edad de cada alumno por teclado. 
# El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*). Al finalizar se deben mostrar los siguientes datos:

# -La edad máxima de todos los alumnos.
# -Los alumnos que tengan la edad máxima

listanombres = []
listaedades = []

while True:
    nombre = input("Nombre: ")
    if nombre != "*":
        listanombres.append(nombre)
        listaedades.append(int(input("Edad: ")))
    if nombre == "*": break;
   
edad_max_alumnos = max(listaedades)

for nombre, edad in zip(listanombres, listaedades):
    if edad == edad_max_alumnos:
        print ("Alumno en edad maxima:", (nombre))
print ("Edad maxima es", (edad_max_alumnos))

#Ejercicio 10
#Escribí un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena 
#(considerar que las mayúsculas difieren de las minúsculas, 
#por lo que, si el string es "Agua", el carácter "A" tiene 1 aparición y el carácter "a" también tiene 1).

dic = {}

una_cadena = input("Cadena: ")
for caracter in una_cadena:
    if caracter in dic:
        dic[caracter] += 1
    else:
        dic[caracter] = 1
for letra, cantidad in dic.items():
    print (letra, cantidad)

#Ejercicio 11
#Modificá el programa anterior para que además imprima los caracteres que no aparecen en la cadena, pero con el valor 0.
dic = {}

alfabeto = "abcdefghijklmnopqrstuvwxyz"
for caracter in alfabeto + alfabeto.upper():
    dic[caracter] = 0

una_cadena = input("Cadena: ")

for caracter in una_cadena:
        if caracter.lower() in alfabeto:
            dic[caracter] += 1

for letra, cantidad in dic.items():
    print (letra, cantidad)

#Ejercicio 12
#Creá un programa que permita guardar los nombres de los alumnos de una clase y las notas que han obtenido. 
#Cada alumno puede tener distinta cantidad de notas.
# Guardá la información en un diccionario cuya claves serán los nombres de los alumnos y los valores serán listas con las notas de cada alumno.
# El programa tiene que pedir el número de alumnos que se va a introducir, luego su nombre y sus notas hasta que introduzcamos un número negativo.
# Al final el programa tiene que mostrar la lista de alumnos y la nota media obtenida por cada uno de ellos.
# Nota: si se introduce el nombre de un alumno que ya existe el programa tiene que dar un error.

#Ejercicio 13 
#Creá un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro creando la función esMultiplo.
n1 = input("Numero 1: ")
n2 = input("Numero 2: ")

def esMultiplo(n1, n2):
    if int(n1) % int(n2) == 0 or int(n2) % int(n1) == 0:
        return ("Es multiplo")
    else:
        return ("No es multiplo")

print (esMultiplo(n1, n2))

#Ejercicio 14
#Creá una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. 
# Escribí un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. 
# El programa tiene que pedir el número de días que se van a introducir.
    


