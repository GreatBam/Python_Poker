# Python poker card game
# Jonathan Gabioud
# 2024-03-05

# Importing libraries
import random, re
from classes.deck import Deck
from classes.player import Player
from classes.score import Score
# from classes.card import Card

deck = Deck()

for card in deck.cards:
    print(card.suit, card.rank, card.img_path)