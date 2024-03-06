# Python poker card game
# Jonathan Gabioud
# 2024-03-05

# Importing libraries
import pygame
from classes.deck import Deck
from classes.player import Player
from classes.button import Button
from classes.score import Score

def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    width = screen.get_width()
    height = screen.get_height()
    clock = pygame.time.Clock()
    fps = 30
    running = True
    
    # game setup
    player = Player("player")
    computer = Player("computer")
    players = [player, computer]
    deck = Deck(screen, players)
    player_selection = []
    
    # set card positions
    deck.display()
    
    # card change button
    change_button = Button(screen, width, height)
    change_button.prepare_change_button()
    
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
        change_button.draw()
        change_button.event_handler(event, player_selection, player.hand, deck)

        # display
        pygame.display.flip()

        # fps
        clock.tick(fps)

    pygame.quit()
    
# run the game
if __name__ == "__main__":
    main()
