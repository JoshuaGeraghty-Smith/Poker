from dataclasses import dataclass, field, astuple
from abc import ABC, abstractmethod
import random
from poker_lookup_table import suit_dep, not_suit_dep
from typing import List
from itertools import combinations
import numpy as np
from collections import namedtuple

SUITS = ('Clubs', 'Spades', 'Hearts', 'Diamonds')
RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')


@dataclass(order=True, eq=True, frozen=True)
class Card():
    """
    Class to model a card.

    Each card has a suit (picked from SUITS tuple) and a rank (picked from RANKS tuple);
    these need to be set when initializing.

    Sort index is used to give cards an int value so they can be compared i.e 'Spades K' > 'Heart Q'
    will be True (__post_init__ sets the sort index).

    Hidden is a bool value, to note if players can see the card or not.
    """
    __slots__ = ('rank', 'suit')
    suit: SUITS
    rank: RANKS


    def __eq__(self, other):
        """
        Only look at rank.
        """
        if not isinstance(other, Card):
            return NotImplemented
        return self.rank == other.rank

    def __str__(self):
        return f'{self.suit} {self.rank}'


@dataclass()
class FullDeck():
    """
    Class to model a deck of cards.
    Has cards attribute which is a list type. Has a default factory to run a function on initialization.
    Can be iterated through and length is the length of the cards attribute.
    """

    # Lambda function creates a list of 52 unique Cards using the SUITS and RANKS tuples.

    cards: List[Card] = field(default_factory=lambda: [Card(suit, rank) for suit in SUITS for rank in RANKS])

    def __iter__(self):
        yield from astuple(self)

    def __len__(self):
        return len(self.cards)

    def __eq__(self, other):
        """
        Needs to have same order and contents to be equal.
        """
        if not isinstance(other, FullDeck):
            return NotImplemented
        return self.cards == other.cards

    def __repr__(self):
        cards = ', '.join(f'{r}' for r in self.cards)
        return f'{self.__class__.__name__}({cards})'

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        card = self.cards.pop(0)
        return card


@dataclass
class Hand(ABC):
    """
    Class to model a hand.
    Has cards attribute which is a list type. Has a default factory to run a function on initialization.

    """

    # Lambda function creates an empty list
    holding: List = field(default_factory=lambda: [])

    def __iter__(self):
        yield from astuple(self)

    def __repr__(self):
        holding = ', '.join(f'{r}' for r in self.holding)
        return f'{self.__class__.__name__}({holding})'

    @abstractmethod
    def add_holdable(self, obj):
        pass


@dataclass()
class PokerHand():

    holding: List[Card] = field(default_factory=lambda: [])
    community_cards: List[Card] = field(default_factory=lambda: [])


    def add_holdable(self, obj):
        self.holding.append(obj)

    def eval_hand(self):
        my_cards = self.holding + self.community_cards


        suit_hand = []
        for suit in SUITS:
            if sum(card.suit == suit for card in my_cards) >= 5:
                suited_cards = [card for card in my_cards if card.suit == suit]
                suit_hand=self.find_best_hand(suited_cards, hash_table=suit_dep)

        values=[self.find_best_hand(five_cards, not_suit_dep) for five_cards in combinations(my_cards, 5)]
        values = [x for x in values if x is not None]
        return min(min(values), suit_hand)


    @staticmethod
    def _hash_func(hand, hash_table):
        ranks_of_hand = []
        for card in hand:
            ranks_of_hand.append(card.rank)
        lookup_string="".join(sorted(ranks_of_hand))
        return hash_table.get(lookup_string)

    def find_best_hand(self, cards, hash_table):
        for five_cards in combinations(cards, 5):
            value = self._hash_func(five_cards, hash_table)
            if value is not None:
                return int(value)
        return None










