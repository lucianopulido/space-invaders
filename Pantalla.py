import pygame


class Pantalla:
    def __init__(self):
        self.pantalla = pygame.display.set_mode((800, 600))
        self.fondo = pygame.image.load('imagenes/Fondo.jpg')

    def pintar_pantalla(self):
        self.pantalla.blit(self.fondo, (0, 0))

    def mover_jugador(self, imagen, x, y):
        self.pantalla.blit(imagen, (x, y))

    def mostrar_puntaje(self, puntaje, x, y):
        texto = puntaje.fuente.render(f'Puntaje: {puntaje.cantidad_puntos}', True, (255, 255, 255))
        self.pantalla.blit(texto, (x, y))

    def mostrar_texto_final(self):
        fuente_final = pygame.font.Font('freesansbold.ttf', 40)
        mi_fuente_final = fuente_final.render("JUEGO TERMINADO", True, (255, 255, 255))
        self.pantalla.blit(mi_fuente_final,(60,200))
