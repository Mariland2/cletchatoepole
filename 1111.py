import os
import pygame
import random

pygame.init()
size = width, height = 800, 800
screen = pygame.display.set_mode(size)
pygame.display.flip()


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


all_sprites = pygame.sprite.Group()




class Mouse(pygame.sprite.Sprite):
    image = load_image("mouse.png")
    image = pygame.transform.scale(image, (50, 50))
    def __init__(self, group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        super().__init__(group)
        self.image = Mouse.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width)
        self.rect.y = random.randrange(height)

    def update(self):
        self.rect = self.rect.move(random.randrange(3) - 1,
                                   random.randrange(3) - 1)

    def get_event(self, event):
        if self.rect.collidepoint(event.pos):
            self.image = self.image_boom

while running:
    screen.fill((0, 0, 0))
    board.render()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:


        pygame.display.flip()


all_sprites.draw(screen)
all_sprites.update()
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()
