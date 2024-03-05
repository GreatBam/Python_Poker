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
        self.selected = False
        
    def draw(self):
        self.image = self.screen.blit(self.img_path, self.position)
        
    def draw_back(self):
        self.back_image = self.screen.blit(self.back_img_path, self.position)
        
    def event_handler(self, event, player_selection:list):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.image.collidepoint(event.pos):
                    if(self.position[1] == 500):
                        if(len(player_selection) < 3):
                            self.position = (self.position[0], self.position[1] - 20)
                            player_selection.append(self)
                            self.selected = True
                    elif(self.position[1] == 480):
                        self.position = (self.position[0], self.position[1] + 20)
                        player_selection.remove(self)
                        self.selected = False
                pygame.time.delay(50)
