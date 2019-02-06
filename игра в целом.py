import pygame, os, sys

pygame.init()
size = width, height = 600, 600
screen = pygame.display.set_mode(size)

v = 200


def terminate():
    pygame.quit()
    sys.exit()


clock = pygame.time.Clock()


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


x_pos = -600
y_pos = -600


def start_screen(x_pos, y_pos):
    intro_text = ["ЗАСТАВКА", "",
                  "Правила игры",
                  "Если в правилах несколько строк,",
                  "приходится выводить их построчно"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (600, 600))
    screen.blit(fon, (int(x_pos), int(y_pos)))
    # pygame.display.flip()
    clock.tick()
    #font = pygame.font.SysFont('Calibri', 30)
    #text_coord = 200
    # for line in intro_text:
    #     string_rendered = font.render(line, 1, pygame.Color('black'))
    #     intro_rect = string_rendered.get_rect()
    #     text_coord += 10
    #     intro_rect.top = text_coord
    #     intro_rect.x = 75
    #     text_coord += intro_rect.height
    #     screen.blit(string_rendered, intro_rect)

    # while True:
    #
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             terminate()
    #         elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
    #             return  # начинаем игру
    #     pygame.display.flip()
    #     clock.tick()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if (x_pos == 0 and y_pos == 0):
            v = 0
        start_screen(int(x_pos), int(y_pos))
        screen.fill((255,255 ,0 ))
        start_screen(int(x_pos), int(y_pos))
        x_pos += v * clock.tick() / 1000
        y_pos += v * clock.tick() / 1000
        pygame.display.flip()
