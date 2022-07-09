import pygame as pg


def main():
    pg.init()
    screen = pg.display.set_mode((640, 480))
    font = pg.font.Font(None, 40)
    gray = pg.Color('gray19')
    blue = pg.Color('dodgerblue')
    # The clock is used to limit the frame rate
    # and returns the time since last tick.
    clock = pg.time.Clock()
    timer = 10  # Decrease this to count down.
    dt = 0  # Delta time (time since last tick).

    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        timer -= dt
        if timer <= 0:
            return

        screen.fill(gray)
        txt = font.render(str(round(timer, 2)), True, blue)
        screen.blit(txt, (70, 70))
        pg.display.flip()
        dt = clock.tick(30) / 1000  # / 1000 to convert to seconds.


if __name__ == '__main__':
    main()
    screen = pg.display.set_mode((640, 480))
    end = 'End of time'
    pg.Surface(screen, (70, 70))
    screen.blit(end, (70, 70))
    print('End of time')
    pg.quit()