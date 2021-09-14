from card import Card, Deck, Hand
from player import Player, Humanoid, Bot

num_of_cards_in_hand = 2

deck = Deck()
deck.shuffle()


player1 = Humanoid(1, "Troy")
player2 = Bot(2, "Sam")

for _ in range(0, num_of_cards_in_hand):
    player1.hand.add_card(deck.deal_card())
    player2.hand.add_card(deck.deal_card())


print(player1)
print(player2)
