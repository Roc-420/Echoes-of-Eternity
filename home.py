# Example file showing a basic pygame "game loop"
import pygame
import time
from main import load_ava,map_import

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
test_font = pygame.font.Font('font/Pixeltype.ttf',155)
test_font_1 = pygame.font.Font('font/Pixeltype.ttf',139)

text_timer = 0
map_list = ["maps/map.txt","maps/map2.txt"]
map_index = 0


# home screen status variables
home_screen_text = 0 # stops generation if text = 0
home_state = 1
start_state = 1
end_state = 0
ava_right,ava_left, ava_up, ava_down, last_idle, ava, ava_idle_left, ava_idle_right =load_ava()
index = 0

def home_screen():
    def title_screen():
        if start_state == 1:
            start_color = "#6D51B9"
        if start_state == 0:
            start_color = '#382A5E'
        if end_state == 1:
            end_color = "#6D51B9"
        if end_state == 0:
            end_color = '#382A5E'
        image = pygame.image.load('scenes/title.png')
        start_text = test_font_1.render('Start Game',False,'Black')
        start_rect = start_text.get_rect(midbottom = (640,360))
        quit_text = test_font_1.render('Quit Game',False,'Black')
        quit_rect = quit_text.get_rect(midbottom = (640,550))
        screen.blit(image,(0,0))
        pygame.draw.rect(screen,start_color,start_rect)
        pygame.draw.rect(screen,start_color,start_rect,border_radius=200)
        screen.blit(start_text,start_rect)
        pygame.draw.rect(screen,end_color,quit_rect)
        pygame.draw.rect(screen,end_color,quit_rect,20000000)
        screen.blit(quit_text,quit_rect)

    def text_generator(texts,pos):
        global text_timer
        global home_screen_text
        sound_effect = pygame.mixer.Sound('music/text_type.wav')
        


        text = texts[: int(text_timer)  ]
        if text == texts:
            home_screen_text = 1
        text_surface = test_font.render(text,False,'Black')
        text_rect = text_surface.get_rect(midbottom = pos)
        screen.blit(text_surface,text_rect)
        text_timer += 0.4
        
        
        
        return text
    
    title_text = "Echoes of Eternity"
    title_screen()
    
    if home_screen_text == 0:
        scroll = pygame.mixer.Sound('music/text_type.wav')
        scroll.play(0) 
        text_generator(title_text,(640,110))
        
    else:
        text_surface = test_font.render(title_text,False,'Black')
        text_rect = text_surface.get_rect(midbottom = (640,110))
        screen.blit(text_surface,text_rect)
    

    
#pygame.display.toggle_fullscreen()
music = pygame.mixer.Sound('music/title.mp3')
music.play(-1)
    
avaX = 500
avaY = 200
ava = last_idle
ava_rect = ava.get_rect(center = (avaX,avaY))
ava.set_colorkey('White') 




def draw_map():
    tile_set = { "#": "tiles/ground2.png", "A" : "tiles/ground3.png", " " : "tiles/ground1.png" ,"S" : "tiles/Tree.png"}
    default = "tiles/ground1.png"
    default = pygame.image.load(default).convert_alpha()
    screen.fill("White")
    map = map_import('maps/map.txt',1280,720)

    
    for row in map:
        for item in row:
            tile = pygame.image.load(tile_set[ row[item] ]).convert_alpha()
            screen.blit(default,item)
            screen.blit(tile,item)

    return map
    
   
def Ava_size():
    global ava
    ava = pygame.transform.rotozoom(ava,0,2)

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
        last_idle = ava_up[1]
    elif direction == 'down':
        index += 0.1
        if index >= len(ava_down): index=0
        ava = ava_down[int(index)]
        ava.set_colorkey('White')
        Ava_size()
        last_idle = ava_down[1]



while running:
   
    if home_state == 1:
        # generating text one word at a time
        home_screen()
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    scroll = pygame.mixer.Sound('music/move.mp3')
                    scroll.play(0)  
                if event.key == pygame.K_UP:
                    if end_state == 1:
                        end_state =0
                        start_state = 1
                    else:
                        pass
                if event.key == pygame.K_DOWN:
                    if start_state == 1:
                        start_state = 0
                        end_state = 1
                    else:
                        pass
                
                if event.key == pygame.K_SPACE:
                    select = pygame.mixer.Sound('music/select.mp3')
                    select.play(0)
                    if start_state == 1:

                        home_state = 0
                    else:
                        pygame.quit()

    if home_state == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False

    # loads map

    
        mapy = draw_map()


    
    #places character
        screen.blit(ava,(avaX,avaY))

    #listens for key press
        keys = pygame.key.get_pressed()
        
        
        if keys[pygame.K_a]:
            avaX -=10
            
            key = True
            direction = 'left'
        elif keys[pygame.K_d]:
            avaX +=10
            
            key = True
            direction = 'right'
        elif keys[pygame.K_w]:
            avaY -=10
            key = True
            direction = 'up'
        elif keys[pygame.K_s]:
            avaY +=10
            
            key = True
            direction = 'down'
        
        else:
            key = False

        Animate()


    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

