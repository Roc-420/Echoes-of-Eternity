# Example file showing a basic pygame "game loop"
import pygame
import time
from main import load_ava,map_import
from colorama import Back,Style,Fore
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
suprise_opt = True
test_font = pygame.font.Font('font/Pixeltype.ttf',155)
test_font_1 = pygame.font.Font('font/Pixeltype.ttf',139)
other_text_font = pygame.font.Font('font/Pixeltype.ttf',34)
text_box_timer = 0
suprise_counter = 0
from logue import dialogue
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
intro = 0


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
        text_generator(title_text,(640,110))
        
    else:
        text_surface = test_font.render(title_text,False,'Black')
        text_rect = text_surface.get_rect(midbottom = (640,110))
        screen.blit(text_surface,text_rect)
    
Screen_W, Screen_H = 1280, 720
screen = pygame.display.set_mode((Screen_W, Screen_H))

inpos = False
running = True

class Combater():
    def __init__(self, enemy, enemylvl, clvl, BGLOAD): #enemy being fought, Clvl - current level,
        self.BGLOAD = BGLOAD
        self.enemy = enemy
        self.enemylvl = enemylvl
        self.clvl = clvl

        self.enemy_multiplier = 1
        self.multiplier = 1

        #Name, HP (to be multiplied by level), moves
        
        self.hound_moves = {'Tackle':5, 'Bite':10}
        self.hound = ['Hound', 20, self.hound_moves]

        self.brute_moves = {'Smash':15, 'Charge':0}
        self.brute = ['Brute', 30, self.brute_moves]

        self.enemies = [self.hound, self.brute]
        
        for i in self.enemies:
            if self.enemy == i[0]:
                self.enemy = i
        print(self.enemy)

        self.HP = 20*int(self.clvl)
        self.current_HP = self.HP

        self.enemy_HP = 100 #int(self.enemy[1])*self.enemylvl      -    FIGURE OUT HOW TO GET SECOND ITEM IN THE LIST
        self.current_eHP = self.enemy_HP


        self.click = 0
        self.buttons = 'menu'

    def rect_init(self):
        self.BG = pygame.image.load(self.BGLOAD)
        self.BG = pygame.transform.scale(self.BG,(Screen_W, Screen_H))
        screen.blit(self.BG,(0,0))

        #platforms

        self.player_platform = pygame.image.load('scenes/Battle_platform.png')
        self.PPX = -300
        self.PPY = 500
        self.enemy_platform = pygame.image.load('scenes/Battle_platform.png')
        self.EPX = Screen_W+600
        self.EPY = 525

        
        self.PP_rect = self.player_platform.get_rect(center = (self.PPX,self.PPY))
        self.player_platform.set_colorkey('White')

        self.EP_rect = self.enemy_platform.get_rect(center = (self.EPX,self.EPY))
        self.enemy_platform = pygame.transform.scale(self.enemy_platform, (500,500))
        self.enemy_platform.set_colorkey('White')

        #ava sprite

        self.ava_idle_right = pygame.image.load('Ava/Ava_idle_right.png')

        self.avaX, self.avaY = 250,400

        self.ava_combat_rect = self.ava_idle_right.get_rect(center = (self.avaX,self.avaY))
        self.ava_idle_right = pygame.transform.scale(self.ava_idle_right, (200,250))
        self.ava_idle_right.set_colorkey('White')

        #mouse and buttons

        self.cursor = pygame.image.load('GUI/cursor.png')
        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_rect = pygame.Rect(0, 0, 25, 25)
        self.cursor = pygame.transform.scale(self.cursor, (50,75))

        #Healthbars

        self.player_ratio = (575/100)*((self.current_HP/self.HP)*100)
        self.enemy_ratio = (575/100)*((self.current_eHP/self.enemy_HP)*100)

        self.player_red_rect = pygame.Rect(25, Screen_H-75, 575, 50)
        self.player_green_rect = pygame.Rect(25, Screen_H-75, self.player_ratio, 50)

        self.enemy_red_rect = pygame.Rect(Screen_W-600, 25, 575, 50)
        self.enemy_green_rect = pygame.Rect(Screen_W-600, 25, self.enemy_ratio, 50)
