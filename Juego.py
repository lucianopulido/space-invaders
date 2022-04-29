import pygame
from Pantalla import Pantalla
# funcion del jugador
from model.Enemigo import Enemigo
from model.Jugador import Jugador
from model.Bala import Bala
from model.Puntaje import Puntaje
import math
import random


def validar_limites_pantalla_jugador():
    if jugador.posicion_x <= 0:
        jugador.posicion_x = 0

    if jugador.posicion_x >= 736:
        jugador.posicion_x = 736


def validar_limites_pantalla_enemigo(e):
    if enemigo[e].posicion_x <= 0:
        enemigo[e].desplazamiento_x = 0.25
        enemigo[e].posicion_y += enemigo[e].desplazamiento_y

    if enemigo[e].posicion_x >= 736:
        enemigo[e].desplazamiento_x = -0.25
        enemigo[e].posicion_y += enemigo[e].desplazamiento_y


def validar_limites_pantalla_bala():
    if bala.posicion_y <= -64:
        bala.posicion_y = 500
        bala.estado = False


def disparar_bala(x, y):
    bala.estado = True
    pantalla.mover_jugador(bala.imagen_bala, x + 16, y + 10)


def hay_colision(x1, x2, y1, y2):
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)) < 27

# Inicializar pygame
pygame.init()

# agregar musica
pygame.mixer.music.load('sonidos/MusicaFondo.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Crear pantalla
pantalla = Pantalla()

# Titulo e icono
pygame.display.set_caption("Invasion Especial")
icono = pygame.image.load("imagenes/ovni.png")
pygame.display.set_icon(icono)

# Jugador

jugador = Jugador()

# Enemigo
enemigo = []
i = 0
cantidad_enemigos = 8
for e in range(cantidad_enemigos):
    enemigo.append(Enemigo())

# Bala
bala = Bala()

puntaje = Puntaje()

se_ejecuta = True

# Loop del juego
while se_ejecuta:
    pantalla.pintar_pantalla()

    # evento para cerrar juego
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # evento presionar flecha
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador.desplazamiento_x = -0.3
            if evento.key == pygame.K_RIGHT:
                jugador.desplazamiento_x = 0.3
            if evento.key == pygame.K_SPACE and not bala.estado:
                sonido_bala = pygame.mixer.Sound('sonidos/disparo.mp3')
                sonido_bala.play()
                bala.posicion_x = jugador.posicion_x
                disparar_bala(jugador.posicion_x, bala.posicion_y)

        # evento soltar flecha
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador.desplazamiento_x = 0

    jugador.posicion_x += jugador.desplazamiento_x

    validar_limites_pantalla_jugador()
    validar_limites_pantalla_bala()

    for e in range(cantidad_enemigos):

        if enemigo[e].posicion_y > 500:
            for j in range(cantidad_enemigos):
                enemigo[j].posicion_y = 1000
            pantalla.mostrar_texto_final()
            break

        enemigo[e].posicion_x += enemigo[e].desplazamiento_x
        validar_limites_pantalla_enemigo(e)

        if hay_colision(bala.posicion_x, enemigo[e].posicion_x, bala.posicion_y, enemigo[e].posicion_y):
            sonido_colision = pygame.mixer.Sound('sonidos/Golpe.mp3')
            sonido_colision.play()
            bala.posicion_y = 500
            bala.estado = False
            enemigo[e].posicion_x = random.randint(0, 736)
            enemigo[e].posicion_y = random.randint(50, 200)
            puntaje.cantidad_puntos += 1

        pantalla.mover_jugador(enemigo[e].imagen_enemigo, enemigo[e].posicion_x, enemigo[e].posicion_y)

    if bala.estado:
        disparar_bala(bala.posicion_x, bala.posicion_y)
        bala.posicion_y -= bala.desplazamiento_y

    pantalla.mostrar_puntaje(puntaje, puntaje.posicion_x, puntaje.posicion_y)

    pantalla.mover_jugador(jugador.imagen_jugador, jugador.posicion_x, jugador.posicion_y)
    pygame.display.update()
