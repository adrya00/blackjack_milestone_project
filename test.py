import setup

new_deck = setup.Deck()
new_deck.shuffle()

# Player
test_player = setup.Hand()

#Deal 1 car from deck Card(suit,rank)
pulled_card = new_deck.deal()
print(pulled_card)
test_player.add_card(pulled_card)
print(test_player.value)

test_player.add_card(new_deck.deal())
print(test_player.value)

