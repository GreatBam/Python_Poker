import random, re
from card import Card

class Deck:
    def __init__(self, cards:list):
        self.cards = cards
        self.create_deck()
        
    def shuffle(self):
        random.shuffle(self.cards)
        
    def create_deck(self):
        suits_list = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suit = (re.findall(r'\b\w', suits_list)[0]).lower()
        rank = (re.findall(r'\b\w', ranks_list)[0]).lower()
        for suit in suits_list:
            for rank in ranks_list:
                self.cards.append(Card(suit, rank, f'images/{rank}{suit}.png'))
        self.shuffle()