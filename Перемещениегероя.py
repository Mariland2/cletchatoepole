import pygame
import os,sys

pygame.init()
size = width, height = 600, 600
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


def start_screen():
    intro_text = ["ЗАСТАВКА", "",
                  "Правила игры",
                  "Если в правилах несколько строк,",
                  "приходится выводить их построчно"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (600, 600))
    screen.blit(fon, (0, 0))
    font = pygame.font.SysFont('Calibri', 30)
    text_coord = 200
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 75
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        # pygame.time.Clock.tick(FPS)
def terminate():
    pygame.quit()
    sys.exit()

x, y = 50, 50
image = load_image("hero1.png")
image = pygame.transform.scale(image, (150, 150))
screen.blit(image, (x, y))


o = False
pygame.mouse.set_visible(o)

running = True
start_screen()
while running:
    for event in pygame.event.get():
        screen.fill((255, 255, 255))
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_UP]:
                y -= 10

            if pygame.key.get_pressed()[pygame.K_DOWN]:
                y += 10

            if pygame.key.get_pressed()[pygame.K_LEFT]:
                x -= 10

            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                x += 10
        screen.blit(image, (x, y))
        pygame.display.flip()



