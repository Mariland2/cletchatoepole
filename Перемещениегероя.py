import pygame
import os

pygame.init()
size = width, height = 1000, 1000
screen = pygame.display.set_mode(size,)


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


x, y = 50, 50
image = load_image("hero1.png")
image = pygame.transform.scale(image, (150, 150))
screen.blit(image, (x, y))

o = False
pygame.mouse.set_visible(o)

running = True
while running:
    for event in pygame.event.get():
        screen.fill((255, 255, 255))
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_UP]:
                screen.fill((255, 255, 255))
                y -= 10

            if pygame.key.get_pressed()[pygame.K_DOWN]:
                screen.fill((255, 255, 255))
                y += 10

            if pygame.key.get_pressed()[pygame.K_LEFT]:
                screen.fill((255, 255, 255))
                x -= 10

            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                screen.fill((255, 255, 255))
                x += 10
        screen.blit(image, (x, y))
        pygame.display.flip()
