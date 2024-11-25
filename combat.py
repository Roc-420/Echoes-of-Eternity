import pygame
import random
clock = pygame.time.Clock()

                        #THINGS TO STILL DO
#Onscreen text
#Display Health remaining as an int
#Display Level and Enemy Name

#Mana System

#Attack Animation for Enemy and Slash Animation

#Attacking (Ava)
    #Defend a little bit and Attack
    #Ultimate        - Work on this
    #Mediocre Attack - Code this

#Buffing and Healing System system (Edward)
    #Multiplier for damage
    #Heal Ava

#Enemy Debuff System (Robot)
    #Give one Charge of Ult     - Code this
    #Debuff Enemy



pygame.init()
Screen_W, Screen_H = 1280, 720


pygame.display.toggle_fullscreen()
screen = pygame.display.set_mode((Screen_W, Screen_H))

other_text_font = pygame.font.Font('font/Pixeltype.ttf',34)
Battle_text = pygame.font.Font('font/Pixeltype.ttf',50)

class Combat():
    def __init__(self, enemy, enemylvl, clvl, BGLOAD): #enemy being fought, Clvl - current level,x
        self.BGLOAD = BGLOAD

        self.enemylvl = enemylvl
        self.clvl = clvl

        self.enemy_multiplier = 1
        self.multiplier = 1

        #Name, HP (to be multiplied by level), moves
        
        self.hound_moves = {'Tackle':2, 'Bite':5}
        self.hound = ['Hound', 20, self.hound_moves, 'enemy/Hound.png', (925, 285), (250,125)]

        self.acalica_moves = {'Beam':11, 'Aura':20, 'Charge':2}
        self.acalica = ['Acalica', 35, self.acalica_moves, 'enemy/Acalica.png', (975, 175), (300,275)]

        self.bitumen_moves = {'Sludge':2, 'Charge':0}
        self.bitumen = ['Bitumen', 5, self.bitumen_moves, 'enemy/Bitumen.png', (975, 300), (125,100)]

        self.ignissus_moves = {'Penetrate':2, 'Slashy':4}
        self.ignissus = ['Ignissus', 8, self.ignissus_moves, 'enemy/Ignissus.png', (950, 225), (125,190)]


        self.Eattack = 0

        self.enemies = [self.hound, self.acalica, self.bitumen, self.ignissus]
        
        for i in range(len(self.enemies)):
            if enemy == self.enemies[i-1][0]:
                self.enemy = self.enemies[i-1]
                print(self.enemy)

        self.HP = 25*int(self.clvl)
        self.current_HP = self.HP

        self.enemy_HP = int(self.enemy[1])*self.enemylvl
        self.current_eHP = self.enemy_HP

        self.enemy_sprite = pygame.image.load(self.enemy[3])

        self.enemy_rect = self.enemy_sprite.get_rect(center = self.enemy[4])
        self.enemy_sprite = pygame.transform.scale(self.enemy_sprite, self.enemy[5])
        self.enemy_sprite.set_colorkey('White')
        
        self.Emoves = self.enemy[2]
        print(self.Emoves)
        self.eTURN = False
        self.finish = False
        self.ult_check = 0


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

        self.text = ''
