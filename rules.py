from dataclasses import field, dataclass
from typing import List

@dataclass
class Tables():
    players: List = field(default_factory=lambda: [])
    
    def set_players(self, player):
        self.Tables.append(player)
        
    pot: int = 0
    
    def set_pot():
        pass
    
    community_cards: List = field(default_factory=lambda: [])
    
        def lay_community_cards(card):
            self.Tables.append(card)
