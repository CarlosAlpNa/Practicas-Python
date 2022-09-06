#Capítulo 28
x = 1

while x <= 10:
	print(x)
	if x == 5:
		break
	x += 1

else:
    print("Salio del bucle while")

x = 0
while x < 10:
    x+=1
    if x == 5 or x == 7: #if con el continue, hacen que se salte la ejecución cuando x vale 5 y cuando vale 7.
        continue
    print(x)
#Ejercicio capitulo 28
print("Crear un bucle while con algunas caracteristicas especiales")
x = 0
                              
while x <= 30: # while se ejecuta hasta menor o igual que 30
	x += 1  # incrementos de 1

	if x == 4 or x == 6 or x == 10:# if para saltar ejecuciones del bucle
		print("Se saltó el valor ", x, " de x")
		continue
	
	if x == 15:# if para romper la ejecución del bucle
		print("Se rompió la ejecución del bucle cuando x valía: ", x)
		break

	print(x)# imprime los resultados que no se corresponden a ninguno de los if