import pygame, random
import os
import sys


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


pygame.init()
size = width, height = 800, 800
screen = pygame.display.set_mode(size, )
all_sprites = pygame.sprite.Group()
all_sprites1 = pygame.sprite.Group()


def draw2(cl):
    font8 = pygame.font.SysFont('Magneto', 20)
    text8 = font8.render("added in one click:   " + str(cl // 1), 1, (0, 0, 0))
    text_x8 = 50
    text_y8 = 80
    screen.blit(text8, (text_x8, text_y8))


def draw(summa):
    font = pygame.font.SysFont('Magneto', 25)
    text = font.render("On your balance:   " + str(summa // 1), 1, (0, 0, 0))
    text_x = 50
    text_y = 50
    screen.blit(text, (text_x, text_y))


def draw3(cl1):
    font7 = pygame.font.SysFont('Magneto', 20)
    text7 = font7.render("added in one second:   " + str(cl1 // 1), 1, (0, 0, 0))
    text_x7 = 50
    text_y7 = 110
    screen.blit(text7, (text_x7, text_y7))


def cn1(price):
    font1 = pygame.font.SysFont('Magneto', 15)
    text1 = font1.render("price " + str(price // 1), 1, (0, 0, 0))
    text_x1 = 106
    text_y1 = 695
    screen.blit(text1, (text_x1, text_y1))


def cn2(price2):
    font2 = pygame.font.SysFont('Magneto', 15)
    text2 = font2.render("price " + str(price2 // 1), 1, (0, 0, 0))
    text_x2 = 306
    text_y2 = 695
    screen.blit(text2, (text_x2, text_y2))


def cn3(price3):
    font3 = pygame.font.SysFont('Magneto', 15)
    text3 = font3.render("price " + str(price3 // 1), 1, (0, 0, 0))
    text_x3 = 506
    text_y3 = 695
    screen.blit(text3, (text_x3, text_y3))


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


class es(pygame.sprite.Sprite):
    image = load_image("pro.png")
    image = pygame.transform.scale(image, (100, 100))

    def __init__(self, group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        super().__init__(group)
        self.image = sprite.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width)
        self.rect.y = random.randrange(height)

    def update(self):
        self.rect = self.rect.move(random.randrange(3) - 1,
                                   random.randrange(3) - 1)

class es2(pygame.sprite.Sprite):
    image = load_image("pro.png")
    image = pygame.transform.scale(image, (75, 75))

    def __init__(self, group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        super().__init__(group)
        self.image = sprite.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width)
        self.rect.y = random.randrange(height)

    def update(self):
        self.rect = self.rect.move(random.randrange(3) - 1,
                                   random.randrange(3) - 1)


def maing():
    while running:

        screen.blit(fonn, (0, 0))
        screen.blit(qwe, (100, 700))
        screen.blit(qwe, (300, 700))
        screen.blit(qwe, (500, 700))
        draw(summa)
        draw2(cl)
        draw3(cl1)
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
                if event.key == pygame.K_2:
                    if summa - price >= 0:
                        cl += 100
                        summa = summa - price
                        price = price * 1.5
                        screen.blit(pygame.transform.scale(qwe, (75, 75)), (300, 700))
                        pygame.display.flip()
                        pygame.time.delay(65)
                if event.key == pygame.K_3:
                    if summa - price >= 0:
                        cl += 100
                        summa = summa - price
                        price = price * 1.5
                        screen.blit(pygame.transform.scale(qwe, (75, 75)), (500, 700))
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
                if event.key == pygame.K_1:
                    if summa - price >= 0:
                        screen.blit(qwe, (300, 700))
                        pygame.display.flip()
                        pygame.time.delay(65)
                if event.key == pygame.K_1:
                    if summa - price >= 0:
                        screen.blit(qwe, (500, 700))
                        pygame.display.flip()
                        pygame.time.delay(65)

        screen.blit(fonn, (0, 0))
        draw(summa)
        screen.blit(image, (x, y))
        screen.blit(qwe, (100, 700))
        pygame.display.flip()


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
screen.blit(qwe, (300, 700))
screen.blit(qwe, (500, 700))

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
                price2 = float(stre[3])
                price3 = float(stre[4])
                cl1 = float(stre[5])
                n = int(stre[6])

                mrun = False
            if event.key == pygame.K_LSHIFT:
                summa = 0
                cl = 10
                price = 500
                price2 = 5000
                price3 = 50000
                cl1 = 0
                n = 0
                per = []
                mrun = False
clock = pygame.time.Clock()
tm = 0
while running:

    screen.blit(fonn, (0, 0))
    all_sprites.draw(screen)
    screen.blit(qwe, (100, 700))
    screen.blit(qwe, (300, 700))
    screen.blit(qwe, (500, 700))
    draw(summa)
    draw2(cl)
    draw3(cl1)
    cn1(price)
    cn2(price2)
    cn3(price3)
    clock.tick(30)

    for event in pygame.event.get():
        # screen.blit(fonn, (0, 0))
        # screen.blit(qwe, (100, 700))
        # draw(summa)
        if event.type == pygame.QUIT:
            f = open("sohr.txt", mode="w")
            per.append(str(summa))
            per.append(str(cl))
            per.append(str(price))
            per.append(str(price2))
            per.append(str(price3))
            per.append(str(cl1))
            per.append(str(n))
            f.write(' '.join(per))
            f.close()
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                summa += cl
                screen.blit(fonn, (0, 0))
                draw(summa)
                draw2(cl)
                draw3(cl1)
                all_sprites1.draw(screen)

                screen.blit(qwe, (100, 700))
                screen.blit(qwe, (300, 700))
                screen.blit(qwe, (500, 700))
                cn1(price)
                cn2(price2)
                cn3(price3)
                screen.blit(image2, (x + 50, y + 50))
                pygame.display.flip()
                pygame.time.delay(65)
            if event.key == pygame.K_1:
                if summa - price >= 0:
                    cl += 100
                    summa = summa - price
                    price = price * 1.5
                    screen.blit(fonn, (0, 0))
                    draw(summa)
                    draw2(cl)
                    draw3(cl1)
                    all_sprites.draw(screen)
                    screen.blit(qwe, (300, 700))
                    screen.blit(qwe, (500, 700))
                    cn1(price)
                    cn2(price2)
                    cn3(price3)
                    screen.blit(pygame.transform.scale(qwe, (75, 75)), (100, 700))
                    pygame.display.flip()
                    pygame.time.delay(65)
            if event.key == pygame.K_2:
                if summa - price2 >= 0:
                    cl = cl * 2
                    n += 1
                    summa = summa - price2
                    price2 = price2 * 1.5
                    screen.blit(fonn, (0, 0))
                    draw(summa)
                    draw2(cl)
                    draw3(cl1)
                    all_sprites.draw(screen)

                    for i in range(1):
                        # можно сразу создавать спрайты с указанием группы

                        sprite = pygame.sprite.Sprite(all_sprites)
                        sprite1= pygame.sprite.Sprite(all_sprites1)
                        # определим его вид
                        sprite.image = load_image("pro.png")
                        sprite1.image = load_image("pro.png")
                        sprite.image = pygame.transform.scale(sprite.image, (100, 100))
                        sprite1.image = pygame.transform.scale(sprite.image, (75, 75))
                        # и размеры
                        sprite.rect = sprite.image.get_rect()
                        sprite1.rect = sprite.image.get_rect()
                        # добавим спрайт в группу
                        all_sprites.add(sprite)
                        all_sprites1.add(sprite1)

                        # задаём случайное местоположение бомбочке
                        sprite.rect.x = random.randrange(width)
                        sprite.rect.y = random.randrange(height)
                        sprite1.rect.x = sprite.rect.x + 12
                        sprite1.rect.y = sprite.rect.y + 12

                    screen.blit(qwe, (100, 700))
                    screen.blit(qwe, (500, 700))
                    cn1(price)
                    cn2(price2)
                    cn3(price3)
                    screen.blit(pygame.transform.scale(qwe, (75, 75)), (300, 700))
                    pygame.display.flip()
                    pygame.time.delay(65)
            if event.key == pygame.K_3:
                if summa - price3 >= 0:
                    cl1 += 100
                    summa = summa - price3
                    price3 = price3 * 1.5
                    screen.blit(fonn, (0, 0))
                    draw(summa)
                    draw2(cl)
                    draw3(cl1)
                    all_sprites.draw(screen)

                    screen.blit(qwe, (100, 700))
                    screen.blit(qwe, (300, 700))
                    cn1(price)
                    cn2(price2)
                    cn3(price3)
                    screen.blit(pygame.transform.scale(qwe, (75, 75)), (500, 700))
                    pygame.display.flip()
                    pygame.time.delay(65)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:
                screen.blit(fonn, (0, 0))
                draw(summa)
                draw2(cl)
                draw3(cl1)
                all_sprites.draw(screen)

                screen.blit(qwe, (100, 700))
                screen.blit(qwe, (300, 700))
                screen.blit(qwe, (500, 700))
                screen.blit(image, (x, y))
                cn1(price)
                cn2(price2)
                cn3(price3)
                pygame.display.flip()
                pygame.time.delay(65)
            if event.key == pygame.K_1:
                if summa - price >= 0:
                    screen.blit(fonn, (0, 0))
                    draw(summa)
                    draw2(cl)
                    draw3(cl1)
                    all_sprites.draw(screen)

                    screen.blit(qwe, (100, 700))
                    screen.blit(qwe, (300, 700))
                    screen.blit(qwe, (500, 700))
                    cn1(price)
                    cn2(price2)
                    cn3(price3)
                    pygame.display.flip()
                    pygame.time.delay(65)
            if event.key == pygame.K_2:
                if summa - price >= 0:
                    screen.blit(fonn, (0, 0))
                    draw(summa)
                    draw2(cl)
                    draw3(cl1)
                    all_sprites.draw(screen)

                    screen.blit(qwe, (100, 700))
                    screen.blit(qwe, (300, 700))
                    screen.blit(qwe, (500, 700))
                    cn1(price)
                    cn2(price2)
                    cn3(price3)
                    pygame.display.flip()
                    pygame.time.delay(65)
            if event.key == pygame.K_3:
                if summa - price >= 0:
                    screen.blit(fonn, (0, 0))
                    draw(summa)
                    draw2(cl)
                    draw3(cl1)
                    all_sprites.draw(screen)
                    screen.blit(qwe, (100, 700))
                    screen.blit(qwe, (300, 700))
                    screen.blit(qwe, (500, 700))

                    cn1(price)
                    cn2(price2)
                    cn3(price3)
                    pygame.display.flip()
                    pygame.time.delay(65)

    screen.blit(fonn, (0, 0))
    draw(summa)
    draw2(cl)
    draw3(cl1)
    all_sprites.draw(screen)

    screen.blit(image, (x, y))
    screen.blit(qwe, (100, 700))
    screen.blit(qwe, (300, 700))
    screen.blit(qwe, (500, 700))

    cn1(price)
    cn2(price2)
    cn3(price3)
    tm += 1
    if tm == 30:
        tm = 0
        summa += cl1
    pygame.display.flip()
