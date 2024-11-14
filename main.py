import pygame
from colorama import Fore,Back,Style
# Initialize pygame and create window
pygame.init()
DISPLAY_W, DISPLAY_H = 1700, 1200
canvas = pygame.Surface((DISPLAY_W, DISPLAY_H))
window = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
running = True

#takes images from directory (we need to learn how to use spritesheets instead of this)
def load_ava():
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


#compiles each direction into a list
    ava_right = [ava_right1, ava_right2, ava_right3, ava_right4, ava_right5, ava_right6]
    ava_left = [ava_left1, ava_left2, ava_left3, ava_left4, ava_left5, ava_left6]
    ava_up = [ava_up1, ava_up2, ava_up3, ava_up4, ava_up5, ava_up6]
    ava_down = [ava_down1, ava_down2, ava_down3, ava_down4, ava_down5, ava_down6]

#default idle
    last_idle = ava_down2
    ava = last_idle

    return ava_right, ava_left, ava_up, ava_down, last_idle, ava, ava_idle_left, ava_idle_right

def get_maze(l): # converts maze txt into array
    lister = []
    temp_row=[]
    txt = open(l,'r')
    content = txt.readlines()
    txt.close()
    for row in content:
        for item in row:
            temp_row.append(item)
        temp_row.pop(-1)
        lister.append(temp_row)
        temp_row = []
    
    return lister

def print_maze(maze):
    for row in maze:
        for item in row:
            if item =="#":
                print(Back.BLACK+ " ",end="")
            elif item =="&":
                print(Back.RED + " ",end="")
            elif item == "A":
                print(Back.BLUE + " ",end="")
            else:
                print(Back.WHITE + " ",end="")
                
        print(Style.RESET_ALL)



def map_import(file,width,height):     
    map = get_maze(file)
    final_dict = []
    tile_width =    int( width / ( len( map[0] ) ) )
    tile_height = int(  height / len(map)    )

    # converting list to a dictionary with cordinates
    temp_dict = {}
    for row_index,row in enumerate(map):
        for item_index,item in enumerate(row):
            temp_dict.update( {( (item_index * tile_width ),(row_index * tile_height)  ) : item } )
        final_dict.append(temp_dict)
        temp_dict = {}
    
    return final_dict



def map_draw(map):
    # tileset should be a dictionary assigning each value in the txt file to a tile, e.g # --> snowtile
    for row in map:
        for item in row:
            pass

