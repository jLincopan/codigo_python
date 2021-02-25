ancho = 20
altura = 10

cuerpo_culebra = "[=]"
cabeza_culebra = "[>]"
espacio_vacio = "[ ]"
PANTALLA = []

def crearMatriz(caracter_inicial, ancho, altura):
    matriz = []
    for i in range(altura):
        columna = []
        for j in range(ancho):
            columna.append(caracter_inicial)
        matriz.append(columna)
    return matriz

def inicializarPantalla(ancho, altura):
    global PANTALLA
    PANTALLA = crearMatriz(espacio_vacio, ancho, altura)

def mostrarPantalla(PANTALLA):
    for i in range(altura):
        for j in range(ancho):
            print(PANTALLA[i][j], end="")
        print("")

#TODO:Hacer que la serpiente aparezca en un lugar aleatorio
def crearCulebra(largo):
    global PANTALLA
    posicion_cabeza_x = 3
    posicion_cabeza_y = 0
    
    posicion_cola_x = 0
    posicion_cola_y = 0

    if posicion_cabeza_y == posicion_cola_y:
        for i in range(largo-1):
            PANTALLA[posicion_cola_y][posicion_cola_x + i] = cuerpo_culebra
        PANTALLA[posicion_cabeza_y][posicion_cabeza_x] = cabeza_culebra

    elif posicion_cabeza_x == posicion_cola_x:
        for i in range(largo-1):
            PANTALLA[posicion_cola_y+i][posicion_cola_x] = cuerpo_culebra
        PANTALLA[posicion_cabeza_y][posicion_cabeza_x] = cabeza_culebra

def avanzar(largo):
    global PANTALLA
    for i in range(largo):
        PANTALLA[0][i] = "[*]"


def culebron():
    inicializarPantalla(ancho, altura)
    crearCulebra(4)
    mostrarPantalla(PANTALLA)

culebron()