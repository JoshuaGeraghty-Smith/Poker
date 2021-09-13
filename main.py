from card import Card, Deck, Hand
from player import Player

num_of_cards_in_hand = 2

deck = Deck()
deck.shuffle()


player1 = Player(1, "Troy")
player2 = Player(2, "Sam")

for _ in range(0,num_of_cards_in_hand):
    player1.hand.add_card(deck.deal_card())
    player2.hand.add_card(deck.deal_card())

print(player1)
print(player2)
