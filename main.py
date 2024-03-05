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
    Deck(players)
    Round(player.hand, computer.hand)

    # tests
    for card in player.hand:
        print(card.suit, card.rank, card.img_path)
    
if __name__ == "__main__":
    main()
