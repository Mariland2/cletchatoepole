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
    font = pygame.font.SysFont('Magneto', 50)
    text = font.render("On your balance:   " + str(summa // 1), 1, (255, 20, 147))
    text_x = 50
    text_y = 50
    screen.blit(text, (text_x, text_y))


def menu():
    screen.blit(ostrova, (0, 0))
    font = pygame.font.SysFont('Magneto', 50)
    text1 = font.render("Press TAB to continue", 1, (255, 20, 147))
    text_x = 50
    text_y = 250
    screen.blit(text1, (text_x, text_y))

    text = font.render("Press SHIFT to start again", 1, (255, 20, 147))
    text_x2 = 50
    text_y2 = 50
    screen.blit(text, (text_x2, text_y2))


def maing():
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


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    screen.blit(image, (x, y))
                    pygame.display.flip()
                    pygame.time.delay(65)
                if event.key == pygame.K_1:
                    if summa - price >= 0:
                        screen.blit(qwe, (100, 700))
                        pygame.display.flip()
                        pygame.time.delay(65)

        screen.blit(fonn, (0, 0))
        draw(summa)
        screen.blit(image, (x, y))
        screen.blit(qwe, (100, 700))
        pygame.display.flip()


x, y = 300, 300
image = load_image("image.png")
image = pygame.transform.scale(image, (300, 300))
image2 = load_image("image.png")
image2 = pygame.transform.scale(image2, (200, 200))

screen.blit(image, (x, y))
fonn = load_image("fonn.jpg")
fonn = pygame.transform.scale(fonn, (800, 800))

qwe = load_image("1.png")
qwe = pygame.transform.scale(qwe, (100, 100))
screen.blit(qwe, (100, 700))

ostrova = load_image("os.jpg")
ostrova = pygame.transform.scale(ostrova, (800, 800))

o = False
pygame.mouse.set_visible(o)

running = True
per = []
mrun = True
while mrun:
    menu()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                f = open("sohr.txt", mode="r")
                stre = f.read()
                stre = stre.split(' ')
                summa = float(stre[0])
                cl = float(stre[1])
                price = float(stre[2])
                mrun = False
            if event.key == pygame.K_LSHIFT:
                summa = 0
                cl = 10
                price = 500
                per = []
                mrun = False



while running:

    screen.blit(fonn, (0, 0))
    draw(summa)
    for event in pygame.event.get():
        # screen.blit(fonn, (0, 0))
        # screen.blit(qwe, (100, 700))
        # draw(summa)
        if event.type == pygame.QUIT:
            f = open("sohr.txt", mode="w")
            per.append(str(summa))
            per.append(str(cl))
            per.append(str(price))
            f.write(' '.join(per))
            f.close()
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                summa += cl
                screen.blit(image2, (x + 50, y + 50))
                pygame.display.flip()
                screen.blit(qwe, (100, 700))
                pygame.time.delay(65)
            if event.key == pygame.K_1:
                if summa - price >= 0:
                    cl += 100
                    summa = summa - price
                    price = price * 1.5
                    screen.blit(pygame.transform.scale(qwe, (75, 75)), (100, 700))
                    pygame.display.flip()
                    pygame.time.delay(65)


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:
                screen.blit(image, (x, y))
                pygame.display.flip()
                pygame.time.delay(65)
            if event.key == pygame.K_1:
                if summa - price >= 0:
                    screen.blit(qwe, (100, 700))
                    pygame.display.flip()
                    pygame.time.delay(65)

    screen.blit(fonn, (0, 0))
    draw(summa)
    screen.blit(image, (x, y))
    screen.blit(qwe, (100, 700))
    pygame.display.flip()
