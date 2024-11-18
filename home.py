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
other_text_font = pygame.font.Font('font/Pixeltype.ttf',34)

text_timer = 0
map_list = ["maps/map.txt","maps/map3.txt"]
map_index = 0



# home screen status variables
home_screen_text = 0 # stops generation if text = 0
home_state = 1
start_state = 1
end_state = 0
ava_right,ava_left, ava_up, ava_down, last_idle, ava, ava_idle_left, ava_idle_right =load_ava()
index = 0
trans_timer  = 0

def collide_check(player_rect,wall_rect_list,directions):
    if directions == "right":
        player_rect.x +=5
    elif directions == "left":
        player_rect.x -=5
    elif directions == "up":
        player_rect.y -=5
    elif directions == "down":
        player_rect.y +=5
    else:
        pass
    for wall in  wall_rect_list:
        if player_rect.colliderect(wall):
            return wall
        
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

avaX = 400
avaY = 600
ava = last_idle
ava_start_list = ["400,600","750,630"]
ava_rect = ava.get_rect(center = (avaX,avaY))
ava.set_colorkey('White') 

class tile_set_1:
    ice = pygame.image.load("tiles/ground3.png").convert_alpha()
    snow = pygame.image.load("tiles/ground1.png").convert_alpha()
    water = pygame.image.load("tiles/water.png").convert_alpha()
    cobble_stone = pygame.image.load("tiles/ground2.png").convert_alpha()
    plank = pygame.image.load("tiles/plank.png").convert_alpha()
    tile_dict = {"@": ice, " " : snow, "$" : water, "E": cobble_stone, "#": cobble_stone, "A" :cobble_stone, "L": plank, "D" : plank,'%':plank}
    default = snow
    walls = ["$","@"]
    exits = ["E","L"]
    entrance = ['A','D']
    
class Music_list:
    scroll_sound = pygame.mixer.Sound('music/text_type.wav')
    title = pygame.mixer.Sound('music/title.mp3')
    over_world_1 = pygame.mixer.Sound("music/lost_woods.mp3")
    playlist = [over_world_1,over_world_1]
    
class special_sprite_set:
    # map 1 assets
    tree = pygame.image.load("special_sprite/Tree.png")
    tree = pygame.transform.rotozoom(tree,0,2)
    tree_rect = tree.get_rect(center = (700,500))
    cabin = pygame.image.load("special_sprite/Cabin.png")
    cabin = pygame.transform.rotozoom(cabin,0,2)
    cabin_rect = cabin.get_rect( center =  (1000,300))   
    image_list_1 = [tree,cabin]
    rect_list_1 = [tree_rect,cabin_rect]

    final_image_list = [ image_list_1, [] ]
    final_rect_list = [  rect_list_1, []   ]
    #--------------------------------------------------------------------------------------------------

class dialogue:
    # map 1 dialogue
    a0 = "A very long tree blocking the sun"
    a1 = "A worn down cabin, with numerous repairs and patches, with materials no longer found upon this planet or any other "
    list_a = [a0,a1]
    #----------------------------------------------------------------------------
    final_list = [list_a,[]]


Music_list.title.play(-1)


