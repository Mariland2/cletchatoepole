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
        for i in range(self.width):
            for t in range(self.height):
                pygame.draw.rect(screen, (255, 255, 255), (
                    self.x + (self.cell_size * self.k - 1), self.y + (self.cell_size * self.n - 1), self.cell_size,
                    self.cell_size), 1)
                self.n += 1
                if self.board[i-1][t-1] == 1:
                    pygame.draw.rect(screen, (0, 0, 150), (50 * (q // 50), 50 * (w // 50), 48, 48), 0)

            self.n = 0
            self.k += 1

    def tr(self, xx, yy):
        self.board[xx][yy] = [1]


board = Board(4, 3)
board.set_view(100, 100, 50)
running = True
screen.fill((0, 0, 0))
board.render()
while running:
    screen.fill((0, 0, 0))
    board.render()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(1):
                q = event.pos[0]
                w = event.pos[1]
                board.tr((q // 50)-1, (w // 50)-1)
        pygame.display.flip()
