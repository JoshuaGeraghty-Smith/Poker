from card import Card, FullDeck, Hand, PokerHand
from player import Player, Humanoid, Bot

num_of_cards_in_hand = 2

deck = FullDeck()
deck.shuffle()


player1 = Humanoid(1, "Troy", PokerHand())
player2 = Bot(2, "Sam", PokerHand())


for _ in range(0, num_of_cards_in_hand):
    player1.hand.add_holdable(deck.deal_card())
    player2.hand.add_holdable(deck.deal_card())


print(player1)
print(player2)

deck2 = FullDeck()
deck3 = FullDeck()
deck3.shuffle()
deck3.deal_card()

print(deck2.sort_index)
print(deck3.sort_index)
