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
    print("Agrupación de personas, animales o cosas considerados como un todo homogéneo, sin distinguir sus partes.")
    print("Un ejemplo de esto seria una agrupacion de numeros reales")
    print("{0,1,2,3,4,5,6,7,8,9}")


def accion2():
    print('Has elegido la opción 2')
    print('1.1.2.El conjunto universal y el conjunto vacío.')
    print("Conjunto universal:\nUn conjunto universal es un conjunto formado por todos los objetos de estudio en un contexto dado.\nPor ejemplo, en aritmética los objetos de estudio son los números naturales, por lo que el conjunto universal \npara este caso puede ser el conjunto de los números naturales N. Al conjunto universal también se le denomina \nconjunto referencial, universo del discurso o clase universal, según el contexto, y se denota habitualmente por U o V.")
    print("Conjunto vacío:\nEl conjunto vacío es el conjunto que no contiene ningún elemento. Puesto que lo único que define a un \nconjunto son sus elementos, el conjunto vacío es único.")
    print("Ejemplo de un conjunto universal:\nU = {1, 2, 3, 4, 5, …} ")
    print("Ejemplo de un conjunto vacio\n{         }")



def accion3():
    print('Has elegido la opción 3')
    print('1.1.3.Definición de conjuntos por extensión y por comprensión.')
    print("Por Extensión o Forma Tabular: Un conjunto se determina por extensión, o sea por enumeración, cuando se listan los elementos del conjunto.")
    print("Un Conjunto por extensión es básicamente la forma más común que utilizan las personas a la hora de escribir un conjunto, de hecho, es la forma que más fácil podemos identificar y comprender.")
    print("V = {Andrés, Oliver, Juan}\nP = {Canadá, Estados Unidos, México}")
    print("Por comprensión o Forma Constructiva: Un conjunto se determina por comprensión, cuando se da una propiedad, que la cumplan todos los elementos del conjunto.")
    print("En Matemática se dice que un conjunto se define por comprensión, cuando se mencionan las características comunes de sus \nelementos, sin nombrarlos uno por uno. (se busca una frase que represente a la totalidad de elementos sin \nnombrar a ninguno en particular)")
    print("A = {Números dígitos}\nB = {Números pares}")

def accion4():
    print('Has elegido la opción 4')
    print('1.2.Operaciones con conjuntos.')
    print("Las operaciones con conjuntos también conocidas como álgebra de conjuntos, nos permiten realizar operaciones sobre los \nconjuntos para obtener otro conjunto. De las operaciones con conjuntos veremos las siguientes unión, intersección, \ndiferencia, diferencia simétrica y complemento")


def accion5():
    print('Has elegido la opción 5')
    print('1.2.1.lgualdad de conjuntos.')
    print("Decimos que dos o más conjuntos son iguales si dichos conjuntos tienen los mismos elementos. Recuerda que para determinar \nla igualdad de conjuntos no importa el orden de sus elementos. Tampoco importa si los elementos están repetidos")
    print("Ejemplo de esto es:\nConjunto 1 ={0,1,2,3,4,5,6,7,8,9}\nConjunto 2 ={8,0,9,3,4,6,1,7,2,5}")


def accion6():
    print('Has elegido la opción 6')
    print('1.2.2.Subconjunto y superconjunto.')
    print("Subconjuntos: Se da cuando todos los elementos de un conjunto pertenecen al otro. El conjunto de los seres vivos es muy \ngrande: tiene muchos subconjuntos, por ejemplo: Las plantas son un subconjunto de los seres vivos. Los animales son \nun subconjunto de los seres vivos.")
    print("Superconjunto: Es un conjunto que incluye todos los elementos (y posiblemente más) de otro conjunto. ")


