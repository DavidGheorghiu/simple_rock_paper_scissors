import getpass
import os
from Player_class import Player as pl

def printPlayerHeaths(player1, player2):
    print(
            '****************\n' +
            'Player 1 HP: ' + str(player1.getHealth()) + '\n'
            'Player 2 HP: ' + str(player2.getHealth()) + '\n'
            '****************'
    )

def checkRoundResults(player1_input, player2_input):
    results = player1_input - player2_input
    if(results == -1 or results == -2 or results == 3):
        #player1 won the round
        return 0
    elif(results == 1 or results == 2 or results == -3):
        #player2 won the round
        return 1
    else:
        #draw
        return 2

def main():
    #create both players
    player1 = pl()
    player2 = pl()

    #display controls
    print('Controls: r = Rock, p = Paper, s = Scissors, press ENTER to submit your choice')
    while True:
        #display players healths
        printPlayerHeaths(player1, player2)

        #players input their choice of rock, paper or scissors
        player1_input = getpass.getpass('Please input Rock, Paper or Scissors: ').lower()
        player2_input = getpass.getpass('Please input Rock, Paper or Scissors: ').lower()

        #clear the terminal
        os.system('cls')

        #get the results of the player choices
        roundResults = checkRoundResults(ord(player1_input), ord(player2_input))

        #deal damage to loser of the round
        if(roundResults == 0):
            player2.damageHealth(10)
            print('Player 1 won the round!')
        elif(roundResults == 1):
            player1.damageHealth(10)
            print('Player 2 won the round!')
        else:
            print('Draw!')

main()