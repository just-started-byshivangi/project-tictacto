def player_choice(board):
    position = 'wrong'
    while  position not in range(1,9):
     position = input("Enter your next position(1-9):")
     if space_check(board,int(position)):
      return position   
     else :
         return False
    pass