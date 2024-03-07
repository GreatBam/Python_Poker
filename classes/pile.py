class Pile:
    def __init__(self, deck:object, players:list):
        self.deck = deck
        self.players = players
        
    def deal(self):
        for _ in range(5):
            for player in self.players:
                player.hand.append(self.cards.pop(0))