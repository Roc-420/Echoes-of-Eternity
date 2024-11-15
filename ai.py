
from random import randrange


# basic ai for combat system

def ai_move(bias,bias_level):
    list = ["rock","paper","scissors"]
    for _ in range(bias_level):
        list.append(bias)

    choice = randrange(0,  (len(list)) )
    return list[choice]



fe = ai_move("rock",2)
print(fe)