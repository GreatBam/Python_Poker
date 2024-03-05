# Python poker card game
# Jonathan Gabioud
# 2024-03-05

import pygame

class Card:
    def __init__(self, suit:str, rank:str, img_path:str, x, y):
        self.suit = suit
        self.rank = rank
        self.img_path = img_path
        self.back_img_path = pygame.image.load('images/back.png')
        self.position = (x, y)
        
    def draw(self, screen:object):
        self.image = screen.blit(self.img_path, self.position)
        
    def draw_back(self, screen:object):
        self.back_image = screen.blit(self.back_img_path, self.position)
        
    def event_handler(self, event, screen:object):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.image.collidepoint(event.pos):
                    print(f'{self.rank} of {self.suit} clicked')
                    self.position = (self.position[0], self.position[1] - 20)
                    self.image = screen.blit(self.img_path, self.position)
                    # if(self.position[1] == 500):
                    #     print(f'{self.rank} of {self.suit} clicked')
                    #     self.position = (self.position[0], self.position[1] - 20)
                    #     self.image = screen.blit(self.img_path, self.position)
                    # else:
                    #     self.position = (self.position[0], self.position[1] + 20)
                    #     self.image = screen.blit(self.img_path, self.position)
