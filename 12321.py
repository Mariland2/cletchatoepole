import pygame

d = input()
d = d.split(' ')
pygame.init()
size = width, height = int(d[0]) * 2 - 1
screen = pygame.display.set_mode(size)

k = int(d[0])
n = int(d[1])
z = k // n
b = 0
o = 0

for i in range(n):
    if o % 3 == 0:
        pygame.draw.circle(screen, pygame.Color('blue'), (k, k), k - z * b, 0)
    if o % 3 == 1:
        pygame.draw.circle(screen, pygame.Color('green'), (k, k), k - z * b, 0)
    if o % 3 == 2:
        pygame.draw.circle(screen, pygame.Color('red'), (k, k), k - z * b, 0)
    b += 1
    o += 1

pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()