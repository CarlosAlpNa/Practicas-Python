#Capitulo 25
print("Saludos gerrero que deseas comprar?\n\n"+
"Intems disponibles: \n\n"+ "Espadas:\n\n1-Espada Nivel 1: 150 Monedas de oro.\n2-Espada Nivel 2: 1200 Monedas de oro. \n\nEscudos:\n\n3-Escudo Nivel 1:100 Monedas de oro\n4-Escudo Nivel 2:750 monedas de oro\n ")

comprar = [3,1]
dinero = 1500
Espadalv1= 150
Espadalv2= 1200
Escudolv1= 100
Escudolv2= 750

if 0 in comprar or comprar == []:
    print("Elige una de los 4 objetos")
if 1 in comprar:
    dinero = dinero - Espadalv1
if 2 in comprar:
    dinero = dinero - Espadalv2
if 3 in comprar:
    dinero = dinero - Escudolv1
if 4 in comprar:
    dinero = dinero - Escudolv2

else:
        print("Elige una de los 4 objetos") 
if dinero < 0:
       print("Fondos insificientes para tu compra")
if comprar == [1] or comprar == [2] or comprar == [3]  or comprar == [4]:
    print("Te quedan " + str(dinero)+ " Monedas de oro")  
    print("se añado el/los objeto/s a tu inventario")                   

