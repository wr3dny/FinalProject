import pygame
import time
import colors_rgb
import random

print(pygame.font.get_fonts())
pygame.init()

screen_color = colors_rgb.wheat
snake_color = colors_rgb.green
lost_game_color = colors_rgb.cadmiumorange
food_for_snake_color = colors_rgb.purple1
close_screen_color = colors_rgb.wheat4
close_screen_text = colors_rgb.greenyellow
msg_color = colors_rgb.azure1
score_color = colors_rgb.black



display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width, display_height))
display.fill(screen_color)
pygame.display.update()
pygame.display.set_caption(f'Plan C - if everything else fails')

clock = pygame.time.Clock()

snake_size = 10
snake_speed = 10

font_type = pygame.font.SysFont('gothici', 25)
score_font = pygame.font.SysFont('gothici', 25)

def player_score(score):
    value = score_font.render('Current score: ' + str(score), True, score_color)
    display.blit(value, [display_width /3, 0])

def snake_current(snake_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, snake_color, [x[0], x[1], snake_size, snake_size])

def message(msg, color):
    mesg = font_type.render(msg, True, color)
    display.blit(mesg, [display_width / 9, display_height / 2])

def gameloop():
    game_over = False
    game_close = False

# snake starting position on screen 
    x1 = display_width / 2
    y1 = display_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    food_for_snakex = round(random.randrange(0, display_width - snake_size) / 10.0) * 10.0
    food_for_snakey = round(random.randrange(0, display_height - snake_size)/ 10.0) * 10.0

    while not game_over:

        while game_close == True:
            display.fill(close_screen_color)
            message('You lost! Press "q" for quit or "a" for playing again', close_screen_text)
            player_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_a:
                        gameloop()
# snake control
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

# setting space boundaries
        if x1 >= display_width or x1 < 0 or y1 > display_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        display.fill(screen_color)

        pygame.draw.rect(display, food_for_snake_color, [food_for_snakex, food_for_snakey, snake_size, snake_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        snake_current(snake_size, snake_list)
        player_score(snake_length - 1)

        pygame.display.update()

        if x1 == food_for_snakex and y1 == food_for_snakey:
            food_for_snakex = round(random.randrange(0, display_width - snake_size) / 10.0) * 10.0
            food_for_snakey = round(random.randrange(0, display_height - snake_size) / 10.0) * 10.0
            snake_length += 1
            print('Gain weight')

        clock.tick(snake_speed)
        print(snake_length)
        print(snake_head)
        print(snake_list)

    pygame.quit()
    quit()


gameloop()
