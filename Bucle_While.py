#Capitulo 27
x = 1

while x < 10:
    print(x)
    x += 1
print("Final primer ciclo")
x = 9
while x > 0:
	print(x)
	x -= 2
print("Final segundo ciclo")

frase = "Lo que escribas, lo repito:"
frase += "\nIntroduce el comando 'salir' para finalizar el programa \n"
mensaje = ""
while mensaje != "salir":
    mensaje = input(frase)
    print(mensaje)
#Ejercicios cap 27
print("Veamos unos ejercicios")
print("Crea un bucle while que se ejecute hasta que x valga 15 con incrementos de 5.")
x = 0
while x <= 15:
	print(x)
	x += 5
print("Crea un bucle while que se ejecute hasta que x valga -100 con decrementos de 20.")    
x = 0
while x >= -100:
	print(x)
	x -= 20
print("rea un bucle while que se ejecute hasta que x valga 0 con decrementos de 1 y que muestre en cada ejecución esta frase con el valor de ejecución correspondiente: 'El valor del bucle es 10'...")
x = 10

while x >= 0:
	print('El valor de x es: ', x)
	x -= 1

