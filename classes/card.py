# Python poker card game
# Jonathan Gabioud
# 2024-03-05

class Card:
    def __init__(self, suit:str, rank:str, img_path:str):
        self.suit = suit
        self.rank = rank
        self.img_path = img_path