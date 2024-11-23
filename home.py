# Example file showing a basic pygame "game loop"
import pygame
import time
from main import load_ava,map_import
from colorama import Back,Style,Fore
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
test_font = pygame.font.Font('font/Pixeltype.ttf',155)
test_font_1 = pygame.font.Font('font/Pixeltype.ttf',139)
other_text_font = pygame.font.Font('font/Pixeltype.ttf',34)
text_box_timer = 0


Screen_W,Screen_H = 1280,720

def str_split(str,splitter):
    str_list  = []
    temp_str = ""
    timer = 0
    # appends the rest into a list
    for char in str:
        timer +=1
        temp_str = temp_str + char
        if len(temp_str) == splitter:
            str_list.append(temp_str)
            temp_str = ""
            

    if len(temp_str) > 0:
        str_list.append(temp_str)




    return str_list


from random import randrange



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

ava = last_idle
ava_start_list = ["400,600","750,630","800,600","800,600","800,600","500,600","500,600","500,600","540,590","880,300","545,600","545,600","545,600","545,600","1100,600","700,600","600,600"]
text_timer = 0
map_list = ["maps/map.txt", "maps/map1.5.txt" , "maps/map3.txt", "maps/map3.5.txt", "maps/map3.6.txt"  , "maps/map4.txt",  "maps/4.5.txt","maps/map5.txt", "maps/map5.1.txt","maps/map5.2.txt", "maps/map5.3.txt", "maps/map5.4.txt", "maps/map5.5.txt", "maps/map6.txt","maps/map6.1.txt","maps/map6.2.txt","maps/map6.3.txt"]
map_index = 0
tile_lister = ["1","1","1","1","1","1","1","2" ,"2" ,"2" ,"2"   ,"2","2","3","3","3","3"]
x,y = ava_start_list[map_index].split(",")
x,y = int(x),int(y)
avaX,avaY = x,y
ava_rect = ava.get_rect(center = (avaX,avaY))
ava_rect = ava.get_rect(center = (avaX,avaY))
ava.set_colorkey('White') 

class tile_set_1:
    ice = pygame.image.load("tiles/ground3.png").convert_alpha()
    snow = pygame.image.load("tiles/ground1.png").convert_alpha()
    water = pygame.image.load("tiles/water.png").convert_alpha()
    cobble_stone = pygame.image.load("tiles/ground2.png").convert_alpha()
    plank = pygame.image.load("tiles/plank.png").convert_alpha()
    forest_1 = pygame.image.load("tiles./F1.png").convert_alpha()
    forest_2 = pygame.image.load("tiles/F2.png").convert_alpha()
    tile_dict = {"@": ice, " " : snow, "$" : water, "E": cobble_stone, "#": cobble_stone, "A" :cobble_stone, "L": plank, "D" : plank,'%':plank
    ,"F": forest_1,"f":forest_2 }
    walls = ["$","@","F","f"]
    exits = ["E","L"]
    entrance = ['A','D']

class tile_set_2:
    ice = pygame.image.load("tiles/ground3.png").convert_alpha()
    snow = pygame.image.load("tiles/ground1.png").convert_alpha()
    cobble_stone = pygame.image.load("tiles/ground2.png").convert_alpha()
    wall1 = pygame.image.load("factory_tiles/wall1.jpg").convert_alpha()
    wall2 = pygame.image.load("factory_tiles/wall2.jpg").convert_alpha()
    wall3 = pygame.image.load("factory_tiles/wall3.jpg").convert_alpha()
    wall4 = pygame.image.load("factory_tiles/wall4.jpg").convert_alpha()
    factoryfloor1 = pygame.image.load("factory_tiles/Factoryfloor1.jpg").convert_alpha()
    factoryfloor2 = pygame.image.load("factory_tiles/Factoryfloor2.jpg").convert_alpha()
    factoryfloor3 = pygame.image.load("factory_tiles/Factoryfloor3.jpg").convert_alpha()
    corner1 = pygame.image.load("factory_tiles/Corner1.jpg").convert_alpha()
    corner2 = pygame.image.load("factory_tiles/Corner2.jpg").convert_alpha()
    corner3 = pygame.image.load("factory_tiles/Corner3.jpg").convert_alpha()
    corner4 = pygame.image.load("factory_tiles/Corner4.jpg").convert_alpha()
    blacky = pygame.image.load("factory_tiles/black.jpg").convert_alpha()
    tile_dict = { "Z" : corner1, "z" : corner2, "X": corner3, "x" : corner4, "N" :wall1, "n" : wall2, "M" : wall3, "m" : wall4,"B" :factoryfloor1, "b" : factoryfloor2, "V" : factoryfloor3, "y" : factoryfloor1, "Y": factoryfloor1, " ": blacky, "@": ice,"#" : cobble_stone, "A" : cobble_stone , "t": snow}
    walls = ["Z","z","X","x","N","n","M","m"]
    exits = ["Y"]
    entrance = ["y","A"]

