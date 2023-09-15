import turtle
import time
import random

# Configuración de la ventana
wn = turtle.Screen()
wn.title("Juego de Serpiente")
wn.bgcolor("white")
wn.setup(width=600, height=600)
wn.tracer(0)  # Desactivar actualización automática de la pantalla

# Cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("green")
cabeza.penup()
cabeza.goto(0, 0)
cabeza.direction = "stop"

# Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0, 100)

# Cuerpo de la serpiente
segmentos = []

# Funciones de movimiento
def mover():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

def ir_arriba():
    if cabeza.direction != "down":
        cabeza.direction = "up"

def ir_abajo():
    if cabeza.direction != "up":
        cabeza.direction = "down"

def ir_izquierda():
    if cabeza.direction != "right":
        cabeza.direction = "left"

def ir_derecha():
    if cabeza.direction != "left":
        cabeza.direction = "right"

# Teclado
wn.listen()
wn.onkeypress(ir_arriba, "w")
wn.onkeypress(ir_abajo, "s")
wn.onkeypress(ir_izquierda, "a")
wn.onkeypress(ir_derecha, "d")

# Función para generar comida en una ubicación aleatoria
def generar_comida():
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    comida.goto(x, y)

# Colisión con la comida
def colision_comida():
    if cabeza.distance(comida) < 20:
        return True
    else:
        return False

# Colisión con los bordes
def colision_bordes():
    if (
        cabeza.xcor() > 290
        or cabeza.xcor() < -290
        or cabeza.ycor() > 290
        or cabeza.ycor() < -290
    ):
        return True
    else:
        return False

# Colisión con el cuerpo
def colision_cuerpo():
    for segmento in segmentos:
        if cabeza.distance(segmento) < 20:
            return True
    return False

# Pantalla de juego
while True:
    wn.update()

    # Mover la serpiente
    mover()

    # Verificar colisiones
    if colision_comida():
        generar_comida()

        # Agregar un segmento al cuerpo de la serpiente
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("green")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

    if colision_bordes() or colision_cuerpo():
        cabeza.goto(0, 0)
        cabeza.direction = "stop"

        # Ocultar los segmentos del cuerpo
        for segmento in segmentos:
            segmento.goto(1000, 1000)

        # Limpiar la lista de segmentos
        segmentos.clear()

    # Mover los segmentos del cuerpo en orden inverso
    for i in range(len(segmentos) - 1, 0, -1):
        x = segmentos[i - 1].xcor()
        y = segmentos[i - 1].ycor()
        segmentos[i].goto(x, y)

    # Mover el primer segmento a la posición de la cabeza
    if len(segmentos) > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x, y)

    # Pausa antes de cada actualización
    time.sleep(0.1)

wn.mainloop()
