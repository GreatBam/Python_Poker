# Python poker card game
# Jonathan Gabioud
# 2024-03-05

import pygame

class Button:
    def __init__(self, player_hand:list, deck:list, screen:object):
        self.player_hand = player_hand
        self.deck = deck
        self.screen = screen
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont("Tahoma", 35)
        self.light_color = (170, 170, 170)
        self.dark_color = (100, 100, 100)
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.text = self.font.render("Change", True, self.text_color)
        self.button_position = (self.width/2)+50,((self.height/2)+(self.height/4))
        self.text_position = ((self.width/2)+61,((self.height/2)+(self.height/4))-5)
        
    def draw(self):
        self.button = pygame.draw.rect(self.screen, self.dark_color, [self.button_position[0], self.button_position[1], 140, 40], 0, 10)
        self.screen.blit(self.text, self.text_position)
        
    def card_change(self):
        for card in self.player_hand:
            if card.selected:
                card.selected = False
                self.player_hand.remove(card)
                self.player_hand.append(self.deck.cards[0])
                self.deck.cards.pop(0)
        self.deck.display()
    
    def event_handler(self, event, player_selection:list):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.button.collidepoint(event.pos):
                    print('Button clicked')
                    self.card_change()
                    player_selection.clear()
                    pygame.time.delay(50)
