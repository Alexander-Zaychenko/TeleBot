from random import randint

def engine(computer_choice, player_choice):
    if computer_choice == player_choice:
        return "Ничья! "
    elif computer_choice == 1 and player_choice == 2 or computer_choice == 2 and player_choice == 3 or computer_choice == 3 and player_choice == 1:
        return "Поражение! "
    elif computer_choice == 2 and player_choice == 1 or computer_choice == 3 and player_choice == 2 or computer_choice == 1 and player_choice == 3:
        return "Победа! "

  
def game(player_choice):
    computer_choice = randint(1, 3)
    engine(computer_choice, player_choice)
  