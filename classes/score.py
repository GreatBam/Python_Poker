# Python poker card game
# Jonathan Gabioud
# 2024-03-05

class Score:
    def __init__(self, player_hand:list, computer_hand:list):
        self.player_hand = player_hand
        self.computer_hand = computer_hand
        
    def check_poker_hand(self, hand:list):
        suits = [card.suit for card in hand]
        ranks = [card.rank for card in hand]
        if(self.straight_flush(suits, ranks)):
            return "straight flush"
        elif(self.four_of_a_kind(ranks)):
            return "four of a kind"
        elif(self.full_house(ranks)):
            return "full house"
        elif(self.flush(suits)):
            return "flush"
        elif(self.straight(ranks)):
            return "straight"
        elif(self.three_of_a_kind(ranks)):
            return "three of a kind"
        elif(self.two_pair(ranks)):
            return "two pair"
        elif(self.pair(ranks)):
            return "pair"
        else:
            return "high card"
