#Capitulo 24
print("Comprobar datos en listas y tuplas")
navegadores = ['chrome', 'firefox', 'opera', 'safari']
print("chrome en la lista?")
print("chrome" in navegadores)
print("edge en la lista?")
print('edge' in navegadores)

entrada = input("Introduce el nombre de un navegador:\n")
if entrada in navegadores:
    print("El navegador que buscas esta en la lista")
else:
    print("El navegador que buscas no esta en la lista")
#Ejercicio cap 24
print("Vamos con el ejercicio")
print("Haz una tupla que contenga cuatro colores de tu elección. Tendrás que poner una condición con el condicional if para cada color que le avise al usuario que el color está en la tupla con un mensaje como este: print('El color rojo está admitido') y una condición False para contemplar cualquier color que no esté en la tupla con un mensaje como este: print('Color no admitido'). No puedes utilizar el operador ==. Además tendrás que hacer esto con un input() que permita introducir un color al usuario.")
colores = input("Introduce un color:\n")
tupla_colores = ('rojo', 'azul', 'verde', 'amarillo','morado','cafe')

if colores in tupla_colores[0]:
	print("El color rojo está admitido")
elif colores in tupla_colores[1]:
	print("El color azul está admitido")
elif colores in tupla_colores[2]:
	print("El color verde está admitido")
elif colores in tupla_colores[3]:
	print("El color amarillo está admitido")
elif colores in tupla_colores[4]:
	print("El color morado está admitido")    
elif colores in tupla_colores[5]:
	print("El color cafe está admitido")    
else:
	print("El color no esta el la tupla")

