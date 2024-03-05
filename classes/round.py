import re

class Round:
    def __init__(self, player_hand:list, computer_hand:list, deck:list):
        self.player_hand = player_hand
        self.computer_hand = computer_hand
        self.deck = deck
        self.correct_input = False
        self.check = False
        self.cards_to_change_list = []
        
    def show_player_hand(self):
        hand = ''
        for card in self.player_hand:
            hand += f'{card.suit} {card.rank} | '
        print(hand)
        
    def show_computer_hand(self):
        hand = ''
        for card in self.computer_hand:
            hand += f'{card.suit} {card.rank} | '
        print(hand)
        
    def ask_cards_change(self):
        while self.correct_input == False and self.check == False:
            changes_str = input('\nWhich cards would you like to change [1-5]? (up to 3 card):\nPress enter to skip\n')
            test_str = re.search('[a-zA-Z]', changes_str)
            if test_str == None:
                self.correct_input = True
            else:
                print('Please enter a valid input')
            self.cards_to_change_list = [int(x) for x in changes_str]
            if(len(self.cards_to_change_list) <= 3):
                self.check = True
            else:
                print('You can only change up to 3 cards')
        self.cards_change()

    def cards_change(self):
        for i in range(len(self.cards_to_change_list)):
            self.cards_to_change_list[i] = int(self.cards_to_change_list[i]) - 1
        position = 0
        for card in self.cards_to_change_list:
            self.player_hand.pop(int(card) - position)
            self.player_hand.append(self.deck.cards[0])
            self.deck.cards.pop(0)
            position += 1
        self.show_player_hand()                
                