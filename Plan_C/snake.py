import pygame
import time
import colors_rgb
import random

# print(pygame.font.get_fonts())

screen = colors_rgb.seashell3
limegreen = (50, 205, 50)
red = (255, 0, 0)
food_for_snake = colors_rgb.purple1
close_screen_color = colors_rgb.black
close_screen_text = colors_rgb.limegreen

screen_color = screen
msg_color = red

pygame.init()

display_width = 600
display_height = 400

display = pygame.display.set_mode((display_width, display_height))
display.fill(screen_color)
pygame.display.update()
pygame.display.set_caption(f'Plan C - if everything else fails')

game_over = False

snake_size = 10

clock = pygame.time.Clock()
snake_speed = 10

font_type = pygame.font.SysFont('franklingothicmedium', 15)


def message(msg, color):
    mesg = font_type.render(msg, True, color)
    display.blit(mesg, [display_width / 4, display_height / 2])

def gameloop():
    game_over = False
    game_close = False

# snake starting position on screen 
    x1 = display_width / 2
    y1 = display_height / 2

    x1_change = 0
    y1_change = 0

    food_for_snakex = round(random.randrange(0, display_width - snake_size))
    food_for_snakey = round(random.randrange(0, display_height - snake_size))

    while not game_over:
        while game_close == True:
            display.fill(close_screen_color)
            message('You lost!\n Press "q" for quit or "a" for playing again', close_screen_text)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_a:
                        gameloop()



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
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
                game_over = True

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

