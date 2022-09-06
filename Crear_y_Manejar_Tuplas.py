#Capitulo 19
lista = ['rojo', 'azul', 'verde', 'amarillo']
tupla = ('rojo', 'azul', 'verde', 'amarillo')
print("Vamos a ver las diferencias entre imprinmir una lista y una tupla lo primero que se imprimira sera una lista y luego la tupla")
print(lista)
print(tupla)
print("A su vez la tupla puede guardar diferentes tipos de fatos y hacer operaciones con ellos")
tupla2 = (10, 15, 20, 'El resultado de la operación es:')
print(tupla2[3], tupla2[2] + tupla2[0] * tupla2[1] / tupla2[0])
#Ejercicos cap 19
colores = ('rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja')
print(f"Vamos a hacer algunas ejercicios\nImprime la segunda posición de esta tupla {tupla}")
print(tupla[1])
numeros = (10, 1, 5, 11)
print(f"Utiliza los símbolos de suma y resta para obtener el resultado 25 a partir de los elementos de la siguiente tupla {numeros} en una variable llamada operacion.")
operacion = numeros[0] + numeros[2] + numeros[3] - numeros[1]
print(operacion)
print("\n")

#Capitulo 20
print("Cómo convertir tuplas a listas y viceversa")
lista = ['rojo', 'azul', 'verde', 'amarillo']
tupla = tuple(lista)
print(tupla)
print("Ahora probemos lo contrario")
tuplas = ("rojo", "azul", "verde", "amarillo")
lista = list(tupla)
print(lista)
#Ejercicios cap 20
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print(f"Intentemos algun ejercicio\nConvierte la siguiente lista {colores} en una tupla y asegúrate que se haya convertido en tupla correctamente imprimiendo en la consola el tipo de elemento que es.")
coltupla = tuple(colores)
print(type(coltupla))#Al poner type() nos ayuda a imprimir el tipo de variable es la que imprimimos
print("\n")



