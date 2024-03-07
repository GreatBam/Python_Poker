# Python poker card game
# Jonathan Gabioud
# 2024-03-05

# Importing libraries
import pygame
from classes.deck import Deck
from classes.player import Player
from classes.button import Button
from classes.pile import Pile

def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    width = screen.get_width()
    height = screen.get_height()
    clock = pygame.time.Clock()
    fps = 60
    running = True
    
    # players creation
    player = Player("player", True)
    computer = Player("computer", False)
    players = [player, computer]
    
    # deck creation
    deck = Deck(screen, players)
    
    # pile creation and cards dealing
    pile = Pile(deck, players)
    pile.deal()
    
    # player card change selection
    player_selection = []
    
    # buttons
    change_button = Button(screen,
                           width,
                           height,
                           "Change",
                           ((width/2)-250,height/2),
                           ((width/2)-239,((height/2)-5)),
                           (100, 100, 100))
    play_button = Button(screen,
                         width,
                         height,
                         "Play",
                         ((width/2)-50,height/2),
                         ((width/2)-10,((height/2)-5)),
                         (0, 0, 255))
    reset_button = Button(screen,
                          width,
                          height,
                          "Reset",
                          ((width/2)+150,height/2),
                          ((width/2)+190,((height/2)-5)),
                          (255, 0, 0))
    
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
            if computer.display:
                card.draw()
            else:
                card.draw_back()
            
        # buttons
        change_button.draw()
        change_button.change_button_event_handler(event, player_selection, player.hand, deck)
        play_button.draw()
        play_button.play_button_event_handler(event, player, computer)
        reset_button.draw()

        # display
        pygame.display.flip()

        # fps
        clock.tick(fps)

    pygame.quit()
    
# run the game
if __name__ == "__main__":
    main()
