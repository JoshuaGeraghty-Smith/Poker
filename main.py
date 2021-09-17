from card import Card, FullDeck, Hand, PokerHand
from player import Player, Humanoid, Bot

from poker_lookup_table import suit_dep, not_suit_dep
import sys


def lookup_hash_table(ht):
    new_keys = []
    for five_cards in ht.keys():
        hand = []
        for rank in five_cards:
            card = Card('Spades', rank)
            hand.append(hash(card))
        new_keys.append(hand)

    print(new_keys)
    return dict(zip(new_keys, ht.values()))


print(sys.getsizeof(not_suit_dep))
print(Card('Clubs', 'A').rank)
num_of_cards_in_hand = 2

deck = FullDeck()
deck.shuffle()


player1 = Humanoid(1, "Troy", PokerHand())
player2 = Bot(2, "Sam", PokerHand())


#for _ in range(0, num_of_cards_in_hand):
    #player1.hand.add_holdable(deck.deal_card())
    #player2.hand.add_holdable(deck.deal_card())



hold=[Card('Clubs', '5'),
Card('Clubs', 'A')]

com=[Card('Clubs', '7'),
Card('Spades', 'A'),
Card('Hearts', '2'),
Card('Clubs', '3'),
Card('Clubs', 'K')]

dom=(Card('Clubs', 'A'),
Card('Spades', 'A'),
Card('Hearts', 'K'),
Card('Spades', 'K'),
Card('Diamonds', 'A'))



Troy=PokerHand(hold, community_cards=com )
print(Troy.eval_hand())