#------------------------------------------------------------------------------------
        #menu buttons
        self.x1, self.y1 = 1300, 525 #425
        self.endx1, self.endy1 = 800, 425
        self.col1 = ('Green')
        self.fight_surf = pygame.image.load('GUI/Fight.png')
        self.fight_surf = pygame.transform.scale(self.fight_surf, (350,65))
        self.button1_rect = pygame.Rect(self.x1, self.y1, 350, 75)

        self.x2, self.y2 = 1300, 525
        self.endx2, self.endy2 = 800, 525
        self.col2 = ('Green')
        self.item_surf = pygame.image.load('GUI/Item.png')
        self.item_surf = pygame.transform.scale(self.item_surf, (350,65))
        self.button2_rect = pygame.Rect(self.x2, self.y2, 350, 75)

        self.x3, self.y3 = 1300, 625
        self.endx3, self.endy3 = 800, 625
        self.col3 = ('Green')
        self.escape_surf = pygame.image.load('GUI/Escape.png')
        self.escape_surf = pygame.transform.scale(self.escape_surf, (350,65))
        self.button3_rect = pygame.Rect(self.x3, self.y3, 350, 75)

        #fight buttons

        self.x4, self.y4 = 800, 450
        self.endx4, self.endy4 = 800,450
        self.col4 = ('Green')
        self.ava_surf = pygame.image.load('GUI/Avaicon.png')
        self.ava_surf = pygame.transform.scale(self.ava_surf, (100,100))
        self.button4_rect = pygame.Rect(self.x4, self.y4, 100, 100)

        self.x5, self.y5 = 925, 450
        self.endx5, self.endy5 = 950, 450
        self.col5 = ('Green')
        self.edward_surf = pygame.image.load('GUI/Edwardicon.png')
        self.edward_surf = pygame.transform.scale(self.edward_surf, (100,100))
        self.button5_rect = pygame.Rect(self.x5, self.y5, 100, 100)

        self.x6, self.y6 = 1050, 450
        self.endx6, self.endy6 = 1100, 450
        self.col6 = ('Green')
        self.robot_surf = pygame.image.load('GUI/Roboticon.png')
        self.robot_surf = pygame.transform.scale(self.robot_surf, (100,100))
        self.button6_rect = pygame.Rect(self.x6, self.y6, 100, 100)

        self.x7, self.y7 = 800, 600
        self.endx7, self.endy7 = 800, 600
        self.col7 = ('Green')
        self.back_surf = pygame.image.load('GUI/Back.png')
        self.back_surf = pygame.transform.scale(self.back_surf, (350,65))
        self.button7_rect = pygame.Rect(self.x7, self.y7, 350, 65)
        
        
        #ava attacks

        #Block
        self.x8, self.y8 = 800, 500
        self.endx8, self.endy8 = 800, 500
        self.col8 = ('Green')
        self.defend_surf = pygame.image.load('GUI/Defend.png')
        self.defend_surf = pygame.transform.scale(self.defend_surf, (100,65))
        self.button8_rect = pygame.Rect(self.x8, self.y8, 100, 65)

        #Ultimate
        self.x9, self.y9 = 925, 450
        self.endx9, self.endy9 = 925, 450
        self.col9 = ('Green')
        self.ultimate_surf = pygame.image.load('GUI/Ultimate.png')
        self.ultimate_surf = pygame.transform.scale(self.ultimate_surf, (100,65))
        self.button9_rect = pygame.Rect(self.x9, self.y9, 100, 65)

        #Slash
        self.x10, self.y10 = 1050, 500
        self.endx10, self.endy10 = 1000, 500
        self.col10 = ('Green')
        self.slash_surf = pygame.image.load('GUI/Slash.png')
        self.slash_surf = pygame.transform.scale(self.slash_surf, (100,65))
        self.button10_rect = pygame.Rect(self.x10, self.y10, 100, 65)

        #Back
        self.x11, self.y11 = 800, 600
        self.endx11, self.endy11 = 800, 600
        self.col11 = ('Green')
        self.back_surf = pygame.image.load('GUI/Back.png')
        self.back_surf = pygame.transform.scale(self.back_surf, (350,65))
        self.button11_rect = pygame.Rect(self.x11, self.y11, 350, 65)

        #Edward Attacks

        #Heal
        self.x12, self.y12 = 850, 475
        self.endx12, self.endy12 = 800, 500
        self.col12 = ('Green')
        self.heal_surf = pygame.image.load('GUI/Heal.png')
        self.heal_surf = pygame.transform.scale(self.heal_surf, (100,65))
        self.button12_rect = pygame.Rect(self.x12, self.y12, 100, 65)

        #Buff
        self.x13, self.y13 = 1000, 475
        self.endx13, self.endy13 = 925, 450
        self.col13 = ('Green')
        self.buff_surf = pygame.image.load('GUI/Buff.png')
        self.buff_surf = pygame.transform.scale(self.buff_surf, (100,65))
        self.button13_rect = pygame.Rect(self.x13, self.y13, 100, 65)

        #Back
        self.x14, self.y14 = 800, 600
        self.endx14, self.endy14 = 800, 600
        self.col14 = ('Green')
        self.back_surf = pygame.image.load('GUI/Back.png')
        self.back_surf = pygame.transform.scale(self.back_surf, (350,65))
        self.button14_rect = pygame.Rect(self.x14, self.y14, 350, 65)

        #Robot Attacks

        #Debuff
        self.x15, self.y15 = 850, 475
        self.endx15, self.endy15 = 800, 500
        self.col15 = ('Green')
        self.debuff_surf = pygame.image.load('GUI/Debuff.png')
        self.debuff_surf = pygame.transform.scale(self.debuff_surf, (100,65))
        self.button15_rect = pygame.Rect(self.x15, self.y15, 100, 65)

        #Charge Ult
        self.x16, self.y16 = 1000, 475
        self.endx16, self.endy16 = 925, 450
        self.col16 = ('Green')
        self.ultcharge_surf = pygame.image.load('GUI/Ultcharge.png')
        self.ultcharge_surf = pygame.transform.scale(self.ultcharge_surf, (100,65))
        self.button16_rect = pygame.Rect(self.x16, self.y16, 100, 65)

        #Back
        self.x17, self.y17 = 800, 600
        self.endx17, self.endy17 = 800, 600
        self.col17 = ('Green')
        self.back_surf = pygame.image.load('GUI/Back.png')
        self.back_surf = pygame.transform.scale(self.back_surf, (350,65))
        self.button17_rect = pygame.Rect(self.x17, self.y17, 350, 65)



        #items buttons


        #misc

        
        self.buttons = 'menu'
        self.count = False
        self.counter = 0
        self.click = 0
        self.buttons = 'menu'
        self.win_check = False
        self.Ultimate = False
        self.charge = 0
        self.stun = 0

        self.end = False
        self.match = False

        
    def platform_blit(self):
        global inpos
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
        global home_state, win, loss #????????????????????????????
        screen.blit(self.BG,(0,0))
        screen.blit(self.player_platform, self.PP_rect)
        screen.blit(self.enemy_platform, self.EP_rect)

        screen.blit(self.ava_idle_right,(self.ava_combat_rect))
        screen.blit(self.enemy_sprite,(self.enemy_rect))
        #buttons
        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_rect.center = self.mouse_pos

        if event.type == pygame.MOUSEBUTTONUP:
            self.click += 1

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
            print(self.counter)
            if self.counter == 0:
                self.count = False

        if self.current_eHP <= 0:
            self.text = 'You won!'
            win = True
            self.match = True
            self.current_eHP += 1
            self.buttons = ''
            
        if self.current_HP <= 0:
            self.text = 'You lost..'
            loss = True
            self.match = True
            self.current_HP += 1
            self.buttons = ''

        if self.match:
            self.count = True
            self.counter = 200
            self.match = False
            self.end = True

        if self.end and self.count == False:
            home_state = 0
            self.end = False
        elif self.end and self.count:
            self.battle = Battle_text.render(self.text, False, (255,255,255))
            screen.blit(self.battle, (775,Screen_H-200))

        

        self.pLVL_HP = other_text_font.render(f'lvl {self.clvl} - {self.current_HP}/{self.HP}', False, (255,255,255))
        screen.blit(self.pLVL_HP, (620,Screen_H-60))###################### text box ######################################################################################
        
        self.eLVL_HP = other_text_font.render(f'lvl {self.enemylvl} {self.enemy[0]} - {self.current_eHP}/{self.enemy_HP}', False, (255,255,255))
        screen.blit(self.eLVL_HP, (450,45))######################################################################################################################

        
        
        if self.current_HP > self.HP: # stops overhealing
            self.current_HP = self.HP

        if self.current_eHP > self.enemy_HP:
            self.current_eHP = self.enemy_HP
                

