# Python poker card game
# Jonathan Gabioud
# 2024-03-05

class Display:
    def __init__(self, players:list):
        self.players = players
        
    def set(self):
        xPos = 100
        for player in self.players:
            if(player.name == 'player'):
                yPos = 500
            else:
                yPos = 100
            for card in player.hand:
                card.position = (xPos, yPos)
                xPos += 100