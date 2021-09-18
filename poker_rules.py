#class deal_cards(player IDs and thus number of players)

    #function starter_chips(player IDs):
        #allocates starter chips to each player
        #returns dictionary of player IDs with starter chips

    #function assign initial cards to each player(player IDs):
        #remove delt cards from deck each time 1 is dealt
        #return dictionary of player IDs with assigned cards
        
    #function community_cards()
        #anti request
        #river
        #bet option
        #card
        #bet option
        #card
        #bet option
        #com_cards
        
    #function player_possibilities(dictionary of player IDs with cards, com_cards):
        #creates best hands for each player
        #compares hands to find winner using 
        #returns nested list dictionary of possible hands for each player
        
    #function winner(list of hands):
        #takes the list of hands and finds the winning hand
        #contingency for drawing, just return winnig hand will be handled
        #returns winning hand
    
    #End winner(nested list dictionary of possible hands for each player):
        #runs through winner function to find each players best hand
        #runs through winner to find best hand
        #matches hand with player/s if draw
        #returns winning player
        
    #need to somehow allocate pot to winning player/s chip pot in the chip dictionary


#class bets
        
    #function anti requests:
        #pass comment will send request to player for initial chips
        #alters 
        
    #function bet:
        #option will also be pass treat as assumed check
        
    #pot collector:
        #allocates chips to pot
        #removes chips from player chip dictionary
        #side pot contingency 