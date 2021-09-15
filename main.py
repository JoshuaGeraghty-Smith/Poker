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



com=[Card('Clubs', '7', False),
Card('Spades', '8', True),
Card('Hearts', 'K', False),
Card('Spades', 'A', False),
Card('Diamonds', '4', False)]



print(player1)
player1.hand.is_suited(com)

