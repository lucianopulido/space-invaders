import pygame.image


class Bala:

    def __init__(self):
        self.imagen_bala = pygame.image.load('imagenes/bala.png')
        self.posicion_x = 0
        self.posicion_y = 500
        self.desplazamiento_y = 0.75
        self.estado = False
