import pygame
import os
import sys

pygame.init()
size = width, height = 800, 800
screen = pygame.display.set_mode(size, )


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


def draw(summa):
    font = pygame.font.SysFont('CalNeulandShadow-Bold', 50)
    text = font.render("На балансе:   " + str(summa//1), 1, (255, 20, 147))
    text_x = 50
    text_y = 50
    screen.blit(text, (text_x, text_y))


summa = 0
cl = 10
price = 500
x, y = 300, 300
image = load_image("pro.png")
image = pygame.transform.scale(image, (300, 300))
image2 = load_image("pro.png")
image2 = pygame.transform.scale(image2, (200, 200))

screen.blit(image, (x, y))
fonn = load_image("fonn.jpg")
fonn = pygame.transform.scale(fonn, (800, 800))

qwe = load_image("1.png")
qwe = pygame.transform.scale(qwe, (100, 100))
screen.blit(qwe, (100, 700))

o = False
pygame.mouse.set_visible(o)

running = True
while running:
    screen.blit(fonn, (0, 0))
    screen.blit(qwe, (100, 700))
    draw(summa)
    for event in pygame.event.get():
        # screen.blit(fonn, (0, 0))
        # screen.blit(qwe, (100, 700))
        # draw(summa)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                summa += cl
                screen.blit(image2, (x + 50, y + 50))
                pygame.display.flip()
                pygame.time.delay(65)
            if event.key == pygame.K_1:
                if summa - price >= 0:
                    cl += 100
                    summa = summa - price
                    price = price * 1.5
                    screen.blit(pygame.transform.scale(qwe, (75, 75)), (100, 700))
                    pygame.display.flip()
                    pygame.time.delay(65)

            if pygame.key.get_pressed()[pygame.K_LEFT]:
                x -= 10

            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                x += 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:
                screen.blit(image, (x, y))
                pygame.display.flip()
                pygame.time.delay(65)
            if event.key == pygame.K_1:
                screen.blit(qwe, (100, 700))
                pygame.display.flip()
                pygame.time.delay(65)

    screen.blit(fonn, (0, 0))
    draw(summa)
    screen.blit(image, (x, y))
    screen.blit(qwe, (100, 700))
    pygame.display.flip()
