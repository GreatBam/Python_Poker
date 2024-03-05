# Python poker card game
# Jonathan Gabioud
# 2024-03-05

# Importing libraries
import pygame
from classes.deck import Deck
from classes.player import Player
from classes.button import Button
from classes.round import Round
from classes.score import Score

def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    fps = 30
    running = True
    
    # game setup
    # player_name = input('Enter your name: ') # under construction
    player = Player("player")
    computer = Player("computer")
    players = [player, computer]
    deck = Deck(screen, players)
    player_selection = []
    
    # set card positions
    deck.display()
    
    # card change button
    button = Button(player.hand, deck, screen)
    
    # game loop
    while running:
        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # screen background color
        screen.fill("green")
        
        # RENDER GAME
        for card in player.hand:
            card.draw()
            card.event_handler(event, player_selection)
            
        for card in computer.hand:
            card.draw_back()
            
        # card change button
        button.draw()

        # display
        pygame.display.flip()

        # fps
        clock.tick(fps)

    pygame.quit()
    
# run the game
if __name__ == "__main__":
    main()

# /////////////// TERMINAL GAME REMAINDER /////////////// *

# # ask for player's name
# player_name = input('Enter your name: ')
# # create player and computer
# player = Player(player_name)
# computer = Player("computer")
# players = [player, computer]
# # create deck
# deck = Deck(players)
# # start  round
# round =Round(player.hand, computer.hand, deck)
# round.show_player_hand()
# # ask player for cards to change
# round.ask_cards_change()
# # show computer hand
# print('Computer hand is:')
# round.show_computer_hand()