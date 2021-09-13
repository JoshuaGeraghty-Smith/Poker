from dataclasses import dataclass, field
from card import Hand

@dataclass
class Player():

    id: int
    name: str
    chips: int = 0
    hand: Hand = field(default_factory= lambda:Hand())


    def __str__(self):
        return f'{self.id}   {self.name}   Chips: {self.chips}   {self.hand}'



