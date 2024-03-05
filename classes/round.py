import re

class Round:
    def __init__(self, player_hand:list, computer_hand:list, deck:list):
        self.player_hand = player_hand
        self.computer_hand = computer_hand
        self.deck = deck
        
    def show_player_hand(self):
        hand = ''
        for card in self.player_hand:
            hand += f'{card.suit} {card.rank} | '
        print(hand)
        
    def cards_change(self):
        correct_input = False
        while False == correct_input:
            changes_str = input('\nWhich cards would you like to change [1-5]? (up to 3 card):\nPress enter to skip\n')
            test_str = re.search('[a-zA-Z]', changes_str)
            if test_str == None:
                correct_input = True
            else:
                print('Please enter a valid input')
        list_of_ints = [int(x) for x in changes_str]
        turn = 0
        check = False
        while check == False:
            if(list_of_ints <= 3):
                for i in list_of_ints:
                    # self.player_hand.pop(i-turn)
                    self.player_hand.insert(i-turn, self.deck.pop(0))
                    turn += 1
                check = True
            else:
                print('You can only change up to 3 cards')
        print('Your new hand is:')
                
                