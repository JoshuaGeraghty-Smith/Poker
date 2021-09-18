from dataclasses import field, dataclass
from typing import List

@dataclass
class Table():

"""    
This class adds players to the table, lays community cards onto the table and 
adds chips to the pot
"""

    players: List = field(default_factory=lambda: [])
    
    def set_players(self, player):
        self.players.append(player)
        
        
    pot: int = 0
    
    def set_pot():
        pass
    
    community_cards: List = field(default_factory=lambda: [])
    
    def lay_community_cards(card):
        self.community_cards.append(card)
