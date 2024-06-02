def preprocess(data):
    #print(f"Before: {data[0]}")
    
    # Create new array to store data of new shape (10,)
    new_data = np.empty([data.shape[0], 13], dtype=int)
    
    
    for i in range(data.shape[0]):
        hand = data[i]

            
        new_hand = np.zeros((2,5), dtype=int)
          # 2d shape for easier processing, sorting
        
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
        
        # Sort in numerical order
        order = np.argsort(new_hand[0])
        new_hand = np.concatenate((new_hand[0][order], new_hand[1][order]))
        
        # Record number of unique cards, unique suits
        unique_cards = np.unique(new_hand[:5]).shape[0]
        unique_suits = np.unique(new_hand[5:]).shape[0]
        
        # Record number of repeated cards, repeated suits
        cards, counts = np.unique(new_hand[:5], return_counts=True)
        repeated_cards = cards[counts > 1].shape[0]
        suits, counts = np.unique(new_hand[5:], return_counts=True)
        repeated_suits = suits[counts > 1].shape[0]
        
        # Replace card codes with difference between each two subsequent codes
        for k in range(len(hand) - 1):
            new_hand[k] = new_hand[k+1] - new_hand[k]
        new_hand = np.delete(new_hand, len(hand) - 1)
        
        # Append number of unique cards, unique suits, repeated cards, repeated suits
        new_hand = np.append(new_hand, [unique_cards, unique_suits, repeated_cards, repeated_suits])
        
        # Resize to 1d array
        new_data[i] = new_hand.flatten()
        
    #print(f"After: {new_data[0]}")
    return new_data
