# Python poker card game
# Jonathan Gabioud
# 2024-03-05

class Pile:
    def __init__(self, deck:object, players:list):
        self.deck = deck
        self.players = players
        
    def deal(self):
        for _ in range(5):
            for player in self.players:
                player.hand.append(self.deck.cards.pop(0))