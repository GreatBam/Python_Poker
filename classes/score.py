# Python poker card game
# Jonathan Gabioud
# 2024-03-05

import pygame, re

class Score:
    def __init__(self, screen:object, width:int, height:int):
        self.screen = screen
        self.width = width
        self.height = height
        self.show = False
        
    def check_poker_hand(self, hand:list):
        # Get the suits and ranks
        suits = [card.suit for card in hand]
        ranks = [card.rank for card in hand]
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
            return {"name":"straight flush", "value":8}
        if(len(four_list) == 1):
            return {"name":"four of a kind", "value":7}
        if(len(pair_list) == 1 and len(trio_list) == 1):
            return {"name":"full house", "value":6}
        if len(set(suits)) == 1:
            return {"name":"flush", "value":5}
        if re.findall('11111',numbers):
            return {"name":"straight", "value":4}
        if(len(trio_list) == 1) and len(pair_list) == 0:
            return {"name":"three of a kind", "value":3}
        if(len(pair_list) == 2):
            return {"name":"two pair", "value":2}
        if(len(pair_list) == 1) and len(trio_list) == 0:
            return {"name":"pair", "value":1}
        return {"name":"high card", "value":1}
    
    def compare_hands(self, player_score:object, computer_score:object):
        player_score_value = player_score['value']
        computer_score_value = computer_score['value']
        if(player_score_value == computer_score_value):
            return "draw"
        if(player_score_value > computer_score_value):
            return f"Player wins with {player_score['name']}"
        return f"Computer wins with {computer_score['name']}"
    
    def show_result(self, player_hand:list, computer_hand:list):
        player_score = self.check_poker_hand(player_hand)
        computer_score = self.check_poker_hand(computer_hand)
        label = self.compare_hands(player_score, computer_score)
        font = pygame.font.SysFont("Tahoma", 35)
        text_color = (255, 255, 255)
        frame_color = (45, 146, 212) # player win color
        frame_color = (226, 32, 32 ) # computer win color
        main_text = font.render(label, True, text_color)
        if(label == "draw"):
            main_text_position = (375, 340)
        else:
            main_text_position = (240, 340)
        pygame.draw.rect(self.screen, frame_color, [50, 225, 700, 250], 0, 10)
        self.screen.blit(main_text, main_text_position)