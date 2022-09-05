#Capitulo 10
smartphones = ['Xiaomi', 'Iphone', 'Huawei', 'Samsung']
print(smartphones)
lista1 = ['texto', 10, 55.8, 'texto']
smartphones = ['Xiaomi', 'Iphone', 'Huawei', 'Samsung']
print(smartphones[0])
print(smartphones[1])
print(smartphones[2])
print(smartphones[3])

#Ejercicos cap 10
colores = ["rojo", "azul", "verde", "amarillo", "marrón", "lila", "negro", "rosa"]
print(f"En la posicion 3 esta el color: {colores[3]}")

print(f"El color {colores[0]} es la posicion 0 y el {colores[7]} en la posicion 7" )

numlist = ["tres", "dos", "cinco", "cuatro", "uno"]
print(numlist)
print("\n")
#Capitulo 11
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila','negro', 'rosa','blanco', 'naranja']
print(f"Vamos a imprimir un color pero ahora desde si valor negatio {colores[-1]}")
#Ejercicios cap 11
print(f"Vamos a acceder a los siguientes colores desde su posicion negativa {colores[-1]} el que sigue {colores[-7]} y asi vamos por mas {colores[-5]} otro mas {colores[-7]} y ya el ultimo {colores[-10]} ")
print("\n")

#Capitulo 12
hardware = ["Case", "Motherboard", "HDD", "SSD", "CPU", "Graphics card", "RAM", "Power supply"]
del hardware[0]
print(hardware)
del hardware[6]
print(hardware)
del hardware[-2]
print(hardware)
#Ejercicio cap 12
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

#Eliminar de la lista los colores azul, marron, negro, rosa
del colores[1]
del colores[3]
del colores[4]
del colores[-3]
print(colores)
print("\n")

#Capitulo 13
hardware = ["Case", "Motherboard", "HDD", "SSD", "CPU", "Graphics card", "RAM", "Power supply"]
hardware.remove("CPU")
hardware.remove("HDD")
print(hardware)
#Ejercicios cap 13
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print(colores)
colores.remove('amarillo')
colores.remove('rojo')
print(colores)
print("\n")

#Capitulo 14
colores = ['rojo', 'azul', 'verde', 'amarillo']
guardaLista = colores.pop(0)
print(colores)
print("El color eliminado de la lista y guardado es el: " + guardaLista)
#Ejercicios cap 14
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print(f"Lista completa:{colores}" )
colorEl1 = colores.pop(1)
colorEl2 = colores.pop(7)
colores_eliminados = [colorEl1, colorEl2]
print(colores_eliminados)
print("\n")