#------------------------------------------------------------------------------------
        #menu buttons
        self.x1, self.y1 = 1300, 425
        self.endx1, self.endy1 = 800, 425
        self.col1 = ('Green')
        self.button1_rect = pygame.Rect(self.x1, self.y1, 400, 75)

        self.x2, self.y2 = 1300, 525
        self.endx2, self.endy2 = 800, 525
        self.col2 = ('Green')
        self.button2_rect = pygame.Rect(self.x2, self.y2, 400, 75)

        self.x3, self.y3 = 1300, 625
        self.endx3, self.endy3 = 800, 625
        self.col3 = ('Green')
        self.button3_rect = pygame.Rect(self.x3, self.y3, 400, 75)

        #fight buttons

        self.x4, self.y4 = 800, 450
        self.endx4, self.endy4 = 800,450
        self.col4 = ('Green')
        self.button4_rect = pygame.Rect(self.x4, self.y4, 100, 125)

        self.x5, self.y5 = 950, 450
        self.endx5, self.endy5 = 950, 450
        self.col5 = ('Green')
        self.button5_rect = pygame.Rect(self.x5, self.y5, 100, 125)

        self.x6, self.y6 = 1100, 450
        self.endx6, self.endy6 = 1100, 450
        self.col6 = ('Green')
        self.button6_rect = pygame.Rect(self.x6, self.y6, 100, 125)

        self.x7, self.y7 = 800, 600
        self.endx7, self.endy7 = 800, 600
        self.col7 = ('Green')
        self.button7_rect = pygame.Rect(self.x7, self.y7, 400, 65)
        
        #ava attacks

        self.x8, self.y8 = 825, 500
        self.endx8, self.endy8 = 800, 500
        self.col8 = ('Green')
        self.button8_rect = pygame.Rect(self.x8, self.y8, 100, 65)

        self.x9, self.y9 = 950, 450
        self.endx9, self.endy9 = 925, 450
        self.col9 = ('Green')
        self.button9_rect = pygame.Rect(self.x9, self.y9, 100, 65)

        self.x10, self.y10 = 1075, 500
        self.endx10, self.endy10 = 1000, 500
        self.col10 = ('Green')
        self.button10_rect = pygame.Rect(self.x10, self.y10, 100, 65)

        self.x11, self.y11 = 825, 600
        self.endx11, self.endy11 = 800, 600
        self.col11 = ('Green')
        self.button11_rect = pygame.Rect(self.x11, self.y11, 350, 65)








        #items buttons


        #misc

        pygame.mouse.set_visible(False)
        self.buttons = 'menu'
        self.count = False
        self.counter = 0

        
    def platform_blit(self):
        global inpos
        print(self.EPX, self.EPY)
        screen.blit(self.BG,(0,0))
        self.slide = 20
        self.slide2 = 20
        
        if self.PP_rect.x >= -70:
            inpos = True
            pass
        else:
            self.PP_rect.x += self.slide
            self.slide/4
            inpos = False

        if self.EP_rect.x <= Screen_W-500:
            inpos2 = True
            pass
        else:
            self.EP_rect.x -= self.slide2
            self.slide2/4
            inpos2 = False
        
        screen.blit(self.player_platform, self.PP_rect)
        screen.blit(self.enemy_platform, self.EP_rect)
        if inpos:
            self.avaX, self.avaY = self.PP_rect.x, self.PP_rect.y

    def enter_combat(self):
        screen.blit(self.BG,(0,0))
        screen.blit(self.player_platform, self.PP_rect)
        screen.blit(self.enemy_platform, self.EP_rect)

        screen.blit(self.ava_idle_right,(self.ava_combat_rect))
        
        #buttons
        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_rect.center = self.mouse_pos

        if event.type == pygame.MOUSEBUTTONUP:
                self.click += 1
                print(self.click)

        self.player_ratio = (575/100)*((self.current_HP/self.HP)*100)
        self.enemy_ratio = (575/100)*((self.current_eHP/self.enemy_HP)*100)

        self.player_red_rect = pygame.Rect(25, Screen_H-75, 575, 50)
        self.player_green_rect = pygame.Rect(25, Screen_H-75, self.player_ratio, 50)

        self.enemy_red_rect = pygame.Rect(Screen_W-600, 25, 575, 50)
        self.enemy_green_rect = pygame.Rect(Screen_W-600, 25, self.enemy_ratio, 50)

        pygame.draw.rect(screen, ('Red'), self.player_red_rect)
        pygame.draw.rect(screen, ('Green'), self.player_green_rect)
        pygame.draw.rect(screen, ('Red'), self.enemy_red_rect)
        pygame.draw.rect(screen, ('Green'), self.enemy_green_rect)

        if self.count:
            self.counter -=1
            if self.counter == 0:
                self.count = False
        
        if self.current_HP > self.HP:
            self.current_HP = self.HP

        if self.current_eHP > self.enemy_HP:
            self.current_eHP = self.enemy_HP
                

