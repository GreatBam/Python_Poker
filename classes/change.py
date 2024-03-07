# Python poker card game
# Jonathan Gabioud
# 2024-03-05

class Change:
    def __init__(self, deck:object, display:object):
        self.deck = deck
        self.display = display
        
    def card_change(self, player_selection:list, player_hand:list):
        for selected_card in player_selection:
            for player_card in player_hand:
                if player_card == selected_card:
                    player_card.selected = False
                    player_hand.remove(selected_card)
                    player_hand.append(self.deck.cards.pop(0))
        self.display.set()