import pygame

d = input()
d = d.split(' ')
pygame.init()
size = width, height = int(d[0]), int(d[0])
screen = pygame.display.set_mode(size)

yy = height // int(d[1])
x = 0
y = 0
t = 0
z = 0
print(yy)
for i in range(int(d[1])):
    z += 1
    for j in range(int(d[1])):
        if t % 2 == 0:
            screen.fill(pygame.Color('black'), (x, y, yy, yy))
            x += yy
        else:
            screen.fill(pygame.Color('white'), (x, y, yy, yy))
            x += yy
        t += 1
    if z % 2 == 1:
        t = 1
    else:
        t = 0
    y += yy
    x = 0

pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
