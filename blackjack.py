import setup

while True:

    # Print an opening statement
    print('WELCOME TO BLACKJACK')

    #Create & shuffle the deck, deal two cards to each player
    deck = setup.Deck()
    deck.shuffle()

    player_hand = setup.Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = setup.Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Setup the Player's chips
    player_chips = setup.Chips()
    
    # Prompt the Player for their bet
    setup.take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    setup.show_some(player_hand, dealer_hand)

    while setup.playing: # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        setup.hit_or_stand(deck, player_hand)

        # Show cards (but keep one dealer card hidden)
        setup.show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21, run player_bust() and break out of loop
        if player_hand.value > 21:
            setup.player_busts(player_hand,dealer_hand,player_chips)

            break

    # If the Player hasn't busted, Play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            setup.hit(deck, dealer_hand)

        # Show all Cards
        setup.show_all(player_hand, dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value >21:
            setup.dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            setup.dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            setup.player_wins(player_hand, dealer_hand, player_chips)
        else:
            setup.push(player_hand, dealer_hand)

    # Inform Player of their chips total
    print('\n Player total chips are at: {}'.format(player_chips.total))

    # Ask to play again
    new_game = input("Would you like to play another hand? y/n: ")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Thank you for playing!')

        break