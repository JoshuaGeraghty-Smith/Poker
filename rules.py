from dataclasses import field, dataclass
from typing import List

@dataclass
class players():
    players: List = field(default_factory=lambda: [])
    
    def set_players(self, player):
        self.players.append(player)