#-----------------------------------------------------------------------------
                #Action Select
        if self.buttons == 'menu':
            pygame.draw.rect(screen, self.col1, self.button1_rect)
            pygame.draw.rect(screen, self.col2, self.button2_rect)
            pygame.draw.rect(screen, self.col3, self.button3_rect)
            if self.x1 != self.endx1:
                self.x1 -=25
                self.x2 -=25
                self.x3 -=25
            self.button1_rect = pygame.Rect(self.x1, self.y1, 400, 75)
            self.button2_rect = pygame.Rect(self.x2, self.y2, 400, 75)
            self.button3_rect = pygame.Rect(self.x3, self.y3, 400, 75)


                                                                    #FIGHT BUTTON
            if self.mouse_rect.colliderect(self.button1_rect):
                self.col1 = ('Yellow')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.col1 = ('Red')
                    self.click = -1
                elif self.click == 1:
                    self.click += 1
                    self.buttons = 'fight'
            else: 
                self.col1 = ('Green')
                                                                    #ITEMS BUTTON
            if self.mouse_rect.colliderect(self.button2_rect):
                self.col2 = ('Yellow')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.col2 = ('Red')
                    self.click = 0
                elif self.click == 1:
                    pass#######################
            else: 
                self.col2 = ('Green')
                                                                    #ESCAPE BUTTON
            if self.mouse_rect.colliderect(self.button3_rect):
                self.col3 = ('Yellow')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.col3 = ('Red')
                    self.click = 0
                elif self.click == 1:
                    pass#######################
            else: 
                self.col3 = ('Green')
                
#----------------------------------------------------------------------------
                #Character Select
        if self.buttons == 'fight':
            
            pygame.draw.rect(screen, self.col4, self.button4_rect)
            pygame.draw.rect(screen, self.col5, self.button5_rect)
            pygame.draw.rect(screen, self.col6, self.button6_rect)
            pygame.draw.rect(screen, self.col7, self.button7_rect)
            if self.mouse_rect.colliderect(self.button4_rect):
                self.col4 = ('Yellow')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.col4 = ('Red')
                    self.click = 0
                elif self.click == 1:
                    self.click += 1
                    self.buttons = 'ava'           #Ava Select
            else: 
                self.col4 = ('Green')

            if self.mouse_rect.colliderect(self.button5_rect):
                self.col5 = ('Yellow')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.col5 = ('Red')
                    self.click = 0
                elif self.click == 1:
                    self.click += 1
                                                    #Edward Select
            else: 
                self.col5 = ('Green')

            if self.mouse_rect.colliderect(self.button6_rect):
                self.col6 = ('Yellow')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.col6 = ('Red')
                    self.click = 0
                elif self.click == 1:
                    self.click += 1
                                                    #Robot Select
            else: 
                self.col6 = ('Green')

            if self.mouse_rect.colliderect(self.button7_rect):
                self.col7 = ('Yellow')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.col7 = ('Red')
                    self.click = 0
                elif self.click == 1:
                    self.buttons = 'menu'
                                                    #Back Button
            else: 
                self.col7 = ('Green')
#-------------------------------------------------------------------------
                #AVA'S MOVES
        if self.buttons == 'ava':
            
            pygame.draw.rect(screen, self.col8, self.button8_rect)
            pygame.draw.rect(screen, self.col9, self.button9_rect)
            pygame.draw.rect(screen, self.col10, self.button10_rect)
            pygame.draw.rect(screen, self.col11, self.button11_rect)

            #Attack 1
            if self.mouse_rect.colliderect(self.button8_rect):
                self.col8 = ('Yellow')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.col8 = ('Red')
                    self.click = 0
                elif self.click == 1:
                    self.click += 1
                    self.current_HP += 100
                    self.damage = 3*self.clvl
                    print(self.current_eHP)
                    #
                    #
                    #
                    #
                    #
                    self.buttons = 'enemyturn' #THIS SECTION HERE WILL ATTACK THE ENEMY
            else:
                self.col8 = ('Green')

            #Attack 2
            if self.mouse_rect.colliderect(self.button9_rect):
                self.col9 = ('Yellow')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.col9 = ('Red')
                    self.click = 0
                elif self.click == 1:
                    self.click += 1
                    self.damage = 5*self.clvl # Damage
                    print(self.current_eHP)
                    #
                    #
                    #
                    #
                    #
                    self.buttons = 'enemyturn' #THIS SECTION HERE WILL ATTACK THE ENEMY
            else:
                self.col9 = ('Green')

            #Attack 3
            if self.mouse_rect.colliderect(self.button10_rect):
                self.col10 = ('Yellow')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.col10 = ('Red')
                    self.click = 0
                elif self.click == 1:
                    self.click += 1
                    print(self.current_eHP)
                    #
                    #
                    #
                    #
                    #
                    self.buttons = 'enemyturn' #THIS SECTION HERE WILL ATTACK THE ENEMY
            else:
                self.col10 = ('Green')

            #Back Button
            if self.mouse_rect.colliderect(self.button11_rect):
                self.col11 = ('Yellow')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.col11 = ('Red')
                    self.click = 0
                elif self.click == 1:
                    self.click += 1
                    print(self.current_eHP)
                    self.buttons = 'fight'
            else:
                self.col11 = ('Green')

        if self.buttons == 'enemyturn':
            # player attack animation here
            self.current_eHP -= self.damage
            # enemy choose attack here
            # enemy attack animation here
            self.current_HP -= 10 # enemy damage
            #lose check
            #win check
            self.buttons = 'menu'
