import getpass
import os
from Player_class import Player

def createPlayers():
    player_count = 0

    #get player count
    while(player_count <= 0):
        player_count = int(input('Input the amount of Players: '))
    
    #create players
    players = []
    for i in range(player_count):
        players.append(Player())
    return players

def printPlayerHeaths(players):
    players_hps = ''
    for i in range(players):
        players += 'Player ' + players[i].getId() + ' HP: ' + str(players[i].getHealth() + '\n')

    print('****************\n' + players_hps + '\n****************')

def playerChoices(players):
    for i in range(len(players)):
        player_input = getpass.getpass('Please input Rock, Paper or Scissors: ')
        players[i].setChoice(player_input)

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
    #display controls
    print('Controls: r = Rock, p = Paper, s = Scissors, press ENTER to submit your choice')

    #create both players
    players = createPlayers()
    game_on = True
    while game_on:
        #display players healths
        printPlayerHeaths(players)

        #players input their choice of rock, paper or scissors
        playerChoices = playerChoices(players)

        #clear the terminal
        os.system('cls')

        #TODO: UPDATE THIS
        #get the results of the player choices
        roundResults = checkRoundResults(players)

        #deal damage to loser of the round
        if(roundResults == 0):
            player2.damageHealth(10)
            print('Player 1 won the round!')
        elif(roundResults == 1):
            player1.damageHealth(10)
            print('Player 2 won the round!')
        else:
            print('Draw!')

        #check to see if any of the players won
        if(player1.getHealth() == 0):
                os.system('cls')
                print('Player 2 wins!')
                game_on = False
        elif(player2.getHealth() == 0):
                os.system('cls')
                print('Player 1 wins!')
                game_on = False

main()