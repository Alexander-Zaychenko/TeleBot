from random import randint

def engine(computer_choice, player_choice):
    if player_choice < 4 and player_choice > 0:
      if computer_choice == player_choice:
          return "Ничья! "
      elif computer_choice == 1 and player_choice == 2 or computer_choice == 2 and player_choice == 3 or computer_choice == 3 and player_choice == 1:
          return "Поражение! "
      elif computer_choice == 2 and player_choice == 1 or computer_choice == 3 and player_choice == 2 or computer_choice == 1 and player_choice == 3:
          return "Победа! "
    else:
        return "Ошибка! "

  
def in_game(player_choice):
    computer_choice = randint(1, 3)
    return engine(computer_choice, int(player_choice))
  