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

    def straight_flush(self, suits:list, ranks:list):
        return True if self.flush(suits) and self.straight(ranks) else False
    
    def flush(self, suits:list):
        return True if len(set(suits)) == 1 else False
    
    def straight(self, ranks:list):
        return False
        
    def rank_counter(self, ranks:list):
        rank_matrix = {
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0,
            "6": 0,
            "7": 0,
            "8": 0,
            "9": 0,
            "10": 0,
            "J": 0,
            "Q": 0,
            "K": 0,
            "A": 0
        }
        pair_list = []
        trio_list = []
        four_list = []
        for rank in ranks:
            for key in rank_matrix:
                if rank == key:
                    rank_matrix[key] += 1
        for key in rank_matrix:
            if rank_matrix[key] == 2:
                pair_list.append(key)
            if rank_matrix[key] == 3:
                trio_list.append(key)
            if rank_matrix[key] == 4:
                four_list.append(key)
        if(len(pair_list) == 1) and len(trio_list) == 0:
            return "pair"
        if(len(pair_list) == 2):
            return "two pair"
        if(len(trio_list) == 1) and len(pair_list) == 0:
            return "three of a kind"
        if(len(four_list) == 1):
            return "four of a kind"
        if(len(pair_list) == 1 and len(trio_list) == 1):
            return "full house"