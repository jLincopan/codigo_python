from time import sleep

# variables globales (por mientras, cuando esté más completo el programa
# pienso quitarlas para solo usar variables locales)

ancho = 20
altura = 10

cuerpo_culebra = "[=]"
cabeza_culebra = "[>]"
espacio_vacio = "[ ]"

posicion_cabeza_x = 3
posicion_cabeza_y = 0
    
posicion_cola_x = 0
posicion_cola_y = 0

PANTALLA = []

#crea, llena y devuelve una matriz con los carácteres especificados en "caracter_inicial"
def crearMatriz(caracter_inicial, ancho, altura):
    matriz = []
    for i in range(altura):
        columna = []
        for j in range(ancho):
            columna.append(caracter_inicial)
        matriz.append(columna)
    return matriz

#llena la matriz que contiene la pantalla
def inicializarPantalla(ancho, altura):
    global PANTALLA
    PANTALLA = crearMatriz(espacio_vacio, ancho, altura)

def mostrarPantalla(PANTALLA):
    for i in range(altura):
        for j in range(ancho):
            print(PANTALLA[i][j], end="")
        print("")

# Llena las posiciones que debería ocupar la serpiente en la matriz
# que representa la pantalla, NO muestra la pantalla, solo cambia los
# carácteres para representar la serpiente
# TODO:Hacer que la serpiente aparezca en un lugar aleatorio
def dibujarCulebra(largo):
    global PANTALLA

    if posicion_cabeza_y == posicion_cola_y:
        for i in range(largo-1):
            PANTALLA[posicion_cola_y][posicion_cola_x + i] = cuerpo_culebra
        PANTALLA[posicion_cabeza_y][posicion_cabeza_x] = cabeza_culebra

    elif posicion_cabeza_x == posicion_cola_x:
        for i in range(largo-1):
            PANTALLA[posicion_cola_y+i][posicion_cola_x] = cuerpo_culebra
        PANTALLA[posicion_cabeza_y][posicion_cabeza_x] = cabeza_culebra

def avanzar(largo):

    global posicion_cabeza_x
    global posicion_cabeza_y
    
    global posicion_cola_x
    global posicion_cola_y

    global PANTALLA
    posicion_cabeza_x+=1
    posicion_cola_x+=1
    dibujarCulebra(4)


def culebron():
    inicializarPantalla(ancho, altura)

    #bucle principal
    while 1:
        print("\033[H\033[J") 
        mostrarPantalla(PANTALLA)
        print()
        avanzar(4)
        sleep(0.250)
    
culebron()