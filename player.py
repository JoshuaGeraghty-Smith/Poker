from dataclasses import dataclass, field
from card import Hand
from abc import ABC, abstractmethod


@dataclass
class Player(ABC):
    """
    Abstract class for player entities, takes in an id and name on initialization,
    every player has a chip value and hand object.
    """
    id: int
    name: str
    chips: int = 0
    hand: Hand = field(default_factory=lambda: Hand())

    def __str__(self):
        return f'{self.id}   {self.name}   Chips: {self.chips}   {self.hand}'

    @abstractmethod
    def place_bet(self):
        pass


@dataclass
class Humanoid(Player):

    def place_bet(self):
        return 250


@dataclass
class Bot(Player):

    def place_bet(self):
        return 100
