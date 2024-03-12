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
        print(self.rank_counter(ranks, suits))
        
    def rank_counter(self, ranks:list, suits:list):
        rank_count_list = {
            "2" : 0,
            "3" : 0,
            "4" : 0,
            "5" : 0,
            "6" : 0,
            "7" : 0,
            "8" : 0,
            "9" : 0,
            "10" : 0,
            "J" : 0,
            "Q" : 0,
            "K" : 0,
            "A" : 0
        }
        pair_list = []
        trio_list = []
        four_list = []
        numbers = ""
        for rank in ranks:
            for key in rank_count_list:
                if rank == key:
                    rank_count_list[key] += 1
        for key in rank_count_list:
            numbers += str(rank_count_list[key])
            if rank_count_list[key] == 2:
                pair_list.append(key)
            if rank_count_list[key] == 3:
                trio_list.append(key)
            if rank_count_list[key] == 4:
                four_list.append(key)
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