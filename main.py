import pygame
from sprite import Spritesheet

# Initialize Pygame and create window
pygame.init()
DISPLAY_W, DISPLAY_H = 1700, 1200
canvas = pygame.Surface((DISPLAY_W, DISPLAY_H))
window = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
running = True

ava_right1 = pygame.image.load('Ava/Ava_right1.png').convert_alpha()
ava_right2 = pygame.image.load('Ava/Ava_right2.png').convert_alpha()
ava_right3 = pygame.image.load('Ava/Ava_right3.png').convert_alpha()
ava_right4 = pygame.image.load('Ava/Ava_right4.png').convert_alpha()
ava_right5 = pygame.image.load('Ava/Ava_right5.png').convert_alpha()
ava_right6 = pygame.image.load('Ava/Ava_right6.png').convert_alpha()

ava_left1 = pygame.image.load('Ava/Ava_left1.png').convert_alpha()
ava_left2 = pygame.image.load('Ava/Ava_left2.png').convert_alpha()
ava_left3 = pygame.image.load('Ava/Ava_left3.png').convert_alpha()
ava_left4 = pygame.image.load('Ava/Ava_left4.png').convert_alpha()
ava_left5 = pygame.image.load('Ava/Ava_left5.png').convert_alpha()
ava_left6 = pygame.image.load('Ava/Ava_left6.png').convert_alpha()

ava_up1 = pygame.image.load('Ava/Ava_up1.png').convert_alpha()
ava_up2 = pygame.image.load('Ava/Ava_up2.png').convert_alpha()
ava_up3 = pygame.image.load('Ava/Ava_up3.png').convert_alpha()
ava_up4 = pygame.image.load('Ava/Ava_up4.png').convert_alpha()
ava_up5 = pygame.image.load('Ava/Ava_up5.png').convert_alpha()
ava_up6 = pygame.image.load('Ava/Ava_up6.png').convert_alpha()

ava_down1 = pygame.image.load('Ava/Ava_down1.png').convert_alpha()
ava_down2 = pygame.image.load('Ava/Ava_down2.png').convert_alpha()
ava_down3 = pygame.image.load('Ava/Ava_down3.png').convert_alpha()
ava_down4 = pygame.image.load('Ava/Ava_down4.png').convert_alpha()
ava_down5 = pygame.image.load('Ava/Ava_down5.png').convert_alpha()
ava_down6 = pygame.image.load('Ava/Ava_down6.png').convert_alpha()

ava_idle_right = pygame.image.load('Ava/Ava_idle_right.png')
ava_idle_left = pygame.image.load('Ava/Ava_idle_left.png')

ava_right = [ava_right1, ava_right2, ava_right3, ava_right4, ava_right5, ava_right6]
ava_left = [ava_left1, ava_left2, ava_left3, ava_left4, ava_left5, ava_left6]
ava_up = [ava_up1, ava_up2, ava_up3, ava_up4, ava_up5, ava_up6]
ava_down = [ava_down1, ava_down2, ava_down3, ava_down4, ava_down5, ava_down6]

index = 0

last_idle = ava_idle_right
ava = last_idle

avaX = DISPLAY_W/2
avaY = DISPLAY_H/2

ava_rect = ava.get_rect(center = (avaX, avaY))
ava.set_colorkey('White')


def Ava_size():
    global ava
    ava = pygame.transform.rotozoom(ava,0,5)




def Animate():
    global index, last_idle, ava
    if key == False:
        ava = last_idle
        Ava_size()
        ava.set_colorkey('White')
    elif direction == 'right':
        index += 0.1
        if index >= len(ava_right): index=0
        ava = ava_right[int(index)]
        last_idle = ava_idle_right
        ava.set_colorkey('White')
        Ava_size()
    elif direction == 'left':
        index += 0.1
        if index >= len(ava_left): index=0
        ava = ava_left[int(index)]
        ava.set_colorkey('White')
        Ava_size()
        last_idle = ava_idle_left
    elif direction == 'up':
        index += 0.1
        if index >= len(ava_up): index=0
        ava = ava_up[int(index)]
        ava.set_colorkey('White')
        Ava_size()
        last_idle = ava_up2
    elif direction == 'down':
        index += 0.1
        if index >= len(ava_down): index=0
        ava = ava_down[int(index)]
        ava.set_colorkey('White')
        Ava_size()
        last_idle = ava_down2

index = 0
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False


    window.fill((0,0,0))

    

    window.blit(ava,(avaX,avaY))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        avaX -=10
        print("left")
        key = True
        direction = 'left'
    elif keys[pygame.K_d]:
        avaX +=10
        print("right")
        key = True
        direction = 'right'
    elif keys[pygame.K_w]:
        avaY -=10
        print("up")
        key = True
        direction = 'up'
    elif keys[pygame.K_s]:
        avaY +=10
        print("down")
        key = True
        direction = 'down'
    else:
        key = False

    Animate()



    clock.tick(60)
    pygame.display.update()

    

pygame.quit()
