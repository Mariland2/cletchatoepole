
import os
import pygame

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

while pygame.event.wait().type != pygame.QUIT:



    class Bomb(pygame.sprite.Sprite):
        image = load_image("bomb.png")

        def __init__(self, group):
            # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
            # Это очень важно!!!
            super().__init__(group)
            self.image = Bomb.image
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(width)
            self.rect.y = random.randrange(height)

        def update(self):
            self.rect = self.rect.move(random.randrange(3) - 1,
                                       random.randrange(3) - 1)
    for _ in range(50):
        Bomb(all_sprites)

    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()

