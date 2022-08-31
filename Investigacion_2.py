print("Investigacion 2")
print("El siguiente programa es la entrega de la investigacion 2 en la cual se desplegara un menu con diferentes opciones a modo de enciclopedia en el cual a travez de un menu seleccionara la informacion que desea visualizar\n\n")
print("Que informacion deseas visualizar?")
#Menu
def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in (opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('1.1.1.----Definición formal de conjunto.', accion1),
        '2': ('1.1.2.----El conjunto universal y el conjunto vacío.', accion2),
        '3': ('1.1.3.----Definición de conjuntos por extensión y por comprensión.', accion3),
        '4': ('1.2.------Operaciones con conjuntos.', accion4),
        '5': ('1.2.1.----lgualdad de conjuntos.', accion5),
        '6': ('1.2.2.----Subconjunto y superconjunto.', accion6),
        '7': ('1.2.3.----Unión, Intersección, complemento, diferencia y diferencia simétrica.', accion7),
        '8': ('1.3.------Funciones.', accion8),
        '9': ('1.3.1.----Producto cartesiano.', accion9),
        '10':('1.3.2.---Relaciones.', accion10),
        '11':('Salir', salir)
        
    }

    generar_menu(opciones, '11')

#Definiciones
def accion1():
    print('Has elegido la opción 1')
    print('1.1.1.Definición formal de conjunto.')


def accion2():
    print('Has elegido la opción 2')
    print('1.1.2.El conjunto universal y el conjunto vacío.')


def accion3():
    print('Has elegido la opción 3')
    print('1.1.3.Definición de conjuntos por extensión y por comprensión.')

def accion4():
    print('Has elegido la opción 4')
    print('1.2.Operaciones con conjuntos.')


def accion5():
    print('Has elegido la opción 5')
    print('1.2.1.lgualdad de conjuntos.')


def accion6():
    print('Has elegido la opción 6')
    print('1.2.2.Subconjunto y superconjunto.')


def accion7():
    print('Has elegido la opción 7')
    print('1.2.3.Unión, Intersección, complemento, diferencia y diferencia simétrica.')


def accion8():
    print('Has elegido la opción 8')
    print('1.3.Funciones.')


def accion9():
    print('Has elegido la opción 9')
    print('1.3.1.Producto cartesiano.')


def accion10():
    print('Has elegido la opción 10')
    print('1.3.2.---Relaciones.')


def salir():
    print('Saliendo, bye bye :)')


if __name__ == '__main__':
    menu_principal()