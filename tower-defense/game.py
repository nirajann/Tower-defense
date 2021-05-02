import pygame

pygame.init()

height = 600
width = 600
win = pygame.display.set_mode((height,width))
pygame.display.set_caption("Gate keepers")

x = 300
y = 300
radius = 15
vel = 10
run = True

while run:

    win.fill((0,0,0))
    pygame.draw.circle(win,(255, 255, 255),(int(x),int(y)),radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #this code is used for movement and keeping the object inside boundires
    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_LEFT] and x > 0:
        x -= vel
    if userInput[pygame.K_RIGHT] and x  < 600:
        x += vel
    if userInput[pygame.K_UP] and y > 0:
        y -= vel
    if userInput[pygame.K_DOWN] and  y < 600:
        y += vel

    pygame.time.delay(10)


    pygame.display.update()