def accion7():
    print('Has elegido la opción 7')
    print('1.2.3.Unión, Intersección, complemento, diferencia y diferencia simétrica.')
    print("Unión: Es la operación que nos permite unir dos o más conjuntos para formar otro conjunto que contendrá a todos los \nelementos que queremos unir, pero sin que se repitan")
    print("Dados dos conjuntos A={1,2,3,4,5,6,7,} y B={8,9,10,11} la unión de estos conjuntos será A∪B={1,2,3,4,5,6,7,8,9,10,11}.")
    print("Intersección: Es la operación que nos permite formar un conjunto, sólo con los elementos comunes involucrados en la operación.")
    print("Dados dos conjuntos A={1,2,3,4,5} y B={4,5,6,7,8,9} la intersección de estos conjuntos será A∩B={4,5}.")
    print("Complemento: Es la operación que nos permite formar un conjunto con todos los elementos del conjunto de referencia o universal, \nque no están en el conjunto. Es decir, dado un conjunto A que está incluido en el conjunto universal U, entonces \nel conjunto complemento de A es el conjunto formado por todos los elementos del conjunto universal, pero sin considerar a los elementos que pertenezcan al conjunto A.")
    print("Dado el conjunto Universal U={1,2,3,4,5,6,7,8,9} y el conjunto A={1,2,9}, el conjunto A' estará formado por los siguientes elementos A'={3,4,5,6,7,8}.")
    print("Diferencia: Es la operación que nos permite formar un conjunto, en donde de dos conjuntos el conjunto resultante es el que tendrá \ntodos los elementos que pertenecen al primero pero no al segundo.")
    print("Dados dos conjuntos A={1,2,3,4,5} y B={4,5,6,7,8,9} la diferencia de estos conjuntos será A-B={1,2,3}.")
    print("Diferencia simétrica: Es la operación que nos permite formar un conjunto, en donde de dos conjuntos el conjunto resultante es el \nque tendrá todos los elementos que no sean comunes a ambos conjuntos.")
    print("Dados dos conjuntos A={1,2,3,4,5} y B={4,5,6,7,8,9} la diferencia simétrica de estos conjuntos será A △ B={1,2,3,6,7,8,9}.")

cadena ={0,1,2,3,4,5,6,7,8,9}
def accion8():
    print('Has elegido la opción 8')
    print('1.3.Funciones.')
    print("Una función es una regla de correspondencia entre dos conjuntos de tal manera que a cada elemento del primer conjunto le corresponde \nuno y sólo un elemento del segundo conjunto.\nAl primer conjunto se le da el nombre de dominio. \nAl segundo conjunto se le da el nombre de contra dominio o imagen.")
    print(f"Por ejemplo para {cadena} haremos una funcion")
    for cadena_mas in cadena:
        cadena_mas = cadena_mas+10
        print(f"El valor inicial de {cadena_mas - 10} ahora tiene un valor de {cadena_mas}")
    print("Ahora cada valor del dominio tiene una imagen o contra Dominio")    
      

def accion9():
    print('Has elegido la opción 9')
    print('1.3.1.Producto cartesiano.')
    print("El producto cartesiano de dos conjuntos es una operación, que resulta en otro conjunto, cuyos elementos son todos los pares ordenados \nque pueden formarse de forma que el primer elemento del par ordenado pertenezca al primer conjunto y el segundo \nelemento pertenezca al segundo conjunto")
    print("Por ejemplo, dado los conjuntos A={1,2,3,4} y B={a,b}\nSu producto cartesiano de A por B es:\n A X B = {(1,a),(1,b),(2,a),(2,b),(3,a),(3,b),(4,a),(4,b)}")

cadena2 ={0,9,3,6,1,7,8,12,84,132,8904}
def accion10():
    print('Has elegido la opción 10')
    print('1.3.2.Relaciones.')
    print("Las relaciones de conjuntos suceden cuando existen ciertos conjuntos que tiene algo en común y que cumplen una propiedad específica en \ncomún o como también puede ser por el número de elementos que pueden tener los conjuntos que queremos comprar. \nLa relación de conjuntos no es más que una comparación entre conjuntos según las cualidades que le asignemos, si es que existen.")
    print(f"Por ejemplo los elementos que tienen en comparten algunos conjuntos como puede ser el conjunto {cadena} y {cadena2} en cuyo caso es {cadena.intersection(cadena2)}")


def salir():
    print('Saliendo, bye bye :)')


if __name__ == '__main__':
    menu_principal()