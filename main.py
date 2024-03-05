# Python poker card game
# Jonathan Gabioud
# 2024-03-05

# Importing libraries
import pygame
from classes.deck import Deck
from classes.player import Player
from classes.round import Round
from classes.score import Score

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

def main():
    #pygame setup, under construction
    # while running:
    #     # poll for events
    #     # pygame.QUIT event means the user clicked X to close your window
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False

    #     # fill the screen with a color to wipe away anything from last frame
    #     screen.fill("purple")

    #     # RENDER YOUR GAME HERE

    #     # flip() the display to put your work on screen
    #     pygame.display.flip()

    #     clock.tick(60)  # limits FPS to 60

    # pygame.quit()
    
    # /////////////// GAME STARTS HERE FOR NOW /////////////// *
    
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