#-----------------------------------------------------------------------------
                #Action Select
        if self.buttons == 'menu':
            #pygame.draw.rect(screen, self.col1, self.button1_rect)
            screen.blit(self.fight_surf, self.button1_rect)
            #pygame.draw.rect(screen, self.col2, self.button2_rect)
            #screen.blit(self.item_surf, self.button2_rect)
            #pygame.draw.rect(screen, self.col3, self.button3_rect)
            #screen.blit(self.escape_surf, self.button3_rect)
            if self.x1 != self.endx1:
                self.x1 -=25
            #    self.x2 -=25
            #    self.x3 -=25
            self.button1_rect = pygame.Rect(self.x1, self.y1, 350, 75)
            #self.button2_rect = pygame.Rect(self.x2, self.y2, 350, 75)
            #self.button3_rect = pygame.Rect(self.x3, self.y3, 350, 75)


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
            #if self.mouse_rect.colliderect(self.button2_rect):
            #    self.col2 = ('Yellow')
            #    if event.type == pygame.MOUSEBUTTONDOWN:
            #        self.col2 = ('Red')
            #        self.click = 0
            #    elif self.click == 1:
            #        pass
            #else: 
            #    self.col2 = ('Green')
            #                                                        #ESCAPE BUTTON
            #if self.mouse_rect.colliderect(self.button3_rect):
            #    self.col3 = ('Yellow')
            #    if event.type == pygame.MOUSEBUTTONDOWN:
            #        self.col3 = ('Red')
            #        self.click = 0
            #    elif self.click == 1:
            #        pass#######################
            #else: 
            #    self.col3 = ('Green')
                
