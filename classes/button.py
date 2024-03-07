# Python poker card game
# Jonathan Gabioud
# 2024-03-05

import pygame
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
        
    def card_change(self, player_selection:list, player_hand:list, deck:list):
        for selected_card in player_selection:
            for player_card in player_hand:
                if player_card == selected_card:
                    player_card.selected = False
                    player_hand.remove(selected_card)
                    player_hand.append(deck.cards.pop(0))
        deck.display()
    
    def change_button_event_handler(self, event, player_selection:list, player_hand:list, deck:list):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.button.collidepoint(event.pos):
                    self.card_change(player_selection, player_hand, deck)
                    player_selection.clear()
                    pygame.time.delay(50)
                    
    def play_button_event_handler(self, event, player:object, computer:object):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.button.collidepoint(event.pos):
                    computer.display = True
                    score = Score(player.hand, computer.hand)
                    print(score.check_poker_hand(player.hand))
