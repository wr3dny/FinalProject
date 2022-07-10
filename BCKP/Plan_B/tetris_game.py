import random
import pygame
# from matplotlib import colors as tcolors
#
# colors_to_use = tcolors

colors = [
    (0, 0, 0),
    (120, 37, 179),
    (100, 179, 179),
    (80, 34, 22),
    (80, 134, 22),
    (180, 34, 22),
    (180, 34, 122),
]


class Fig:
    fig = [
        [[1, 5, 9, 13], [4, 5, 6, 7]], # prosty
        [[0, 1, 4, 5]], # klocek
        [[0, 1, 5, 6], [1, 2, 4, 5], [0, 4, 5, 9], [1, 4, 5, 8]], # zetka
        [[0, 1, 2, 6], [0, 1, 2, 4], [1, 5, 8, 9], [1, 5, 9, 10]], # elka
        [[1, 4, 5, 6], [4, 5, 6, 9], [1, 4, 5, 9], [1, 5, 6, 9]] #piramida

    ]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.fig) - 1)
        self.color = random.randint(1, len(colors) - 1)
        self.rotation = 0

    def image(self):
        return self.fig[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.fig[self.type])


class Tetris:
    lvl = 2
    score = 0
    state = 'start'
    field = []
    height = 0
    width = 0
    x = 100
    y = 60
    zoom = 20
    fig = None

    def __init__(self, height, width):
        self.height = height
        self.width = width
        for i in range(width):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)

    def new_fig(self):
        self.fig = Fig(3, 0)

    def intersects(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.fig.image():
                    if i + self.fig.y > self.height - 1 or j + self.fig.x > self.width - 1 or j + self.fig.x < 0 or \
                            self.field[i + self.fig.y][j + self.fig.x] > 0:
                        intersection = True
        return intersection

    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.fig.image():
                    self.field[i + self.fig.y][j + self.fig.x] = self.fig.color
                    self.break_lines()
                    self.new_fig()
                    if self.intersects():
                        game.state = 'gameover'


    def break_lines(self):
        lines = 0
        for i in range(1, self.height):
            zeroes = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zeroes += 1
                    for ii in range(i, 1, -1):
                        for j in range(self.width):
                            self.field[ii][j] = self.field[ii - 1][j]
            self.score += lines ** 2

    def go_space(self):
        while not self.intersects():
            self.fig.y += 1
        self.fig.y -= 1
        self.freeze()

    def go_down(self):
        self.fig.y += 1
        if self.intersects():
            self.fig.y -= 1
            self.freeze()

    def go_side(self, dx):
        old_x = self.fig.x
        self.fig.x += dx
        if self.intersects():
            self.fig.x = old_x

    def rotate(self):
        old_rotation = self.fig.rotation
        self.fig.rotate()
        if self.intersects():
            self.fig.rotation = old_rotation


# Initialize the game engine
pygame.init()


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

size = (400, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Tetris")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
fps = 25
game = Tetris(20, 10)
counter = 0

pressing_down = False

while not done:
    if game.fig is None:
        game.new_fig()
    counter += 1
    if counter > 100000:
        counter = 0

    if counter % (fps // game.lvl // 2) == 0 or pressing_down:
        if game.state == "start":
            game.go_down()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.rotate()
            if event.key == pygame.K_DOWN:
                pressing_down = True
            if event.key == pygame.K_LEFT:
                game.go_side(-1)
            if event.key == pygame.K_RIGHT:
                game.go_side(1)
            if event.key == pygame.K_SPACE:
                game.go_space()
            if event.key == pygame.K_ESCAPE:
                game.__init__(20, 10)

    if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pressing_down = False

    screen.fill(WHITE)

    for i in range(game.height):
        for j in range(game.width):
            pygame.draw.rect(screen, GRAY, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
            if game.field[i][j] > 0:
                pygame.draw.rect(screen, colors[game.field[i][j]],
                                 [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

    if game.fig is not None:
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in game.fig.image():
                    pygame.draw.rect(screen, colors[game.fig.color],
                                     [game.x + game.zoom * (j + game.fig.x) + 1,
                                      game.y + game.zoom * (i + game.fig.y) + 1,
                                      game.zoom - 2, game.zoom - 2])

    font = pygame.font.SysFont('Calibri', 25, True, False)
    font1 = pygame.font.SysFont('Calibri', 65, True, False)
    text = font.render("Score: " + str(game.score), True, BLACK)
    text_game_over = font1.render("Game Over", True, (255, 125, 0))
    text_game_over1 = font1.render("Press ESC", True, (255, 215, 0))

    screen.blit(text, [0, 0])
    if game.state == "gameover":
        screen.blit(text_game_over, [20, 200])
        screen.blit(text_game_over1, [25, 265])

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()








