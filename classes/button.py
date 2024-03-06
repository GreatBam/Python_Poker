# Python poker card game
# Jonathan Gabioud
# 2024-03-05

import pygame

class Button:
    def __init__(self, screen:object, width:int, height:int):
        self.screen = screen
        self.width = width
        self.height = height
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont("Tahoma", 35)
        self.light_color = (170, 170, 170)
        self.dark_color = (100, 100, 100)
        
    def prepare_change_button(self):
        self.button_position = (self.width/2)+50,((self.height/2)+(self.height/4))
        self.text_position = ((self.width/2)+61,((self.height/2)+(self.height/4))-5)
        self.text = self.font.render("Change", True, self.text_color)
        
    def draw(self):
        self.button = pygame.draw.rect(self.screen, self.dark_color, [self.button_position[0], self.button_position[1], 140, 40], 0, 10)
        self.screen.blit(self.text, self.text_position)
        
    def card_change(self, player_selection:list, player_hand:list, deck:list):
        for selected_card in player_selection:
            for player_card in player_hand:
                if player_card == selected_card:
                    player_card.selected = False
                    player_hand.remove(selected_card)
                    player_hand.append(deck.cards.pop(0))
        deck.display()
    
    def event_handler(self, event, player_selection:list, player_hand:list, deck:list):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.button.collidepoint(event.pos):
                    self.card_change(player_selection, player_hand, deck)
                    player_selection.clear()
                    pygame.time.delay(50)
