'''Importing the required modules'''
from colorama import init, Fore
import utils
init()
number_of_players = int(input('Enter number of players. '))
winner_num: int = 0
winner_score: int = 0
for player_number in range(number_of_players):
    player: utils.Player = utils.Player(player_number)
    player_result: int = player.move()
    if player_result > winner_score:
        winner_num = player_number
        winner_result = player_result
if winner_score == 0:
    print(Fore.GREEN, ' IT WAS AN EQUAL GAME, DRAW!')
else:
    print(Fore.GREEN, ' PLAYER ' + str(winner_num + 1) +
          ' WON WITH A SCORE OF ' + str(winner_result) + '!')
