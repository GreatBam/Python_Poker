# Python poker card game
# Jonathan Gabioud
# 2024-03-05

import re

class Score:
    def __init__(self, player_hand:list, computer_hand:list):
        self.player_hand = player_hand
        self.computer_hand = computer_hand
        
    def check_poker_hand(self, hand:list):
        suits = [card.suit for card in hand]
        ranks = [card.rank for card in hand]
        # if(self.straight_flush(suits, ranks)):
        #     return "straight flush"
        # elif(self.four_of_a_kind(ranks)):
        #     return "four of a kind"
        # elif(self.full_house(ranks)):
        #     return "full house"
        # elif(self.flush(suits)):
        #     return "flush"
        # elif(self.straight(ranks)):
        #     return "straight"
        # elif(self.three_of_a_kind(ranks)):
        #     return "three of a kind"
        # elif(self.two_pair(ranks)):
        #     return "two pair"
        # elif(self.pair(ranks)):
        #     return "pair"
        # else:
        #     return "high card"
        print(self.rank_counter(ranks, suits))

    def straight_flush(self, suits:list, ranks:list):
        return True if self.flush(suits) and self.straight(ranks) else False
    
    def flush(self, suits:list):
        return True if len(set(suits)) == 1 else False
    
    def straight(self, ranks:list):
        return False
        
    def rank_counter(self, ranks:list, suits:list):
        rank_matrix = [
            {"id":1, "rank":"2", "value": 0},
            {"id":2, "rank":"3", "value": 0},
            {"id":3, "rank":"4", "value": 0},
            {"id":4, "rank":"5", "value": 0},
            {"id":5, "rank":"6", "value": 0},
            {"id":6, "rank":"7", "value": 0},
            {"id":7, "rank":"8", "value": 0},
            {"id":8, "rank":"9", "value": 0},
            {"id":9, "rank":"10", "value": 0},
            {"id":10, "rank":"J", "value": 0},
            {"id":11, "rank":"Q", "value": 0},
            {"id":12, "rank":"K", "value": 0},
            {"id":13, "rank":"A", "value": 0}
        ]
        print(rank_matrix)
        pair_list = []
        trio_list = []
        four_list = []
        numbers = ""
        for rank in ranks:
            for key in rank_matrix:
                if rank == key['rank']:
                    key['value'] += 1
        for key in rank_matrix:
            numbers += str(key['value'])
            if key['value'] == 2:
                pair_list.append(key)
            if key['value'] == 3:
                trio_list.append(key)
            if key['value'] == 4:
                four_list.append(key)
        print(numbers)
        print(pair_list)
        print(len(pair_list))
        print(trio_list)
        print(len(trio_list))
        print(four_list)
        print(len(four_list))
        if re.findall('11111',numbers) and len(set(suits)) == 1:
            return "straight flush"
        if(len(four_list) == 1):
            return "four of a kind"
        if(len(pair_list) == 1 and len(trio_list) == 1):
            return "full house"
        if len(set(suits)) == 1:
            return "flush"
        if re.findall('11111',numbers):
            return "straight"
        if(len(trio_list) == 1) and len(pair_list) == 0:
            return "three of a kind"
        if(len(pair_list) == 2):
            return "two pair"
        if(len(pair_list) == 1) and len(trio_list) == 0:
            return "pair"
        return "high card"