def draw_map():
    global map_list
    global map_index
    global tile_set_1
    tile_set = tile_set_1.tile_dict
    walls = tile_set_1.walls
    exits = tile_set_1.exits
    entrance = tile_set_1.entrance
    wall_rect_list = []
    exit_rect_list = []
    entrance_rect_list = []
    special_list = []
    default = tile_set_1.default
    map = map_import(map_list[map_index],1280,720)

    
    for row in map:
        for item in row:
            tile = tile_set[ row[item] ]
            wally = tile.get_rect(topleft = item)
            screen.blit(default,wally)
            screen.blit(tile,wally)
            if row[item] in walls:
                wall_rect_list.append(wally)
            elif row[item] in exits:
                exit_rect_list.append(wally)
            elif row[item] in entrance:
                entrance_rect_list.append(wally)
    for image,rect in zip(special_sprite_set.final_image_list[map_index],special_sprite_set.final_rect_list[map_index]):
        screen.blit(image,rect)
        special_list.append(rect)
        wall_rect_list.append(rect)
   
    return map, wall_rect_list, exit_rect_list, entrance_rect_list, special_list

    
   
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
                        Music_list.title.stop()
                        Music_list.playlist[map_index].play(-1)
                    
                        
                    else:
                        pygame.quit()

    if home_state == 0: # overwold state, map exploration  here
        print(map_index,avaX,avaY)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False

    # loads map

    
        mapy,wall_list,exit_list,entrance_list,special_lists = draw_map()
      # gets ava cords
        ava_rect = ava.get_rect(center = (avaX,avaY))

        



    
    #places character
        screen.blit(ava,ava_rect)

    #listens for key press
        keys = pygame.key.get_pressed()
        

        if collide_check(ava_rect,exit_list,directions="None"):      
            if   Music_list.playlist[map_index] !=  Music_list.playlist[map_index + 1]:
                Music_list.playlist[map_index].stop()
                map_index +=1
                Music_list.playlist[map_index].play(-1)
            else:
                map_index +=1
            
    
        if collide_check(ava_rect,entrance_list,directions="None"):      
            if   Music_list.playlist[map_index] !=  Music_list.playlist[map_index - 1]:
                Music_list.playlist[map_index].stop()
                map_index -=1
                Music_list.playlist[map_index].play(-1)
            else:    
                map_index -=1
        if collide_check(ava_rect,exit_list,directions="None") or collide_check(ava_rect,entrance_list,directions="None"):
            home_state = "trans"
            scroll = pygame.mixer.Sound('music/map_transfer.mp3')
            scroll.play(0)
            x,y = ava_start_list[map_index].split(",")
            x,y = int(x),int(y)
            avaX,avaY = x,y
            ava_rect = ava.get_rect(center = (avaX,avaY))
        
       
        elif keys[pygame.K_a]:
            
            if collide_check(ava_rect,wall_rect_list=wall_list,directions="left"):
                pass
            else:
                avaX -=2
            
            key = True 
            direction = 'left'
        elif keys[pygame.K_d]:
           
            if collide_check(ava_rect,wall_rect_list=wall_list,directions="right"):
                pass
            else:
                avaX +=2
            key = True
            direction = 'right'
        elif keys[pygame.K_w]:

            if collide_check(ava_rect,wall_rect_list=wall_list,directions="up"):
                pass
            else:
                avaY -=2
            if collide_check(ava_rect,wall_rect_list=wall_list,directions="up") in special_lists and keys[pygame.K_SPACE]:
                home_state = "dialogue"
                dialogue_timer = 0
                dialogue_option = special_lists.index(collide_check(ava_rect,wall_rect_list=wall_list,directions="up"))
                dialogue_str = dialogue.final_list[map_index][dialogue_option]
            
            key = True
            direction = 'up'
        elif keys[pygame.K_s]:
          
            if collide_check(ava_rect,wall_rect_list=wall_list,directions="down"):
                pass
            else:
                avaY +=2
            key = True
            direction = 'down'
        
        else:
            key = False

        Animate()

    if home_state == "trans":
        screen.fill("Black")
        trans_timer += 0.1
        if int(trans_timer) == 1:
            home_state = 0
            trans_timer = 0
          
    if home_state == "dialogue":
        
        for event in pygame.event.get():
            print("in event loop")

            if event.type == pygame.KEYDOWN  :
                        
                if event.key == pygame.K_SPACE:
                    pygame.time.wait(30)
                    home_state = 0

      
        if int(dialogue_timer) == len(dialogue_str) +1:
            pass

        else:
            temp_text = dialogue_str[: int(dialogue_timer)]
            dialogue_game = other_text_font.render(temp_text,False,"White")
            dialogue_rect = dialogue_game.get_rect(midbottom = (640,40))
            background_rect = dialogue_rect.inflate(30,20)
            
            pygame.draw.rect(screen,"Black",background_rect)
            
            screen.blit(dialogue_game,dialogue_rect)
            Music_list.scroll_sound.play(0)

            dialogue_timer +=0.2
            
            pygame.draw.rect(screen,"Black",background_rect)
            screen.blit(dialogue_game,dialogue_rect)


    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()



#NOTES
# AVAS TOP TRIANGLE IS TOO HIGH
# HER LEFT AND RIGHT WORK FINE
# BOTTOM IS TWEAKING

