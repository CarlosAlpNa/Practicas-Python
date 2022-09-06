#Capitulo 10
from asyncio import CancelledError
from traceback import print_tb


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
print(f"Lista despues de elimiar algunos elementos:{colores}" )
colores_eliminados = [colorEl1, colorEl2]
print(f"Los elementos eliminados son: {colores_eliminados}")
print("\n")

#Capitulo 15
colores = ['rojo', 'azul', 'verde', 'amarillo']
print(f"La lista es:{colores} y le vamos a agregar un color mas en este caso el naranja")
colores.append('naranja')
print(f"Despues de agregarlo quedo:{colores}")
#Ejercicios cap 15
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print([f"Tenemos la lista{colores} y vamos a agregar nuevos colores a la misma en este caso fuxia y celeste"])
colores.append('fuxia')
colores.append('celeste')
print(f"Despues de agregarle los colores la lisa se ve asi:{colores}")
print("\n")

#Capitulo 16
print(f"Ahora podemos espesificar en que lugar podemos agregar los nuevos valores")
colores = ['rojo', 'azul', 'verde', 'amarillo']
print(colores)
print("Ahora agregemos el valor naranja en algun lugar")
colores.insert(-2,'naranja')
print(f"Despues de agregarle el color a la lisa se ve asi:{colores}")
#Ejercicios cap 16
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print(f"Como ejercicio vamos a agregar  los colores 'magenta' y 'turquesa' utilizando insert(). en la cadena que ya tenemos {colores}")
colores.insert(-4, 'magenta')
colores.insert(-1, 'turquesa')
print(f"Despues de agregarle los colores la lisa se ve asi:{colores}")
print("\n")

#Capitulo 17
colores = ['rojo', 'azul', 'verde', 'amarillo']
print(f"Vamos a acomodar la lista por orden alfabetico:{colores}")
print(f"Ya ordenada queda asi:")
print(sorted(colores))
print("Que tal si ahora la ordenamos alfabeticamente pero al revez")
print(f"Ya ordenada queda asi:")
colores.sort(reverse=True)
print(colores)
#Ejercicios cap 17 
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón','lila', 'negro', 'rosa', 'blanco', 'naranja']
print(f"Vamos a ordenar la la lista {colores} \nen orden alfabético descendente (de la letra 'z' a la 'a'). ")
colores.sort(reverse=True)
print(f"Vemoas como quedo: {colores}")
print("\n")

#Capitulo 18
print(f"Ahora vamos a contar los elementos de la lsitas, tenemos las lista de colores {colores}")
print("Como se puede observar son muchos elemnetos para contarlos manualmente por que no mejor que lo haga la maquina")
CanColores = len(colores)
print (CanColores)
print("Como podemos observar la maquinas nos ha dicho el numeros de elemntos que estan dentro de la lista y asi podemos guardarlo en una variable para un futuro uso")