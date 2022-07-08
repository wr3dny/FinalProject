import random

class Figure:
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
        self.color = random.randint(1, len(colors) -1)
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


def main():
    pass


if __name__ == '__main__':
    main()