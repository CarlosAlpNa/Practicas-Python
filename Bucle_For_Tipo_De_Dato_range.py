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