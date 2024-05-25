import numpy as np

#%% PREPROCESSING
'''def preprocess(data):
    print(f"Before: {data[0]}")
    new_data = np.empty([data.shape[0], 1], dtype=int)
    for i in range(data.shape[0]):
        hand = data[i]
        # Sort in numerical order
        hand.sort()
        # Change format
        #new_hand = np.full((20,), -1, dtype=int)
        new_hand = np.zeros((20,), dtype=int)
        for j in range(len(hand)):
            if hand[j] < 13: # first suit
                new_hand[4*j] = hand[j] + 1
            elif hand[j] < 26: # second suit
                new_hand[4*j + 1] = hand[j] % 13 + 1
            elif hand[j] < 39: # third suit
                new_hand[4*j + 2] = hand[j] % 13 + 1
            else: # fourth suit
                new_hand[4*j + 3] = hand[j] % 13 + 1
        new_data[i] = np.linalg.norm(new_hand)
    print(f"After: {new_data[0]}")
    return new_data'''


def preprocess(data):
    #print(f"Before: {data[0]}")
    
    # Create new array to store data of new shape (20,)
    new_data = np.empty([data.shape[0], 20], dtype=int)
    
    
    for i in range(data.shape[0]):
        hand = data[i]

            
        new_hand = np.zeros((5,4), dtype=int)
          # 2d shape for sorting later
        new_cards = np.zeros((5,), dtype=int)
          # just the nonzero entries for sorting later
          
        
        # Change format of each hand:
            # * use number codes from first suit (except everything + 1
            #   to differentiate from zero entries)
            # * each card is represented by 4 numbers, the only nonzero
            #   number's index corresponds to its suit
        for j in range(len(hand)):
            if hand[j] < 13: # first suit
                new_hand[j][0] = hand[j] + 1
                new_cards[j] = hand[j] + 1
            elif hand[j] < 26: # second suit
                new_hand[j][1] = hand[j] % 13 + 1
                new_cards[j] = hand[j] % 13 + 1
            elif hand[j] < 39: # third suit
                new_hand[j][2] = hand[j] % 13 + 1
                new_cards[j] = hand[j] % 13 + 1
            else: # fourth suit
                new_hand[j][3] = hand[j] % 13 + 1
                new_cards[j] = hand[j] % 13 + 1
        
        
        # Sort in numerical order
        order = new_cards.argsort()
        new_hand = new_hand[order]
        
        # Change to 1d array to better match original data
        new_data[i] = new_hand.flatten()
        
    #print(f"After: {new_data[0]}")
    return new_data
