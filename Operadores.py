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

#Vamos con los ejercicios 
#Cap 7
sumaEjr = 20 + 23 + 44
print("Veamos si el resultado es el que pide el ejercicio", + sumaEjr  )

restaEjr = 20 - 23 - 84
print("Veamos si el resultado es el que pide el ejercicio", + restaEjr  )

mulEjr = 10 * 87
print("Veamos si el resultado es el que pide el ejercicio", + mulEjr  )


divEjr = 5000 *  230 / 115000
print("Veamos si el resultado es el que pide el ejercicio", + divEjr  )


opEjer = 10 / 5 + 15 - 17
print("Veamos si el resultado es el que pide el ejercicio", + opEjer  )

#Cap 8
op1024 = 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2
print("Veamos si el resultado es el que pide el ejercicio", + op1024  )

print("Vamos a redondear 17.567383292929200234 para tener solo 5 decimales", + round(17.567383292929200234, 5))