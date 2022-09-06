#Capitulo 31
print("¿Qué son los diccionarios de Python?")
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
consulta = teclado1['Modelo'], teclado1['Precio'], teclado2['Modelo'], teclado2['Precio']
print("Muestra los modelos y los precios")
print(consulta)
print("Muestra todos los detalles del teclado 1")
muestraTeclado = dict(teclado1)
print(muestraTeclado)
#Ejercicio Cap 31
print("Del diccionario teclado2 del capítulo, muestra los elementos Modelo y Precio con presentación en un print(). El resultado será esto en la consola:'El modelo Corsair K55 RGB cuesta 59,99 $.'")
print('El modelo', teclado2['Modelo'], 'cuesta', teclado2['Precio'], '$.')

