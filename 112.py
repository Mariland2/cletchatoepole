import pygame
import os

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size


def load_image(nich, colorkey=None):
    fullname = os.path.join('data', nich)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', nich)
        raise SystemExit(message)
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


image = load_image("mouse.png")
image = pygame.transform.scale(image, (50, 50))

o = False
pygame.mouse.set_visible(o)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            screen.fill((0,0,0))
            screen.blit(image, (event.pos[0]-25, event.pos[1]-30))

        pygame.display.flip()
