# this code is used for movement and keeping the object inside boundires
userInput = pygame.key.get_pressed()
if userInput[pygame.K_LEFT] and x > 0:
    x -= vel
if userInput[pygame.K_RIGHT] and x < 600:
    x += vel
if userInput[pygame.K_UP] and y > 0:
    y -= vel
if userInput[pygame.K_DOWN] and y < 600:
    y += vel

pygame.time.delay(10)