import random

class Deck:
    def __init__(self, cards:list):
        self.cards = cards
        self.shuffle()
        
    def shuffle(self):
        random.shuffle(self.cards)