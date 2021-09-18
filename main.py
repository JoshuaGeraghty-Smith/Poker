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


card1 = Card('Clubs', 'J', False)
card2 = Card('Spades', '2', True)

print(card1.sort_index)
print(card2.sort_index)

