import dataclasses
import random

SUITS = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


@dataclasses.dataclass
class Card():
    suit: SUITS
    rank: RANKS
    hidden: bool


@dataclasses.dataclass
class Deck():
    cards: [Card]

    def __iter__(self):
        yield from dataclasses.astuple(self)

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        card = self.cards.pop(0)
        return card


@dataclasses.dataclass
class Hand():
    cards: [Card]

    def __iter__(self):
        yield from dataclasses.astuple(self)

    def add_card(self, card):
        self.hand.append(card)


cards = [Card(suit, rank, False) for suit in SUITS for rank in RANKS]
deck = Deck(cards)
deck.shuffle()
for card in deck:
    print(card)
print(len(deck))