#----------------------------------------------------------------------------
                #Character Select
        if self.buttons == 'fight':
            
            #pygame.draw.rect(screen, self.col4, self.button4_rect)
            screen.blit(self.ava_surf, self.button4_rect)
            #pygame.draw.rect(screen, self.col5, self.button5_rect)
            screen.blit(self.edward_surf, self.button5_rect)
            #pygame.draw.rect(screen, self.col6, self.button6_rect)
            screen.blit(self.robot_surf, self.button6_rect)
            #pygame.draw.rect(screen, self.col7, self.button7_rect)
            screen.blit(self.back_surf, self.button7_rect)
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
                    self.buttons = 'edward'         #Edward Select
            else: 
                self.col5 = ('Green')

            if self.mouse_rect.colliderect(self.button6_rect):
                self.col6 = ('Yellow')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.col6 = ('Red')
                    self.click = 0
                elif self.click == 1:
                    self.click += 1
                    self.buttons = 'robot'          #Robot Select
            else: 
                self.col6 = ('Green')

            if self.mouse_rect.colliderect(self.button7_rect):
                self.col7 = ('Yellow')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.col7 = ('Red')
                    self.click = 0
                elif self.click == 1:
                    self.buttons = 'menu'           #Back Button
            else: 
                self.col7 = ('Green')
#-------------------------------------------------------------------------
                #AVA'S MOVES
        if self.buttons == 'ava':
            
            #pygame.draw.rect(screen, self.col8, self.button8_rect)
            screen.blit(self.defend_surf, self.button8_rect)
            
            if self.ult_check >= 5:
                screen.blit(self.ultimate_surf, self.button9_rect)
            else:
                pygame.draw.rect(screen, self.col9, self.button9_rect)
            #pygame.draw.rect(screen, self.col10, self.button10_rect)
            screen.blit(self.slash_surf, self.button10_rect)
            #pygame.draw.rect(screen, self.col11, self.button11_rect)
            screen.blit(self.back_surf, self.button11_rect)


            self.ult_count = other_text_font.render(f'ULT {self.ult_check}/5', False, (255,255,255))
            screen.blit(self.ult_count, (935,Screen_H-200))

            self.Stun = other_text_font.render('Stun', False, (255,255,255))
            screen.blit(self.Stun, (830,Screen_H-150))

            self.Slash = other_text_font.render('Slash Attack', False, (255,255,255))
            screen.blit(self.Slash, (1040,Screen_H-150))
          
            #Attack 1
            if self.mouse_rect.colliderect(self.button8_rect):
                self.col8 = ('Yellow')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.col8 = ('Red')
                    self.click = 0
                elif self.click == 1:
                    self.click += 1
                    self.stun = 3
                    self.damage = 0
                    self.text = 'Ava Blocked some damage!'
                    #
                    #
                    #
                    self.eTURN = True
                    self.buttons = 'enemyturn' #THIS SECTION HERE WILL ATTACK THE ENEMY
            else:
                self.col8 = ('Green')

            #Attack 2
            if self.mouse_rect.colliderect(self.button9_rect):
                self.col9 = ('Yellow')
                if self.ult_check >= 5:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.click = 0
                    elif self.click == 1:
                        self.click += 1

                        self.count = True
                        self.counter = 60
                        self.Ultimate = True
                        self.charge = 0
                        #
                        #
                        #
                        self.buttons = 'enemyturn' #THIS SECTION HERE WILL ATTACK THE ENEMY
            else:
                self.col9 = (50,50,50)

            #Attack 3
            if self.mouse_rect.colliderect(self.button10_rect):
                self.col10 = ('Yellow')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.col10 = ('Red')
                    self.click = 0
                elif self.click == 1:
                    self.damage = 3*self.clvl
                    self.click += 1
                    #
                    #
                    #
                    self.text = 'Ava used Slash!'
                    self.eTURN = True
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
                    self.buttons = 'fight'
            else:
                self.col11 = ('Green')

