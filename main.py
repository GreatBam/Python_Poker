# Python poker card game
# Jonathan Gabioud
# 2024-03-05

# Importing libraries
import random, re
from classes.deck import Deck
from classes.player import Player
from classes.round import Round
from classes.score import Score

def main():

    player_name = input('Enter your name: ')
    player = Player(player_name)
    computer = Player("computer")
    players = [player, computer]
    deck = Deck(players)
    round =Round(player.hand, computer.hand, deck)
    round.show_player_hand()
    round.ask_cards_change()
    
    print('Computer hand is:')
    
if __name__ == "__main__":
    main()