class tile_set_3:
    rfloor1 = pygame.image.load("research_tile/Rfloor1.jpg").convert_alpha()
    rfloor2 = pygame.image.load("research_tile/Rfloor2.jpg").convert_alpha()
    rfloor3 = pygame.image.load("research_tile/Rfloor3.jpg").convert_alpha()
    rwall1 = pygame.image.load("research_tile/Rwall1.jpg").convert_alpha()
    rwall2 = pygame.image.load("research_tile/Rwall2.jpg").convert_alpha()
    rwall3 = pygame.image.load("research_tile/Rwall3.jpg").convert_alpha()
    rwall4 = pygame.image.load("research_tile/Rwall4.jpg").convert_alpha()
    blacky = pygame.image.load("factory_tiles/black.jpg").convert_alpha()
    tile_dict = {"J" : rfloor1, "j" : rfloor2, "K" : rfloor3, "O": rwall1, "o" : rwall2, "P" : rwall3, "p" : rwall4, "U": rfloor1, "u" : rfloor1, " " : blacky}
    walls = ["O","o","P","p"]
    exits = ["U"]
    entrance = ["u"]
    #{"J": tiles/Rfloor1.jpg, "j": tiles/Rfloor2.jpg, "K": tiles/Rfloor3.jpg, "O": tiles/Rwall1.jpg, "o": tiles/Rwall2.jpg, "P": tiles/Rwall3.jpg, "p": tiles/Rwall4.jpg, "U": tiles/Rfloor1.jpg, "u": tiles/Rfloor1.jpg,}
class Music_list:
    scroll_sound = pygame.mixer.Sound('music/text_type.wav')
    title = pygame.mixer.Sound('music/home.mp3')
    chill = pygame.mixer.Sound("music/chill.mp3")
    scary = pygame.mixer.Sound("music/scary.mp3")
    playlist = [chill,chill,chill,chill,chill,chill,chill     ,scary,scary,scary,scary,scary,scary,scary,scary,scary,scary]
    
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
    #------------------------------------------------------------------------------------------------------------

    final_image_list = [ image_list_1, [],[], [], [], [], [],[],[],[],[],[],[],[],[],[],[],[] ]
    final_rect_list = [  rect_list_1, [],[], [], [], [], [] ,[],[] ,[],[],[],[],[],[],[],[] ]
    #--------------------------------------------------------------------------------------------------

class dialogue:
    # map 1 dialogue
    a0 = "........................"
    a1 = "........................"
    list_a = [a0,a1]
    #----------------------------------------------------------------------------
    final_list = [list_a,[]]


Music_list.title.play(-1)


