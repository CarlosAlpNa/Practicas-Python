#Capitulo 32
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}
consulta = teclado1.get('Modelo'), teclado1['Precio'], teclado2['Modelo'], teclado2['Precio'] #Tambien se puede usar el comando .get() para obtener los valores
print(consulta)
print(teclado1['Precio'])
print("Cambiemos ahora el precio")
teclado1['Precio'] = '85' #Se pueden modificar los calores de los diccionarios
print(teclado1['Precio'])
print("Primera forma de imprimirlo en un ciclo")
for x in teclado1:
    print(x)
print("Las categorias primero y luego sus valores de cada categoria para el primer teclado")
for x in teclado2.values():
    print(x)
print("Tambien se puede imprimir asi")
for x in teclado2:
    print(teclado2[x])

for x, y in teclado2.items():
    print(x,": ",y)
print("Con esto podemos imprimir tanto las categorias como sus valores")

#Ejercicios cap 32
print("\nEjercicio cap 32")
print("Itera el diccionario teclado1 con un solo bucle for")
for x in teclado1:
	print(x, '=', teclado1[x] + '.')
