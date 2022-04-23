from binhex import FInfo
from math import modf


s4b = input("Como es tu primer apellido:")
s4c = input("Como es tu segundo apellido:")
print (str.upper(s4a[0] + s4b[0] + s4c[0]))

#Ejercicio 5#
#Realizar un programa que lea tres números por teclado y calcule el promedio de ellos.
s5 = input("3 numeros:")
suma = (int(s5[0]) + int(s5[2]) + int(s5[4])) / 3
print (suma)

#Ejercicio 6#
#Dada una cierta cantidad de minutos (ingresada por teclado) hacer un programa que muestre cuántas horas y minutos son. Por ejemplo 150 minutos son 2 horas y 30 minutos.
s6 = input("Minutos:")
horas = (int(s6) // 60)
minutos = int(s6) - (int(horas) * 60) 
print (("Horas: ") + str(horas) + " y Minutos: " + str(minutos))

#Ejercicio 7#
#Un comerciante, el cual tiene un sueldo base, recibe un 10% extra por comisión por cada venta que realiza. Realizar un programa que devuelva el dinero que recibirá por comisión luego de 4 ventas y el total de dinero que ganará ese mes, teniendo en cuenta estas ventas y su sueldo base.
s7a = input("Sueldo base: ")
s7b = input("Venta: ")
Fin_de_mes = int(s7a) + (int(s7b) * 0.10)
print (Fin_de_mes)

#Ejercicio 8#
#Escribir un programa para calcular la nota final de un estudiante, teniendo en cuenta que por cada respuesta correcta el estudiante suma 4 puntos, por cada incorrecta se le resta 1 punto y si la respuesta está en blanco no se le suma ni se le resta.
s8 = [input("Respuesta 1: "), input("Respuesta 2: "), input("Respuesta 3: ")]
nota = 0
for respuesta in s8:
    if respuesta == 'Correcta':
        nota += 4
    elif respuesta == 'Incorrecta':
        nota += 1
    elif respuesta == '':
        nota
print(nota)

