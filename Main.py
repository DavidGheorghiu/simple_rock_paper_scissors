import getpass
import os
from Player_class import Player as pl

def printPlayerHeaths(player1, player2):
    print('********************')
    print('* Player 1 HP: ' + str(player1.getHealth()) + ' *')
    print('* Player 2 HP: ' + str(player2.getHealth()) + ' *')
    print('********************')

def checkResults(player1_input, player2_input):
    print('lol')

def main():
    player1 = pl()
    player2 = pl()
    print('Controls: r = Rock, p = Paper, s = Scissors, press ENTER to submit your choice')
    while True:
        printPlayerHeaths(player1, player2)
        player1_input = getpass.getpass('Please input Rock, Paper or Scissors: ').lower()
        player2_input = getpass.getpass('Please input Rock, Paper or Scissors: ').lower()
        checkResults(player1_input, player2_input)
        os.system('clear')

main()