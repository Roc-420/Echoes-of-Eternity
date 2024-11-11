import pygame
from sprite import Spritesheet

# Initialize Pygame and create window
pygame.init()
DISPLAY_W, DISPLAY_H = 1000, 800
canvas = pygame.Surface((DISPLAY_W, DISPLAY_H))
window = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
running = True

ava_right1 = pygame.image.load('Ava/Ava_right1.png').convert_alpha()
ava_right2 = pygame.image.load('Ava/Ava_right2.png').convert_alpha()
ava_right3 = pygame.image.load('Ava/Ava_right3.png').convert_alpha()
ava_right4 = pygame.image.load('Ava/Ava_right4.png').convert_alpha()
ava_right5 = pygame.image.load('Ava/Ava_right5.png').convert_alpha()
ava_right6 = pygame.image.load('Ava/Ava_right6.png').convert_alpha()
#ava_idle_scaled = pygame.transform.scale(ava_idle,(16,16))
ava_idle = pygame.image.load('Ava/Ava_idle_right.png')
ava_right = [ava_right1, ava_right2, ava_right3, ava_right4, ava_right5, ava_right6]
index = 0
ava = ava_right[int(index)]

avaX = DISPLAY_W/2
avaY = DISPLAY_H/2

ava_rect = ava.get_rect(center = (avaX, avaY))
ava.set_colorkey('White')
ava = pygame.transform.rotozoom(ava,0,7)






def Animate():
    global index, ava
    if key == False:
        ava = ava_idle
        ava = pygame.transform.rotozoom(ava,0,7)
        ava.set_colorkey('White')
    else:
        index += 0.1
        if index >= len(ava_right): index=0
        ava = ava_right[int(index)]
        ava.set_colorkey('White')
        ava = pygame.transform.rotozoom(ava, 0, 7)

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
    elif keys[pygame.K_d]:
        avaX +=10
        print("right")
        key = True
    elif keys[pygame.K_w]:
        avaY -=10
        print("up")
        key = True
    elif keys[pygame.K_s]:
        avaY +=10
        print("down")
        key = True
    else:
        key = False

    Animate()



    clock.tick(60)
    pygame.display.update()

    

pygame.quit()

