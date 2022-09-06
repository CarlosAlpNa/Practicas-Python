#Capitulo 29
print("Capitulo 29")
for x in "Python":
    print(x)


cursos = ['Python', 'JavaScript', 'COBOL', 'HTML']
for x in cursos:
	if x == 'COBOL':
		continue
	if x == 'HTML':
		break
	print(x)
for x in []:
	pass #Igual que while se pueden dejar bucles vacios
#Ejercicio cap 29
print("Crea un bucle for que itere la siguiente tupla y muestre una frase como esta en cada iteración: 'El color es: ' + color + '.'.")
colores = ('rojo','azul','verde','amarillo')

for x in colores:
	print("el color es: " + x + ".")
print("\n")


#Capítulo 30
print("Capitulo 30")
for x in range(10):
	print(x)
else:
	print("Se acabo el bucle for...")
for x in range(5,10):
	print(x)

numeros = [2,4,8,16,32,64,128]
for x in range(len(numeros)):
	print("Número de operacion: ", x," Multiplicacion: ", numeros[x], "Resultados: ", numeros[x] * numeros[x])
#Ejercicio capitulo 30
print("Crea un bucle for con un range() que vaya desde el valor 7 hasta el valor 700 en saltos de 100. Basta con que imprimas el valor de cada iteración.")
for x in range(7, 700, 100):
	print(x)
print("\n")


