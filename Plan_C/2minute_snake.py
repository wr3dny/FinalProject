import pygame
import time
import colors_rgb
import random
import datetime



# print(pygame.font.get_fonts())
pygame.init()

screen_color = colors_rgb.wheat
snake_color = colors_rgb.green
lost_game_color = colors_rgb.cadmiumorange
food_for_snake_color = colors_rgb.purple1
close_screen_color = colors_rgb.wheat4
close_screen_text1 = colors_rgb.black
close_screen_text2 = colors_rgb.red2
close_screen_text3 = colors_rgb.green
close_screen_text4 = colors_rgb.purple
lastscore_color = colors_rgb.blue
msg_color = colors_rgb.azure1
score_color = colors_rgb.black
timer_color = colors_rgb.blue

today = datetime.date.today()

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
    value = score_font.render('Current score: ' + str(score - 1), True, score_color)
    display.blit(value, [display_width / 3, 0])


def dump_file_save(added):
    with open('dump_file.txt', 'w') as f:
        f.write(added)



def file_save():
    with open('dump_file.txt', 'r') as f:
        last = f.readline()
        with open('high_score.txt', 'a+') as fopen:
            d1 = today
            fopen.write('\n' + str(today) + ' - ' + last)


def file_open(line):
    with open('high_score.txt', 'r') as f:
        last_lines = f.readlines()[-line]
        return last_lines


def snake_current(snake_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, snake_color, [x[0], x[1], snake_size, snake_size])


def message(msg1, msg2, msg3, msg4, color1, color2, color3, color4):
    mesg1 = font_type.render(msg1, True, color1)
    display.blit(mesg1, [display_width / 15, display_height / 3])
    mesg2 = font_type.render(msg2, True, color2)
    display.blit(mesg2, [display_width / 15, display_height / 3 + 2 * 25])
    mesg3 = font_type.render(msg3, True, color3)
    display.blit(mesg3, [display_width / 15, display_height / 3 + 4 * 25])
    mesg4 = font_type.render(msg4, True, color4)
    display.blit(mesg4, [display_width / 15, display_height / 3 + 6 * 25])


def score_msg(scr0, scr1, scr2, scr3, scr4, scr5, color4):
    scr0 = font_type.render(scr0, True, color4)
    display.blit(scr0, [display_width / 2, display_height / 3 - 2 * 25])
    scr1 = font_type.render(scr1, True, color4)
    display.blit(scr1, [display_width / 2, display_height / 3])
    scr2 = font_type.render(scr2, True, color4)
    display.blit(scr2, [display_width / 2, display_height / 3 + 2 * 25])
    scr3 = font_type.render(scr3, True, color4)
    display.blit(scr3, [display_width / 2, display_height / 3 + 4 * 25])
    scr4 = font_type.render(scr4, True, color4)
    display.blit(scr4, [display_width / 2, display_height / 3 + 6 * 25])
    scr5 = font_type.render(scr5, True, color4)
    display.blit(scr5, [display_width / 2, display_height / 3 + 8 * 25])

def main():
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
    food_for_snakey = round(random.randrange(0, display_height - snake_size) / 10.0) * 10.0
# basic for counter - 120s , delay 1000 == 1s, set in upper left corner
    time_counter = 120
    time_delay = 1000
    timer_event = game_over

    text = font_type.render('You got: ' + str(time_counter), True, timer_color)
    display.blit(text, [0, 0])
    pygame.time.set_timer(timer_event, time_delay)

    for event in pygame.event.get():
        if event.type == timer_event:
            # recreate text
            time_counter -= 1
            text = font_type.render('You got: ' + str(time_counter), True, timer_color)
        pygame.display.update()

    while not game_over:

        while game_close == True:
            final_score = str(snake_length - 1)
            dump_file_save(final_score)

            message('You lost!', 'q - quit game', 'p - play again', 's - last 5 scores', close_screen_text1,
                    close_screen_text2, close_screen_text3, close_screen_text4)


            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        main()
                    if event.key == pygame.K_s:
                        top_text = 'Last 5 scores:'
                        scr_line1 = file_open(1)
                        scr_line2 = file_open(2)
                        scr_line2 = scr_line2.replace('\n', '')
                        scr_line3 = file_open(3)
                        scr_line3 = scr_line3.replace('\n', '')
                        scr_line4 = file_open(4)
                        scr_line4 = scr_line4.replace('\n', '')
                        scr_line5 = file_open(5)
                        scr_line5 = scr_line5.replace('\n', '')
                        score_msg(top_text, scr_line1, scr_line2, scr_line3, scr_line4, scr_line5, lastscore_color)
                        pygame.display.update()
                        time.sleep(4)
                        main()

            pygame.display.update()

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
# setting end
        elif snake_length == 0:
            game_close = True

# trying to add time dependig loose

        if time_counter == 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        display.fill(screen_color)

        pygame.draw.rect(display, food_for_snake_color, [food_for_snakex, food_for_snakey, snake_size, snake_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        # making 'move' - deleting first square
        if len(snake_list) > snake_length:
            del snake_list[0]

        # for x in snake_list[:-1]:
        #     if x == snake_head:
        #         game_close = True

        snake_current(snake_size, snake_list)
        player_score(snake_length)
        display.blit(text, [0, 0])
        pygame.display.update()

        score_to_save = 0

        if x1 == food_for_snakex and y1 == food_for_snakey:
            food_for_snakex = round(random.randrange(0, display_width - snake_size) / 10.0) * 10.0
            food_for_snakey = round(random.randrange(0, display_height - snake_size) / 10.0) * 10.0
            snake_length += 1
            print(snake_length)



        clock.tick(snake_speed)
    file_save()
    pygame.quit()

    quit()


if __name__ == '__main__':
    main()

