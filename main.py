from card import Card, Deck, Hand


num_of_cards_in_hand = 2

deck = Deck()
deck.shuffle()


player1 = Hand()
player2 = Hand()

for _ in range(0,num_of_cards_in_hand):
    player1.add_card(deck.deal_card())
    player2.add_card(deck.deal_card())

print(player1)
print(player2)
