# Python poker card game
# Jonathan Gabioud
# 2024-03-05

class Player:
    def __init__(self, name:str, display:bool):
        self.name = name
        self.hand = []
        self.display = display