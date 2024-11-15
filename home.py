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
map_list = ["maps/map3.txt","maps/map2.txt"]
map_index = 0



# home screen status variables
home_screen_text = 0 # stops generation if text = 0
home_state = 1
start_state = 1
end_state = 0
ava_right,ava_left, ava_up, ava_down, last_idle, ava, ava_idle_left, ava_idle_right =load_ava()
index = 0


def collide_check(player_rect,wall_rect_list,directions):
    if directions == "right":
        player_rect.x +=10
    elif directions == "left":
        player_rect.x -=10
    elif directions == "up":
        player_rect.y -=10
    elif directions == "down":
        player_rect.y +=10
    else:
        pass
    for wall in  wall_rect_list:
        if player_rect.colliderect(wall):
            return True
        
    return False

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
    
avaX = 700
avaY = 200
ava = last_idle
ava_rect = ava.get_rect(center = (avaX,avaY))
ava.set_colorkey('White') 




def draw_map():
    global map_list
    global map_index
    tile_set = {  "@": "tiles/ground3.png", " " : "tiles/ground1.png", "$": "tiles/water.png", "E" : "tiles/ground2.png", "#" : "tiles/ground2.png"} 

    walls = ["$", "@",]
    exits = ['E']
    wall_rect_list = []
    exit_rect_list = []
    default = "tiles/ground1.png"
    default = pygame.image.load(default).convert_alpha()
    screen.fill("Black")
    print(map_index)
    map = map_import(map_list[map_index],1280,720)

    
    for row in map:
        for item in row:
            tile = pygame.image.load(tile_set[ row[item] ]).convert_alpha()
            wally = tile.get_rect(topleft = item)
            screen.blit(tile,wally)
            if row[item] in walls:
                wall_rect_list.append(wally)
            elif row[item] in exits:
                exit_rect_list.append(wally)
    return map, wall_rect_list, exit_rect_list

    
   
def Ava_size():
    global ava
    ava = pygame.transform.rotozoom(ava,0,2)
    print(avaX,avaY)

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

max_speed = 15

while running:
   
    if home_state == 1: # home screen state, 
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

    if home_state == 0: # overwold state, map exploration  here
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False

    # loads map

    
        mapy,wall_list,exit_list = draw_map()
      # gets ava cords
        ava_rect = ava.get_rect(center = (avaX,avaY))



    
    #places character
        screen.blit(ava,ava_rect)

    #listens for key press
        keys = pygame.key.get_pressed()
        
        
    
        if collide_check(ava_rect,exit_list,directions="None"):
            map_index +=1
            avaX = 200
            avaY = 600
            ava_rect = ava.get_rect(center = (avaX,avaY))
            screen.fill("Black")
            
        elif keys[pygame.K_a]:

            if collide_check(ava_rect,wall_rect_list=wall_list,directions="left"):
                pass
            else:
                avaX -=10
            
            key = True 
            direction = 'left'
        elif keys[pygame.K_d]:
           
            if collide_check(ava_rect,wall_rect_list=wall_list,directions="right"):
                pass
            else:
                avaX +=10
            key = True
            direction = 'right'
        elif keys[pygame.K_w]:
        
            if collide_check(ava_rect,wall_rect_list=wall_list,directions="up"):
                pass
            else:
                avaY -=10
            key = True
            direction = 'up'
        elif keys[pygame.K_s]:
          
            if collide_check(ava_rect,wall_rect_list=wall_list,directions="down"):
                pass
            else:
                avaY +=10
            key = True
            direction = 'down'
        
        else:
            key = False

        Animate()


    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()


#NOTES
# AVAS TOP TRIANGLE IS TOO HIGH
# HER LEFT AND RIGHT WORK FINE
# BOTTOM IS TWEAKING

