def preprocess(data):
    
    # Create new array to store data of new shape (10,)
    new_data = np.empty([data.shape[0], 4], dtype=int)
    
    # For each poker hand in data
    for i in range(data.shape[0]):
        hand = data[i]
        
        # Create 2d array for easier use 
        new_hand = np.zeros((2,5), dtype=int)
        
        # Change format of each hand:
            # new_hand[0]: hand using number codes from first suit
            # new_hand[1]: number corresponding to each card's suit
        for j in range(len(hand)):
            if hand[j] < 13: # first suit
                suit = 1
            elif hand[j] < 26: # second suit
                suit = 2
            elif hand[j] < 39: # third suit
                suit = 3
            else: # fourth suit
                suit = 4
            
            new_hand[0, j] = hand[j] % 13
            new_hand[1, j] = suit
        
        # Record number of unique cards, unique suits
        unique_cards = np.unique(new_hand[0]).shape[0]
        unique_suits = np.unique(new_hand[1]).shape[0]
        
        # Record number of repeated cards, repeated suits
        cards, counts = np.unique(new_hand[0], return_counts=True)
        repeated_cards = cards[counts > 1].shape[0]
        suits, counts = np.unique(new_hand[1], return_counts=True)
        repeated_suits = suits[counts > 1].shape[0]
        
        # Final data comes from these counts/ numbers
        new_data[i] = np.array([unique_cards, unique_suits, repeated_cards, repeated_suits])
        
    return new_data
