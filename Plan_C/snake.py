import pygame

seashell3 = (205, 197, 191)
limegreen = (50, 205, 50)
red = (255, 0, 0)

pygame.init()
display = pygame.display.set_mode((600, 400))
display.fill(seashell3)
pygame.display.update()
pygame.display.set_caption('Plan C - if everything else fails')



gameover = False
while not gameover:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
        print(event)
pygame.quit()
quit()