#-------------------------------------------------------------------------
                #EDWARDS'S MOVES
        if self.buttons == 'edward':
            
            #pygame.draw.rect(screen, self.col12, self.button12_rect)
            screen.blit(self.heal_surf, self.button12_rect)
            #pygame.draw.rect(screen, self.col13, self.button13_rect)
            screen.blit(self.buff_surf, self.button13_rect)
            #pygame.draw.rect(screen, self.col14, self.button14_rect)
            screen.blit(self.back_surf, self.button14_rect)

            self.Heal = other_text_font.render('Heal', False, (255,255,255))
            screen.blit(self.Heal, (880,Screen_H-175))

            self.Buff = other_text_font.render('Buff', False, (255,255,255))
            screen.blit(self.Buff, (1030,Screen_H-175))

            #Attack 1
            if self.mouse_rect.colliderect(self.button12_rect):
                self.col12 = ('Yellow')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.col12 = ('Red')
                    self.click = 0
                elif self.click == 1:
                    self.click += 1
                    self.heal = 10*self.clvl
                    self.current_HP += self.heal
                    self.damage = 0
                    #
                    #
                    #
                    self.text = f'Edward healed {self.heal} damage!'
                    self.eTURN = True
                    self.buttons = 'enemyturn' #THIS SECTION HERE WILL ATTACK THE ENEMY
            else:
                self.col12 = ('Green')

            #Attack 2
            if self.mouse_rect.colliderect(self.button13_rect):
                self.col13 = ('Yellow')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.col13 = ('Red')
                    self.click = 0
                elif self.click == 1:
                    self.click += 1
                    self.damage = 0
                    self.multiplier += 0.2
                    #
                    #
                    self.text = f'Edward Buffed the team! {round(self.multiplier*100)}%'
                    self.eTURN = True
                    self.buttons = 'enemyturn' #THIS SECTION HERE WILL ATTACK THE ENEMY
            else:
                self.col13 = ('Green')

            #Back Button
            if self.mouse_rect.colliderect(self.button14_rect):
                self.col14 = ('Yellow')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.col14 = ('Red')
                    self.click = 0
                elif self.click == 1:
                    self.click += 1
                    self.buttons = 'fight'
            else:
                self.col14 = ('Green')

#-------------------------------------------------------------------------
                #ROBOT'S MOVES
        if self.buttons == 'robot':
            
            #pygame.draw.rect(screen, self.col15, self.button15_rect)
            screen.blit(self.debuff_surf, self.button15_rect)
            #pygame.draw.rect(screen, self.col16, self.button16_rect)
            screen.blit(self.ultcharge_surf, self.button16_rect)
            #pygame.draw.rect(screen, self.col17, self.button17_rect)
            screen.blit(self.back_surf, self.button17_rect)

            self.Debuff = other_text_font.render('Debuff', False, (255,255,255))
            screen.blit(self.Debuff, (867,Screen_H-175))

            self.Charge_Ult = other_text_font.render('Ult Charge', False, (255,255,255))
            screen.blit(self.Charge_Ult, (997,Screen_H-175))
          
            #Debuff
            if self.mouse_rect.colliderect(self.button15_rect):
                self.col15 = ('Yellow')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.col15 = ('Red')
                    self.click = 0
                elif self.click == 1:
                    self.click += 1
                    self.enemy_multiplier = (self.enemy_multiplier/4)*3
                    self.damage = 0
                    #
                    #
                    #
                    self.text = 'Robot Debuffed the Enemy!'
                    self.eTURN = True
                    self.buttons = 'enemyturn' #THIS SECTION HERE WILL ATTACK THE ENEMY
            else:
                self.col15 = ('Green')

            #Charge Ult
            if self.mouse_rect.colliderect(self.button16_rect):
                self.col16 = ('Yellow')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.col16 = ('Red')
                    self.click = 0
                elif self.click == 1:
                    self.click += 1
                    self.damage = 0
                    self.ult_check += 1
                    #
                    self.text = 'Robot charged Ultimate by 1!'
                    self.eTURN = True
                    self.buttons = 'enemyturn' #THIS SECTION HERE WILL ATTACK THE ENEMY
            else:
                self.col16 = ('Green')

            #Back Button
            if self.mouse_rect.colliderect(self.button17_rect):
                self.col17 = ('Yellow')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.col17 = ('Red')
                    self.click = 0
                elif self.click == 1:
                    self.click += 1
                    self.buttons = 'fight'
            else:
                self.col17 = ('Green')

