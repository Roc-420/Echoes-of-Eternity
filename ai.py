
from random import randrange


# basic ai for combat system

def ai_move(bias,bias_level):
    list = ["rock","paper","scissors"]
    for _ in range(bias_level):
        list.append(bias)

    choice = randrange(0,  (len(list)) )
    return list[choice]


def win_check(move_1,move_2):
    list = ["rock","paper","scissors","rock"]
    move_pos_1 = list.index(move_1)
    move_pos_2  = list.index(move_2)
    if move_1 == move_2:
        print("tie!!")
    elif move_1 == list[ move_pos_2 +1  ]:
        print("player 1 wins!!")
    elif move_2 == list[move_pos_1 + 1]:
        print("player 2 wins!!")
fe = ai_move("rock",2)
print(fe)


win_check("rock","rock")