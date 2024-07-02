import random

def choose_first():
    if random.randint(0,1)== 0:
        return 'Player2'
    else :
        return 'Player1'
    pass