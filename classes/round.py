import re

class Round:
    def __init__(self, player_hand:list, computer_hand:list, deck:list):
        self.player_hand = player_hand
        self.computer_hand = computer_hand
        self.deck = deck
        self.list_of_ints = []
        self.check = False
        
    def show_player_hand(self):
        hand = ''
        for card in self.player_hand:
            hand += f'{card.suit} {card.rank} | '
        print(hand)
        
    def ask_cards_change(self):
        correct_input = False
        while correct_input == False and self.check == False:
            changes_str = input('\nWhich cards would you like to change [1-5]? (up to 3 card):\nPress enter to skip\n')
            test_str = re.search('[a-zA-Z]', changes_str)
            if test_str == None:
                correct_input = True
            else:
                print('Please enter a valid input')
            self.list_of_ints = [int(x) for x in changes_str]
            if(len(self.list_of_ints) <= 3):
                self.check = True
            else:
                print('You can only change up to 3 cards')
        self.cards_change()

                
                