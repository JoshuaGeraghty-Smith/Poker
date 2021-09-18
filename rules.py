from dataclasses import field, dataclass
from typing import List

@dataclass
class Table():

"""    
This class adds players to the table with a seats limit, lays community cards onto the table and 
adds chips to the pot
"""

    players: List = field(default_factory=lambda: [])
    seats: int = 8
    community_cards: List = field(default_factory=lambda: [])
    pot: int = 0
    
    def add_player(self, player):
        if len(players) < self.seats:
            self.players.append(player)
        
            
    def set_pot():
        pass
    
    
    def lay_community_cards(card):
        self.community_cards.append(card)
