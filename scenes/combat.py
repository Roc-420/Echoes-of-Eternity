import pygame
clock = pygame.time.Clock()

                        #THINGS TO STILL DO
#Onscreen text
#Display Health remaining as an int
#Display Level and Enemy Name

#HP and Damage Scaling


#Enemy AI and Bias for moves

#Mana System

#Attack Animation for Enemy and Slash Animation

#Attacking (Ava)
    #Defend a little bit and Attack
    #Ultimate
    #Mediocre Attack

#Buffing and Healing System system (Edward)
    #Multiplier for damage
    #Heal Ava

#Enemy Debuff System (Robot)
    #Give one Charge of Ult
    #Debuff Enemy


Screen_W, Screen_H = 1280, 720
screen = pygame.display.set_mode((Screen_W, Screen_H))

class Combat():
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










#enemy name (enemies to fight are listed above in the class), enemyLVL, playerLVL, BG file
p1 = Combat('hound', 10, 10, 'scenes/battle_background.jpg')
p1.rect_init()

inpos = False
running = True
while running:
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


    clock.tick(60)
    pygame.display.update()
pygame.quit()