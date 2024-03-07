class Display:
    def __init__(self, players:list):
        self.players = players
        
    def display(self):
        xPos = 100
        for player in self.players:
            if(player.name == 'player'):
                yPos = 500
            else:
                yPos = 100
            for card in player.hand:
                card.position = (xPos, yPos)
                xPos += 100