#----------------------------------------------------------------------------------------------------------------
        screen.blit(self.cursor, self.mouse_rect)

p1 = Combater('hound', 10, 10, 'scenes/battle_background.jpg')
p1.rect_init()

    
#pygame.display.toggle_fullscreen()

ava = last_idle
ava_start_list = ["400,600","750,630","800,600","800,600","800,600","500,600","500,600","500,600","540,590","880,300","545,600","545,600","545,600","545,600","1100,600","700,600","600,600"]
text_timer = 0
map_list = ["maps/map.txt", "maps/map1.5.txt" , "maps/map3.txt", "maps/map3.5.txt", "maps/map3.6.txt"  , "maps/map4.txt",  "maps/4.5.txt","maps/map5.txt", "maps/map5.1.txt","maps/map5.2.txt", "maps/map5.3.txt", "maps/map5.4.txt", "maps/map5.5.txt", "maps/map6.txt","maps/map6.1.txt","maps/map6.2.txt","maps/map6.3.txt"]
map_index = 8
tile_lister = ["1","1","1","1","1","1","1","2" ,"2" ,"2" ,"2"   ,"2","2","3","3","3","3"]
x,y = ava_start_list[map_index].split(",")
x,y = int(x),int(y)
avaX,avaY = x,y
ava_rect = ava.get_rect(center = (avaX,avaY))
ava_rect = ava.get_rect(center = (avaX,avaY))
ava.set_colorkey('White') 
opening = pygame.image.load("scenes/sky.png")

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
    intro = pygame.mixer.Sound("music/intro.mp3")
    chill = pygame.mixer.Sound("music/chill.mp3")
    scary = pygame.mixer.Sound("music/scary.mp3")
    write = pygame.mixer.Sound("music/write.mp3")
    suprise = pygame.mixer.Sound("music/suprise.mp3")
    suprise.set_volume(4)
    playlist = [chill,chill,chill,chill,chill,chill,chill     ,scary,scary,scary,scary,scary,scary,scary,scary,scary,scary]
    