def draw_map():
    global map_list
    global map_index
    global tile_set_1
    tile_set =    eval( current_tile_set + ".tile_dict" )     # tile_set_1.tile_dict
    walls =     eval( current_tile_set + ".walls" )                      ## tile_set_1.walls
    exits =           eval(current_tile_set + ".exits")               #tile_set_1.exits
    entrance =         eval(current_tile_set + ".entrance")                        # tile_set_1.entrance
    wall_rect_list = []
    exit_rect_list = []
    entrance_rect_list = []
    special_list = []
    map = map_import(map_list[map_index],1280,720)

    
    for row in map:
        for item in row:
            tile = tile_set[ row[item] ]
            wally = tile.get_rect(topleft = item)
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
battle_opt = 0
while running:
    #battle_opt +=0.01 move this to overwold state latger

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
        #battle_opt +=0.02
        if int(battle_opt) >= 5:
            battle_opt = 0
            choice = randrange(0,2)
            if choice == 0:
                pass
            else:
                home_state = "combat"
   

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False

    # loads map

        tiler = tile_lister[map_index]
        current_tile_set =  "tile_set_" + tiler
        screen.fill("Pink")
        mapy,wall_list,exit_list,entrance_list,special_lists = draw_map()
      # gets ava cords
        ava_rect = ava.get_rect(center = (avaX,avaY))
        
        print(map_list[map_index])



    
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
                dialogue_list  = str_split(dialogue_str,180) 
                
            
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
            
            if event.type == pygame.KEYDOWN  :
                        
                if event.key == pygame.K_SPACE and int(dialogue_timer) > 180:
                    pygame.draw.rect(screen,"black",back_bg_1)
                    pygame.draw.rect(screen,"black",back_bg_2)
                    pygame.draw.rect(screen,"black",back_bg_3)

                    dialogue_timer = 0 
                    text_box_timer +=1

                elif event.key == pygame.K_SPACE:
                    pygame.time.wait(30)
                    home_state = 0
                    text_box_timer = 0

    

        current_dialogue = dialogue_list[text_box_timer]
        if int(dialogue_timer) == len(dialogue_str) +1:
            pass

        else:
            temp_text = current_dialogue[: int(dialogue_timer)]

            
            
            
            
            dialogue_timer +=0.2
            # background rectange
            back_txt = "2" * 65
            back_txt_py = other_text_font.render(back_txt,False,"Black")
            back_bg_1 = back_txt_py.get_rect(midbottom = (640,40))
            back_bg_1 = back_bg_1.inflate(30,20)
            back_bg_2 = back_txt_py.get_rect(midbottom = (640,80))
            back_bg_2 =  back_bg_2.inflate(30,20)
            back_bg_3 = back_txt_py.get_rect(midbottom = (640,120))
            back_bg_3 = back_bg_3.inflate(30,20)
            
            #pygame.draw.rect(screen,"Black",back_txt_rect)


            
            if int(dialogue_timer) <= 60 or int(dialogue_timer) >=60:
                Music_list.scroll_sound.play(0)
                if len(temp_text) < 60:
                    text_1 = temp_text
                else:
                    text_1 = current_dialogue[: 60]
                dialogue_game = other_text_font.render(text_1,False,"White")
                dialogue_rect = dialogue_game.get_rect(midbottom = (640,40))
                pygame.draw.rect(screen,"Black",back_bg_1)
                screen.blit(dialogue_game,dialogue_rect)
            if int(dialogue_timer) > 60:
                if int(dialogue_timer) < 120:
                    text_2 = current_dialogue[60 : int(dialogue_timer)]
                else:
                    text_2 = current_dialogue[60: 120]
                text_2 = other_text_font.render(text_2,False,"White")
                dialogue_rect_2 = dialogue_game.get_rect(midbottom = (640,80))
                pygame.draw.rect(screen,"Black",back_bg_2)
                screen.blit(text_2,dialogue_rect_2)
            
            if int(dialogue_timer) > 120:
                text_3 = current_dialogue[120: int(dialogue_timer)]
                text_3 = other_text_font.render(text_3,False,"White")
                dialogue_rect_3 = dialogue_game.get_rect(midbottom = (640,120))
                pygame.draw.rect(screen,"Black",back_bg_3)
                screen.blit(text_3,dialogue_rect_3)



    if home_state == "combat":
        # PUT COMBAT LOGIC HERE: YOU CAN REPLACE THE STUFF HERE
        screen.fill("Pink")
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    home_state = 0
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()



#NOTES
# AVAS TOP TRIANGLE IS TOO HIGH
# HER LEFT AND RIGHT WORK FINE
# BOTTOM IS TWEAKING

