from dataclasses import dataclass, field
import random
from typing import List

SUITS = ('Clubs', 'Spades', 'Hearts', 'Diamonds')
RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')


@dataclass(order=True)
class Card():



    sort_index: int = field(init=False, repr=False)
    suit: SUITS
    rank: RANKS
    hidden: bool


    def __post_init__(self):
        self.sort_index = (RANKS.index(self.rank) * len(SUITS)
                            + SUITS.index(self.suit))

    def __str__(self):
        return f'{self.suit} {self.rank}'




@dataclass
class Deck():
    """


    """
    cards: List[Card] = field(default_factory= lambda:[Card(suit, rank, False) for suit in SUITS for rank in RANKS])

    def __iter__(self):
        yield from dataclasses.astuple(self)

    def __len__(self):
        return len(self.cards)

    def __repr__(self):
        cards = ', '.join(f'{r}' for r in self.cards)
        return f'{self.__class__.__name__}({cards})'

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

    def __repr__(self):
        cards = ', '.join(f'{r}' for r in self.cards)
        return f'{self.__class__.__name__}({cards})'

    def add_card(self, card):
        self.cards.append(card)


