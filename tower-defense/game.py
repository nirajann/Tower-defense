import pygame

pygame.init()

height = 600
width = 600
win = pygame.display.set_mode((height,width))
pygame.display.set_caption("Gate keepers")


run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
