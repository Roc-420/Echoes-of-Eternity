import pygame
from colorama import Fore,Back,Style
# Initialize pygame and create window
pygame.init()
DISPLAY_W, DISPLAY_H = 1700, 1200
canvas = pygame.Surface((DISPLAY_W, DISPLAY_H))
window = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
running = True

#takes images from directory (we need to learn how to use spritesheets instead of this)


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
