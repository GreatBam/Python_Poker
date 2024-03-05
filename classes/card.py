# Python poker card game
# Jonathan Gabioud
# 2024-03-05

import pygame

class Card:
    def __init__(self, suit:str, rank:str, img_path:str):
        self.suit = suit
        self.rank = rank
        self.img_path = img_path
        self.back_img_path = pygame.image.load('images/back.png')
        
    def draw(self, screen:object, x:int, y:int):
        screen.blit(self.img_path, (x, y))
