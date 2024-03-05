# Python poker card game
# Jonathan Gabioud
# 2024-03-05

import pygame

class Card:
    def __init__(self, suit:str, rank:str, img_path:str, screen:object, x, y):
        self.suit = suit
        self.rank = rank
        self.img_path = img_path
        self.screen = screen
        self.position = (x, y)
        self.back_img_path = pygame.image.load('images/back.png')
        
    def draw(self):
        self.image = self.screen.blit(self.img_path, self.position)
        
    def draw_back(self):
        self.back_image = self.screen.blit(self.back_img_path, self.position)
        
    def event_handler(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.image.collidepoint(event.pos):
                    # debug
                    # print(f'{self.rank} of {self.suit} clicked')
                    if(self.position[1] == 500):
                        self.position = (self.position[0], self.position[1] - 20)
                    elif(self.position[1] == 480):
                        self.position = (self.position[0], self.position[1] + 20)
                    pygame.time.delay(100)
