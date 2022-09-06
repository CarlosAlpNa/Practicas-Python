
#Capítulo 21



print("Operadores de comparación en Python")
num1 = 10
num2 = 20 #Aqui debemos de cambiar manualmente los valores de los numeros para ver que condicionales se activan
if num1 == num2:
    print("los dos Numeros son iguales")

if  num1  > num2: 
    print("El numero 1 es Mayor que el numero 2")

if  num1  < num2: 
    print("El numero 1 es Menor que el numero 2") 

if num1   >= num2:
    print("El numero 1 Mayor o igual qué 2")

if num1   <= num2:
    print("El numero 1 Menor o igual qué el numero 2")

if num1   != num2:
    print("El numero 1 Diferente qué el numero 2 ")  

#Ejercicios cap 21
print("Vamos a poner en practica algunos condicionales")
num1 = 15
num2 = 20
if num1 != num2:
	print("Se hace verdad la condicion")
num1 = 1450
num2 = 60
if num1 >= num2:
	print("Se hace verdad la condicion")
num1 = 60
num2 = 60
if num1 != num2:
	print("Se hace verdad la condicion")
print("Con eso vemos algunos usos de los condicionales")
print("\n")

#Capitulo 22
print("El condicional IF ELSE")
edad = 20
if edad >= 18:
    print("Puedes acceder, eres mayor de edad")
else:
    print("No puedes accede, eres menor de edad")    
#Ejercicios cap 22
print("Vamos con algun ejercicio") 
color = "rojo"
if color != "rojo":
    print ("El color no es rojo.")
else:
    print("El color es rojo.")
print("Como pudimos ver el codigo corre con normalidad lo cual nos idica que ya no hay ningun arror que arreglar")
print("\n")

#Capitulo 23
print("El condicional if elif else e input, entrada de datos")
edad = int(input("¿Cuál es tu edad?\n"))
if edad <= 0:
	print("Nadie puede tener esa edad.")
elif edad <= 1 and edad < 18:
	print("Eres menor de edad.")
elif edad <= 100:
	print("Eres mayor de edad.")
else:
	print("Edad no válida.")
#Ejercicio capitulo 23
print("Ahora agregaremos mas rangos de edad") 
edad = int(input("¿Cuál es tu edad?\n"))
if edad <= 0:
	print("Nadie puede tener esa edad.")
elif edad <= 1 and edad < 18:
	print("Eres menor de edad.")
elif edad == 18 and edad <= 45:
	print("Eres mayor de edad y en buena edad.")
elif edad <= 100:
	print("Eres mayor de edad.")
elif edad > 100 and edad <= 120:
	print("Eres muy mayor, cuidado al bajar las escaleras")
else:
	print("Edad no válida.")
    
print("\n")


