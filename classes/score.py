# Python poker card game
# Jonathan Gabioud
# 2024-03-05

import pygame, re

class Score:
    def __init__(self, screen:object, width:int, height:int, player_hand:list, computer_hand:list):
        self.screen = screen
        self.width = width
        self.height = height
        self.player_hand = player_hand
        self.computer_hand = computer_hand
        
    def check_poker_hand(self, hand:list):
        suits = [card.suit for card in hand]
        ranks = [card.rank for card in hand]
        print(self.rank_counter(ranks, suits))
        
    def rank_counter(self, ranks:list, suits:list):
        # Set all the variables
        numbers = ""
        pair_list = []
        trio_list = []
        four_list = []
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
        # Count the number of each rank
        for rank in ranks:
            for key in rank_count_list:
                if rank == key:
                    rank_count_list[key] += 1
        # Set the numbers variable, the pair, trio and four lists
        for key in rank_count_list:
            numbers += str(rank_count_list[key])
            if rank_count_list[key] == 2:
                pair_list.append(key)
            if rank_count_list[key] == 3:
                trio_list.append(key)
            if rank_count_list[key] == 4:
                four_list.append(key)
        # Check the poker hand
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
    
    def show_result(self):
        player_score = self.check_poker_hand(self.player_hand)
        computer_score = self.check_poker_hand(self.computer_hand)
        print(player_score, computer_score)
        pygame.draw.rect(self.screen, "light_gray", [self.button_position[0], self.button_position[1], 140, 40], 0, 10)