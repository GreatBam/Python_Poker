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