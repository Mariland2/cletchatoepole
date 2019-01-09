import pygame

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        self.x = self.left
        self.y = self.top
        self.n = 0
        self.k = 0
        for self.i in range(self.width):
            for self.t in range(self.height):
                pygame.draw.rect(screen, (255, 255, 255), (
                    self.x + (self.cell_size * self.k - 1), self.y + (self.cell_size * self.n - 1), self.cell_size,
                    self.cell_size), 1)
                self.n += 1
            self.n = 0
            self.k += 1


board = Board(4, 3)
board.set_view(100, 100, 50)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    board.render()
    pygame.display.flip()
