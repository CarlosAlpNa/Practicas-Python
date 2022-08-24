from __future__ import division
from cgi import print_arguments
from pickletools import float8


print("Operaciones Basicas")

suma = 1 + 2
resta = 55 - 3
multiplicacion = 2 * 5
division = 10 / 3

print(suma , resta, multiplicacion, division)

print("Ahora vamos con los exponentes\n")

exponente = 2 ** 5

print (exponente)

#Ahora con flotantes
 
print("Vamos a intenar ahora con flotantes")

float1 = 894.899891
float2 = 564.731167
print ("El valor de el primer flotante es: ")
print(float1)
print ("El valor de el segundo flotantes es:")
print(float2)
print("La suma de ambos valores es: ")
print(float1 + float2, )
print("Muchos decimales no? vamos a redondear")
print(round(float1 + float2, 2))