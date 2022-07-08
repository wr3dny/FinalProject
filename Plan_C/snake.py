import pygame
import time

seashell3 = (205, 197, 191)
limegreen = (50, 205, 50)
red = (255, 0, 0)

screen_color = seashell3
msg_color = red

name = input('Please give me your name \n --->')

pygame.init()

display_width = 600
display_height = 400

display = pygame.display.set_mode((display_width, display_height))
display.fill(screen_color)
pygame.display.update()
pygame.display.set_caption(f'Plan C - if everything else fails \n Now {name} plays')

gameover = False

x1 = display_width / 2
y1 = display_height / 2

snake_size = 10

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()
snake_speed = 10

font_type = pygame.font.SysFont('calibri', 15)


def message(msg,color):
    mesg = font_type.render(msg, True, color)
    display.blit(mesg, [display_width / 2 , display_height / 2])


while not gameover:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_size
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_size
                y1_change = 0
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = snake_size
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -snake_size

    if x1 >= display_width or x1 < 0 or y1 > display_height or y1 < 0:
        gameover = True

    x1 += x1_change
    y1 += y1_change

    display.fill(screen_color)
    pygame.draw.rect(display, limegreen, [x1, y1, snake_size, snake_size])
    pygame.display.update()
    clock.tick(snake_speed)

message('You lost', red)
pygame.display.update()
time.sleep(2)

pygame.quit()
quit()