class special_sprite_set:
    # map 1 assets
    tree = pygame.image.load("special_sprite/Tree.png")
    tree = pygame.transform.rotozoom(tree,0,2)
    tree_rect = tree.get_rect(center = (700,500))
    cabin = pygame.image.load("special_sprite/Cabin.png")
    cabin = pygame.transform.rotozoom(cabin,0,2)
    cabin_rect = cabin.get_rect( center =  (1000,300))   
    talk = pygame.image.load("special_sprite/talk.png")
    talk = pygame.transform.rotozoom(talk,0,2)
    talk_rect = talk.get_rect(center = (300,300))
    image_list_1 = [tree,cabin,talk]
    rect_list_1 = [tree_rect,cabin_rect,talk_rect]
    #------------------------------------------------------------------------------------------------------------
    talk_0 = talk.get_rect(center = (600,400))
    #-----------------



    ship = pygame.image.load("special_sprite/Ship_full.png")
    ship = pygame.transform.rotozoom(ship,0,2)
    ship_rect = ship.get_rect(center = (360,600))
    talk2 = talk.get_rect(center = (300,300))
    #--------
    talk3 = talk.get_rect(center= (750,400))
    #----------
    talk4 = talk.get_rect(  center = (700,200))
    #--------
    talk5 = talk.get_rect(center = (500,400))
    #---------
    talk6 = talk.get_rect(center = (300,300))
    #---------
    talk7 = talk.get_rect(center = (300,300))
    #---------
    talk8 = talk.get_rect(center = (300,300))
    #---------
    talk9 = talk.get_rect(center = (300,300))
    #---------
    talk10 = talk.get_rect(center = (470,300))
    #---------
    talk11 = talk.get_rect(center = (470,300))
    #---------
    talk12 = talk.get_rect(center = (280,300))
    #---------
    talk13 = talk.get_rect(center = (280,300))
    #---------
    talk14 = talk.get_rect(center = (280,170))
    #---------
    talk15 = talk.get_rect(center = (640,300))

    final_image_list = [ image_list_1, [talk],[ship,talk], [talk],         [talk], [talk], [talk],[talk],[talk],[talk],[talk],[talk],[talk],[talk],[talk],[talk],[talk],[talk] ]
    final_rect_list = [  rect_list_1, [talk_0],[ship_rect,talk2], [talk3], [talk4], [talk5], [talk6] ,[talk7],[talk8] ,[talk9],[talk10],[talk11],[talk12],[talk13],[talk14],[talk15],[] ]
    #--------------------------------------------------------------------------------------------------


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
                
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    scroll = pygame.mixer.Sound('music/move.mp3')
                    scroll.play(0)  
                if event.key == pygame.K_w:
                    if end_state == 1:
                        end_state =0
                        start_state = 1
                    else:
                        pass
                if event.key == pygame.K_s:
                    if start_state == 1:
                        start_state = 0
                        end_state = 1
                    else:
                        pass
                
                if event.key == pygame.K_SPACE:
                    select = pygame.mixer.Sound('music/select.mp3')
                    select.play(0)
                    if start_state == 1:
                        screen.blit(opening,(0,0))
                        Music_list.write.play(-1)
                        home_state = "dialogue"
                        dialogue_timer = 0
                        dialogue_str = " In a distant universe, where peace has long been forgetton, and humankind are haunted by the disturbing creations of their ancestors, living lives of fear and paranoia, an unlikely meeting between two individuals would give it renewed hope and set the trajectory for its future..............................."
                        dialogue_list  = str_split(dialogue_str,180) 
                        Music_list.title.stop()
                        Music_list.intro.play(-1)
                        intro  = 1
                        #Music_list.playlist[map_index].play(-1)
                    
                        
                    else:
                        pygame.quit()

    if home_state == 0: # overwold state, map exploration  here 0.01 8
        #battle_opt +=0.02
        if map_index == 8:
            suprise_counter +=0.02
        if int(suprise_counter) >=6 and suprise_opt == True:
            suprise_opt = False
            Music_list.suprise.play(0)
            suprise_counter = 0
        if int(battle_opt) >= 4:
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
                avaX -=1
            
            key = True 
            direction = 'left'
        elif keys[pygame.K_d]:
           
            if collide_check(ava_rect,wall_rect_list=wall_list,directions="right"):
                pass
            else:
                avaX +=1
            key = True
            direction = 'right'
        elif keys[pygame.K_w]:

            if collide_check(ava_rect,wall_rect_list=wall_list,directions="up"):
                pass
            else:
                avaY -=1
            if collide_check(ava_rect,wall_rect_list=wall_list,directions="up") in special_lists and keys[pygame.K_SPACE]:
                home_state = "dialogue"
                dialogue_timer = 0
                dialogue_option = special_lists.index(collide_check(ava_rect,wall_rect_list=wall_list,directions="up"))
                dialogue_str = dialogue.final_list[map_index][dialogue_option]
                dialogue_list  = str_split(dialogue_str,180)
                Music_list.write.play(-1)
                
        
            key = True
            direction = 'up'
        elif keys[pygame.K_s]:
          
            if collide_check(ava_rect,wall_rect_list=wall_list,directions="down"):
                pass
            else:
                avaY +=1
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
                    if intro == 1:
                        Music_list.intro.stop()
                        Music_list.playlist[map_index].play(-1)
                        intro = 0
                    pygame.time.wait(30)
                    Music_list.write.stop()
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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        try:
            if inpos == False:
                p1.platform_blit()
            else:
                p1.enter_combat()
        except:
            pass
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()



#NOTES
# AVAS TOP TRIANGLE IS TOO HIGH
# HER LEFT AND RIGHT WORK FINE
# BOTTOM IS TWEAKING

