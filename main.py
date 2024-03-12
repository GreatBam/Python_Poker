# Python poker card game
# Jonathan Gabioud
# 2024-03-05

# Importing libraries
import pygame
from classes.player import Player
from classes.deck import Deck
from classes.pile import Pile
from classes.display import Display
from classes.change import Change
from classes.button import Button
from classes.score import Score

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
    deck.create_deck()
    deck.shuffle()
    
    # pile creation and cards dealing
    pile = Pile(deck, players)
    pile.deal()

    # display cards on board
    display = Display(players)
    display.set()
    
    # set card changes
    change = Change(deck, display)
    
    # player card change selection
    player_selection = []
    
    # prepare score object
    score = Score(screen, width, height)
    
    # create buttons
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
                          ((width/2)+178,((height/2)-5)),
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
            card.event_handler(event,
                               player_selection)
            
        for card in computer.hand:
            if computer.show_cards:
                card.draw()
            else:
                card.draw_back()

        # draw buttons
        if(player.play_state == False):
            play_button.draw()
            play_button.play_button_event_handler(event,
                                                player,
                                                computer)
            change_button.draw()
            change_button.change_button_event_handler(event,
                                                    player_selection,
                                                    player,
                                                    change)
        else:
            reset_button.draw()
            reset_button.reset_button_event_handler(event,
                                                    players,
                                                    deck,
                                                    pile,
                                                    display)

        # display
        pygame.display.flip()

        # fps
        clock.tick(fps)

    pygame.quit()
    
# run the game
if __name__ == "__main__":
    main()
