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
    for player in players:
        players_hps += 'Player ' + str(player.getId()) + ' HP: ' + str(player.getHealth()) + '\n'

    print('****************\n' + players_hps + '\n****************')

def playerChoices(players):
    for player in players:
        player_input = getpass.getpass('Please input Rock, Paper or Scissors: ')
        player.setChoice(player_input)

def checkRoundResults(players):
    #rock, paper and scissors counts
    rock_count = 0
    paper_count = 0
    scissors_count = 0

    #count rock, paper and scissor choices
    for player in players:
        player_choice = player.getChoice()
        if(player_choice == 'r'):
            rock_count += 1
        elif(player_choice == 'p'):
            paper_count += 1
        else:
            scissors_count += 1

    #do damage to players based on choices
    for player in players:
        player_choice = player.getChoice()
        if(player_choice == 'r'):
            player.damageHealth(paper_count*10)
        elif(player_choice == 'p'):
            player.damageHealth(scissors_count*10)
        else:
            player.damageHealth(rock_count*10)
        
        #remove losers from the list of players
        if(player.getHealth() <= 0):
            #TODO: have players names in the future and print them instead of ids
            print('Player ' + str(player.getId()) + ' has lost!')
            players.remove(player)
        

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
        player_choices = playerChoices(players)

        #clear the terminal
        os.system('cls')

        #get the results of the player choices
        checkRoundResults(players)

        if(len(players) == 1):
            print(str(players[0].getId()) + ' has won!')
            return

main()