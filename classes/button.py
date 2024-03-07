# Python poker card game
# Jonathan Gabioud
# 2024-03-05

import pygame
from classes.change import Change
from classes.score import Score

class Button:
    def __init__(self, screen:object, width:int, height:int, label:str, button_pos:tuple, text_pos:tuple, color:tuple): 
        self.screen = screen
        self.width = width
        self.height = height
        self.label = label
        self.button_position = button_pos
        self.text_position = text_pos
        self.button_color = color
        self.font = pygame.font.SysFont("Tahoma", 35)
        self.text_color = (255, 255, 255)
        self.text = self.font.render(self.label, True, self.text_color)
        
    def draw(self):
        self.button = pygame.draw.rect(self.screen, self.button_color, [self.button_position[0], self.button_position[1], 140, 40], 0, 10)
        self.screen.blit(self.text, self.text_position)
    
    def change_button_event_handler(self, event, player_selection:list, player_hand:list, change:object):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.button.collidepoint(event.pos):
                    change.card_change(player_selection, player_hand)
                    player_selection.clear()
                    pygame.time.delay(50)
                    
    def play_button_event_handler(self, event, player:object, computer:object):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.button.collidepoint(event.pos):
                    computer.show_cards = True
                    score = Score(player.hand, computer.hand)
                    print(score.check_poker_hand(player.hand))
                    
    def reset_button_event_handler(self, event, players:list, deck:object, pile:object, display:object):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.button.collidepoint(event.pos):
                    for player in players:
                        if player.name == "computer":
                            player.show_cards = False
                        deck.cards.append(player.hand)
                        player.hand.clear()
                    deck.shuffle()
                    pile.deal()
                    display.set()
                    pygame.time.delay(50)
