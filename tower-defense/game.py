import pygame
import os

pygame.init()

win_height = 1000
win_width = 500
win = pygame.display.set_mode((win_height, win_width))
pygame.display.set_caption("Gate keepers")
bg = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Background.png")), (win_height,win_width))
bullet_img = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Bullets", "buller.png")), (10, 10))


# Load Images of the Character (there are two popular ways)
stationary = pygame.image.load(os.path.join("Assets/Hero", "standing.png"))
# One way to do it - using the sprites that face left.

left =  [pygame.image.load(os.path.join("Assets/Hero", "L1.png")),
         pygame.image.load(os.path.join("Assets/Hero", "L2.png")),
         pygame.image.load(os.path.join("Assets/Hero", "L3.png")),
         pygame.image.load(os.path.join("Assets/Hero", "L4.png")),
         pygame.image.load(os.path.join("Assets/Hero", "L5.png")),
         pygame.image.load(os.path.join("Assets/Hero", "L6.png")),
         pygame.image.load(os.path.join("Assets/Hero", "L7.png")),
         pygame.image.load(os.path.join("Assets/Hero", "L8.png")),
         pygame.image.load(os.path.join("Assets/Hero", "L9.png"))]

right = [pygame.image.load(os.path.join("Assets/Hero", "R1.png")),
         pygame.image.load(os.path.join("Assets/Hero", "R2.png")),
         pygame.image.load(os.path.join("Assets/Hero", "R3.png")),
         pygame.image.load(os.path.join("Assets/Hero", "R4.png")),
         pygame.image.load(os.path.join("Assets/Hero", "R5.png")),
         pygame.image.load(os.path.join("Assets/Hero", "R6.png")),
         pygame.image.load(os.path.join("Assets/Hero", "R7.png")),
         pygame.image.load(os.path.join("Assets/Hero", "R8.png")),
         pygame.image.load(os.path.join("Assets/Hero", "R9.png"))]



class hero:
    def __init__(self,x,y):
        #walk
        self.x = x
        self.y = y
        self.velx =10
        self.vely =10
        self.face_right = True
        self.face_left = False
        self.stepIndex = 0
        #jump
        self.jump = False
        #shoot
        self.bullets = []
        self.cool_down_count = 0

    def move_hero(self,userInput):
        if userInput[pygame.K_RIGHT] and self.x <= 950:
            self.x += self.velx
            self.face_right = True
            self.face_left = False
        elif userInput[pygame.K_LEFT] and self.x >= 0:
            self.x -= self.velx
            self.face_right = False
            self.face_left = True
        else:
            self.stepIndex = 0

    def draw(self,win):
        if self.stepIndex >= 9:
            self.stepIndex = 0
        elif self.face_left:
            win.blit(left[self.stepIndex],(self.x,self.y))
            self.stepIndex += 1
        if self.face_right:
            win.blit(right[self.stepIndex],(self.x,self.y))
            self.stepIndex += 1

    def jump_motion(self,userInput):
        if userInput[pygame.K_SPACE] and self.jump is False:
            self.jump = True
        if self.jump is True:
            self.y -= self.vely * 2
            self.vely -= 1
        if self.vely < -10:
            self.jump = False
            self.vely = 10

    def direction(self):
        if self.face_right:
            return 1
        if self.face_left:
            return -1

    def cooldown(self):
        if self.cool_down_count >= 10:
            self.cool_down_count = 0
        elif self.cool_down_count > 0:
            self.cool_down_count += 1

    def shoot(self):
        self.cooldown()
        if userInput[pygame.K_e] and self.cool_down_count == 0:
            bullet = Bullet(self.x,self.y, self.direction())
            self.bullets.append(bullet)
            self.cool_down_count = 1
        for bullet in self.bullets:
            bullet.move()
            if bullet.off_screen():
                self.bullets.remove(bullet)

#for bullets
class Bullet:
    def __init__(self,x,y,direction):
        self.x =x + 25
        self.y =y + 35
        self.direction = direction


    def draw_bullet(self):
        win.blit(bullet_img,(self.x,self.y))

    def move(self):
       if self.direction == 1:
           self.x += 15
       if self.direction == -1:
           self.x -= 15

    def off_screen(self):
        return not(self.x >= 0 and self.x <= 800)


def draw_game():
    win.fill((0,0,0))
    win.blit(bg, (0, 0))
    player.draw(win)
    for bullet in player.bullets:
        bullet.draw_bullet()
    pygame.time.delay(30)
    pygame.display.update()


player = hero(250,370)


#mainloop
run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #input
    userInput = pygame.key.get_pressed()

    #shoot
    player.shoot()

    #movement
    player.move_hero(userInput)
    player.jump_motion(userInput)

    #draw game in window
    draw_game()

