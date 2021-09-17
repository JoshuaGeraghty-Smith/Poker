from card import Card, FullDeck, Hand, PokerHand
from player import Player, Humanoid, Bot

from poker_lookup_table import suit_dep, not_suit_dep
import sys


num_of_cards_in_hand = 2

deck = FullDeck()
deck.shuffle()


player1 = Humanoid(1, "Troy", PokerHand())
player2 = Bot(2, "Sam", PokerHand())


#for _ in range(0, num_of_cards_in_hand):
    #player1.hand.add_holdable(deck.deal_card())
    #player2.hand.add_holdable(deck.deal_card())



hold=[Card('Diamonds', '5'),
Card('Clubs', '6')]

com=[Card('Clubs', '7'),
Card('Clubs', 'A'),
Card('Hearts', '9'),
Card('Clubs', 'T'),
Card('Clubs', '8')]

dom=(Card('Clubs', 'A'),
Card('Spades', 'A'),
Card('Hearts', 'K'),
Card('Spades', 'K'),
Card('Diamonds', 'A'))



Troy=PokerHand(hold, community_cards=com )
print(Troy.eval_hand())
