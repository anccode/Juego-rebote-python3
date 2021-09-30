import pygame

class pelota:
    def __init__(self, ventana, x, y):
        self.ventana = ventana
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0

    def dibujar(self):
        pygame.draw.rect(self.ventana, (255, 255, 255), (self.x, self.y, 10, 10))

    def mover(self):
        self.x += self.vx
        self.y += self.vy


def refrescar(ventana):
    ventana.fill((0, 0, 0))
    bola.dibujar()
    text = font.render(str(golpes), True, ((255, 255, 255)))
    text_rect = text.get_rect()
    text_rect.centerx = 300
    ventana.blit(text, text_rect)

def main():
    global bola, golpes, font
    ventana = pygame.display.set_mode((600, 400))
    ventana.fill((0, 0, 0))
    bola = pelota(ventana, 50, 100)
    bola.vx = 0.5
    bola.vy = 0.2
    golpes = 0
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 30)
    jugar = True
    while jugar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jugar = False
        bola.mover()
        if bola.x >= 590:
            bola.vx *= -1
            bola.x = 590
            golpes += 1
        if bola.x <= 0:
            bola.vx *= -1
            bola.x = 0
            golpes += 1
        if bola.y >= 390:
            bola.vy *= -1
            bola.y = 390
            golpes += 1
        if bola.y <= 0:
            bola.vy *= -1
            bola.y = 0
            golpes += 1
        refrescar(ventana)
        pygame.display.update()


if __name__ == '__main__':
    main()
    pygame.quit()