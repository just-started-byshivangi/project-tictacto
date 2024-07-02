def player_input():
    marker = ''
    
    while marker not in ['X', 'O']:
        marker = input('Player 1: Do you want to be X or O?').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
   