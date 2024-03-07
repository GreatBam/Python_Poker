# Python poker card game
# Jonathan Gabioud
# 2024-03-05

class Player:
    def __init__(self, name:str, show_cards:bool):
        self.name = name
        self.hand = []
        self.show_cards = show_cards
        if(name == 'player'):
            self.play_state = False
            self.changes = 3