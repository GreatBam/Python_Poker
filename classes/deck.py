# Python poker card game
# Jonathan Gabioud
# 2024-03-05

import random, re, pygame
from classes.card import Card

class Deck:
    def __init__(self, screen:object, players:list):
        self.screen = screen
        self.cards = self.create_deck()
        self.shuffle()
        self.deal(players)
        
    def shuffle(self):
        random.shuffle(self.cards)
        
    def create_deck(self):
        suits_list = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        cards = []
        for suit in suits_list:
            for rank in ranks_list:
                suit_path = (re.findall(r'\b\w', suit)[0]).lower()
                rank_path = rank.lower()
                image = pygame.image.load(f'images/{suit_path}{rank_path}.png')
                cards.append(Card(suit, rank, image, self.screen, 0, 0))
        return cards
    
    def deal(self, players):
        for _ in range(5):
            for player in players:
                player.hand.append(self.cards.pop(0))