#--------------------------------------------------------------------------------------------------------

        if self.buttons == 'enemyturn':
            
            if self.Ultimate:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.click = 0
                elif self.click == 1:
                    self.click += 1
                    self.charge += 1
                    print('x',self.charge)
                if self.count:
                    self.text = f'Spam click the screen to deal more damage!! X{self.charge}'
                elif self.count == False:
                    self.damage = self.clvl*(self.charge*1.5)
                    self.Ultimate = False
                    self.text = f'The Ultimate did {self.damage} damage with a multiplier of {self.charge}!'
                    self.eTURN = True
                    self.ult_check = 0

            self.battle = Battle_text.render(self.text, False, (255,255,255))
            screen.blit(self.battle, (750,Screen_H-200))

            if self.stun == 3:
                self.battle = Battle_text.render('Will be Stunned next turn', False, (255,255,255))
                screen.blit(self.battle, (750,Screen_H-150))
            elif self.stun == 2:
                self.battle = Battle_text.render('Enemy is Stunned!', False, (255,255,255))
                screen.blit(self.battle, (750,Screen_H-150))
          
            if self.eTURN:
                self.count = True
                self.counter = 150
                self.eTURN = False
                self.semifin = True
            if self.semifin == True and self.count == False:
                self.finish = True
                self.semifin = False
            if self.finish == True:
                # player attack animation here
                self.current_eHP -= round(self.damage*self.multiplier)
                print('multiplier is',self.multiplier*100)
                self.Eattack = random.choice(list(self.Emoves.values()))
                #a = input()
                #enemy attack animation here
                self.stun -= 1
                if self.stun <= 0:
                    self.current_HP -= round(self.Eattack*self.enemy_multiplier*self.enemylvl)
                elif self.stun == 1:
                    pass
                elif self.stun == 2:
                    self.current_HP -= round((self.Eattack*self.enemy_multiplier*self.enemylvl)/3) # enemy damage
                print(self.enemy_multiplier)
                self.charge = 0
                
                self.buttons = 'menu'
                self.semifin = False
                self.finish = False
                
#----------------------------------------------------------------------------------------------------------------
        pygame.mouse.set_visible(False)
        screen.blit(self.cursor, self.mouse_rect)
        










#enemy name (enemies to fight are listed above in the class), enemyLVL, playerLVL, BG file
p1 = Combat('Acalica',10,10,"scenes/battle_background.jpg")
p1.rect_init()

inpos = False
running = True
home_state = "combat"
win = False
loss = False


pygame.display.toggle_fullscreen()

while running:
    if home_state== 0:
        pygame.quit()
    if home_state == "combat":
            # PUT COMBAT LOGIC HERE: YOU CAN REPLACE THE STUFF HERE
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        try:
            if inpos == False:
                p1.platform_blit()

                pygame.mouse.set_visible(True)
            elif home_state == 'combat':
                p1.enter_combat()
                print('blitting')
            if home_state == 0:
                if win:
                    print("win!!!1")
                    outcome = True
                elif loss:
                    print("loss!!!")
                    if map_index >=2:
                        map_index =2
                    else:
                        map_index -=2                    
                    outcome = False
                
                print("end game!!")
                win = False
                loss = False
                inpos = False
            
        except:
            pass


    clock.tick(60)
    pygame.display.update()
pygame.quit()


