import pygame


class Jugador:

    def __init__(self):
        self.imagen_jugador = pygame.image.load("imagenes/cohete.png")
        self.posicion_x = 368
        self.posicion_y = 500
        self.desplazamiento_x = 0
