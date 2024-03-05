# Python poker card game
# Jonathan Gabioud
# 2024-03-05

# Importing libraries
from classes.deck import Deck
from classes.player import Player
from classes.round import Round
from classes.score import Score

def main():
    # ask for player's name
    player_name = input('Enter your name: ')
    # create player and computer
    player = Player(player_name)
    computer = Player("computer")
    players = [player, computer]
    # create deck
    deck = Deck(players)
    # start  round
    round =Round(player.hand, computer.hand, deck)
    round.show_player_hand()
    # ask player for cards to change
    round.ask_cards_change()
    # show computer hand
    print('Computer hand is:')
    round.show_computer_hand()
    
if __name__ == "__main__":
    main()
