from dataclasses import dataclass, field
import random
from typing import List

SUITS = ['♣, ♢, ♡, ♠']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


@dataclass
class Card():
    suit: SUITS
    rank: RANKS
    hidden: bool

    def __str__(self):
        return f'{self.suit}{self.rank}'


@dataclass
class Deck():
    cards: List[Card] = field(default_factory= lambda:[Card(suit, rank, False) for suit in SUITS for rank in RANKS])

    def __iter__(self):
        yield from dataclasses.astuple(self)

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        card = self.cards.pop(0)
        return card


@dataclass
class Hand():
    cards: List[Card] = field(default_factory= lambda:[])

    def __iter__(self):
        yield from dataclasses.astuple(self)

    def add_card(self, card):
        self.cards.append(card)






deck = Deck()
deck.shuffle()
#print(deck)
player_hand = Hand()
player_hand.add_card(deck.deal_card())
print(player_hand)
