import pygame.image
import random


class Enemigo:

    def __init__(self):
        self.imagen_enemigo = pygame.image.load('imagenes/enemigo.png')
        self.posicion_x = random.randint(0, 736)
        self.posicion_y = random.randint(50, 200)
        self.desplazamiento_x = 0.25
        self.desplazamiento_y = 50

