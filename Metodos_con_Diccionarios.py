#Capítulo 33
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
print(len(teclado1) + len(teclado2))

teclado2.pop('Categoría')
print(teclado1)

del teclado2['Precio']
print(teclado2)

print("Oborrar todo")
del teclado2
#print(teclado2) lo tenemos que poner como comentario por que nuna vez borrado el diccionario ya no se puede imprimir y da error 
teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}
teclado2.clear()
print("Con esto lo podemos limpiar pero no borara")
print(teclado2)
#Podemos agregar mas cosas al diccionarios
teclado1["Color"]= "Negro"
print(teclado1)
#Tambien podemos copiar diccionarios p