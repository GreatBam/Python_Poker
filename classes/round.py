import re

class Round:
    def __init__(self, player_hand:list, computer_hand:list):
        self.player_hand = player_hand
        self.computer_hand = computer_hand
        self.cards_change()
        
    def cards_change(self):
        correct_input = False
        while False == correct_input:
            changes_str = input('\nWhich cards would you like to change [1-5]? (up to 3 card):\nPress enter to skip\n')
            test_str = re.search('[a-zA-Z]', changes_str)
            if test_str == None:
                correct_input = True
            else:
                print('Please enter a valid input')
        print("Hello world")