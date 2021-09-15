from dataclasses import dataclass, field, astuple
from abc import ABC, abstractmethod
import random
from texas_holdem_hashtable import suit_dep, not_suit_dep
from typing import List
from itertools import combinations
import numpy as np

SUITS = ('Clubs', 'Spades', 'Hearts', 'Diamonds')
RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')


@dataclass(order=True, eq=True, unsafe_hash=True)
class Card():
    """
    Class to model a card.

    Each card has a suit (picked from SUITS tuple) and a rank (picked from RANKS tuple);
    these need to be set when initializing.

    Sort index is used to give cards an int value so they can be compared i.e 'Spades K' > 'Heart Q'
    will be True (__post_init__ sets the sort index).

    Hidden is a bool value, to note if players can see the card or not.
    """

    sort_index: int = field(init=False, repr=False)
    suit: SUITS
    rank: RANKS
    hidden: bool

    def __post_init__(self):
        self.sort_index = (RANKS.index(self.rank))

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

    cards: List[Card] = field(default_factory=lambda: [Card(suit, rank, False) for suit in SUITS for rank in RANKS])

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


@dataclass(order=True)
class PokerHand(Hand):

    #sort_index: int = field(init=False, repr=False)
    holding: List[Card] = field(default_factory=lambda: [])
    #value: int

    def add_holdable(self, obj):
        self.holding.append(obj)

    def is_suited(self, community_cards):
        my_cards = self.holding + community_cards
        for suit in SUITS:
            if sum(card.suit == suit for card in my_cards) >= 5:
                for five_cards in combinations(my_cards, 5):
                    print(five_cards)
            for five_cards in combinations(my_cards, 5):
                sum(hash(card) for card in five_cards)




                #print(not_suit_dep.get(ranks))

    def combination_of_hands(self, community_cards):
        my_cards = self.holding + community_cards


