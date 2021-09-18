from card import Card, FullDeck, Hand, PokerHand
from player import Player, Humanoid, Bot

from texas_holdem_hashtable import suit_dep, not_suit_dep


num_of_cards_in_hand = 2

deck = FullDeck()
deck.shuffle()


player1 = Humanoid(1, "Troy", PokerHand())
player2 = Bot(2, "Sam", PokerHand())


for _ in range(0, num_of_cards_in_hand):
    player1.hand.add_holdable(deck.deal_card())
    player2.hand.add_holdable(deck.deal_card())


com=[]
for _ in range(0, 5):
    com.append(deck.deal_card())



for i in com:
    player1.hand.add_holdable(i)
    player2.hand.add_holdable(i)


print(player1.hand)
print(player2.hand)
if player1.hand.eval_best_hand() == player2.hand.eval_best_hand():
    print('Draw')

elif player1.hand.eval_best_hand() < player2.hand.eval_best_hand():
    print(player1.name + ' wins')

elif player1.hand.eval_best_hand() > player2.hand.eval_best_hand():
    print(player2.name + ' wins')


