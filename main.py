import pygame as pg

# Initialize pg and create window
pg.init()
DISPLAY_W, DISPLAY_H = 1700, 1200
canvas = pg.Surface((DISPLAY_W, DISPLAY_H))
window = pg.display.set_mode((DISPLAY_W, DISPLAY_H))
running = True

#takes images from directory (we need to learn how to use spritesheets instead of this)
ava_right1 = pg.image.load('Ava/Ava_right1.png').convert_alpha()
ava_right2 = pg.image.load('Ava/Ava_right2.png').convert_alpha()
ava_right3 = pg.image.load('Ava/Ava_right3.png').convert_alpha()
ava_right4 = pg.image.load('Ava/Ava_right4.png').convert_alpha()
ava_right5 = pg.image.load('Ava/Ava_right5.png').convert_alpha()
ava_right6 = pg.image.load('Ava/Ava_right6.png').convert_alpha()

ava_left1 = pg.image.load('Ava/Ava_left1.png').convert_alpha()
ava_left2 = pg.image.load('Ava/Ava_left2.png').convert_alpha()
ava_left3 = pg.image.load('Ava/Ava_left3.png').convert_alpha()
ava_left4 = pg.image.load('Ava/Ava_left4.png').convert_alpha()
ava_left5 = pg.image.load('Ava/Ava_left5.png').convert_alpha()
ava_left6 = pg.image.load('Ava/Ava_left6.png').convert_alpha()

ava_up1 = pg.image.load('Ava/Ava_up1.png').convert_alpha()
ava_up2 = pg.image.load('Ava/Ava_up2.png').convert_alpha()
ava_up3 = pg.image.load('Ava/Ava_up3.png').convert_alpha()
ava_up4 = pg.image.load('Ava/Ava_up4.png').convert_alpha()
ava_up5 = pg.image.load('Ava/Ava_up5.png').convert_alpha()
ava_up6 = pg.image.load('Ava/Ava_up6.png').convert_alpha()

ava_down1 = pg.image.load('Ava/Ava_down1.png').convert_alpha()
ava_down2 = pg.image.load('Ava/Ava_down2.png').convert_alpha()
ava_down3 = pg.image.load('Ava/Ava_down3.png').convert_alpha()
ava_down4 = pg.image.load('Ava/Ava_down4.png').convert_alpha()
ava_down5 = pg.image.load('Ava/Ava_down5.png').convert_alpha()
ava_down6 = pg.image.load('Ava/Ava_down6.png').convert_alpha()

ava_idle_right = pg.image.load('Ava/Ava_idle_right.png')
ava_idle_left = pg.image.load('Ava/Ava_idle_left.png')

#compiles each direction into a list
ava_right = [ava_right1, ava_right2, ava_right3, ava_right4, ava_right5, ava_right6]
ava_left = [ava_left1, ava_left2, ava_left3, ava_left4, ava_left5, ava_left6]
ava_up = [ava_up1, ava_up2, ava_up3, ava_up4, ava_up5, ava_up6]
ava_down = [ava_down1, ava_down2, ava_down3, ava_down4, ava_down5, ava_down6]

#default idle
last_idle = ava_down2
ava = last_idle

#adjustable coordinates
avaX = DISPLAY_W/2
avaY = DISPLAY_H/2

def Offscreen_check(ifXY):
    global avaX, avaY
    if ifXY == 'X' or ifXY == 'XY':
        if avaX <= -100:
            avaX = DISPLAY_W
        elif avaX >= DISPLAY_W + 100:
            avaX = -90
    if ifXY == 'Y' or ifXY == 'XY':
        if avaY <= -10:
            avaY = DISPLAY_W
        elif avaY >= DISPLAY_W + 10:
            avaY = 0


#ava hitbox and coordinate manager
ava_rect = ava.get_rect(center = (avaX, avaY))
ava.set_colorkey('White')

#to scale later
def Ava_size():
    global ava
    ava = pg.transform.rotozoom(ava,0,5)


#if key is pressed
key = False

def Animate():
    
    global index, last_idle, ava

    #reverts to idle if no key is pressed
    if key == False:
        ava = last_idle
        Ava_size()
        ava.set_colorkey('White')

    #animates using one of the lists based on the direction
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

#index for iteration
index = 0

#initializes frame rate manager
clock = pg.time.Clock()

while running:
    #quits the game if window is closed
    for event in pg.event.get():
        if event.type == pg.QUIT: running = False

    #fills screen with black so that previous frames are erased
    window.fill((0,0,0))

    
    #places character
    window.blit(ava,(avaX,avaY))

    #listens for key press
    keys = pg.key.get_pressed()
    if keys[pg.K_a]:
        avaX -=10
        print("left")
        key = True
        direction = 'left'
    elif keys[pg.K_d]:
        avaX +=10
        print("right")
        key = True
        direction = 'right'
    elif keys[pg.K_w]:
        avaY -=10
        print("up")
        key = True
        direction = 'up'
    elif keys[pg.K_s]:
        avaY +=10
        print("down")
        key = True
        direction = 'down'
    else:
        key = False

    Animate()
    #Offscreen_check('XY')

    #manages frame rate (60fps)
    clock.tick(60)

    #updates the display
    pg.display.update()

pg.quit()