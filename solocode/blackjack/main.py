import random
import sys #annoying to press q all the time
import time

debug = False

def main():
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    player_deck = []
    dealer_deck = []

    random.shuffle(deck)
    draw_card(dealer_deck, deck)
    draw_card(player_deck, deck)
    draw_card(player_deck, deck)
    print_status(player_deck, dealer_deck)

    #gameplay loop
    while True:
        
        print("Type [H] to hit, [S] to stay, and [Q] to quit: ")
        player_input = input()
        player_input = player_input.lower()

        #player's turn
        if player_input == "h":
            draw_card(player_deck, deck)
        elif player_input == "s":
            print("stay")
        elif player_input == "q":
            sys.exit()
        
        if calculate_score(player_deck) > 21:
            print("Calculating...")
            time.sleep(2)

            print("You bust")
            sys.exit()

        #dealer's turn
        draw_card(dealer_deck, deck)

        print_status(player_deck, dealer_deck)

        if calculate_score(dealer_deck) >= 17:
            if calculate_score(dealer_deck) > 21:
                print("Calculating...")
                time.sleep(2)
                
                print("The dealer busts")
                sys.exit()
            else: #neither bust
                print("Calculating...")
                time.sleep(2)

                if calculate_score(dealer_deck) > calculate_score(player_deck):
                    print("The dealer's score is higher!\n Dealer wins")
                    sys.exit()
                else: # player score is higher
                    print("Your score is higher!\n You win")
                    sys.exit()

                # code if both end up tying
                print("It's a tie!")
                sys.exit()
        

def draw_card(hand: list, deck: list):
    hand.append(deck.pop())

def calculate_score(hand: list):
    score = 0
    for card in hand:
        card_type = check_string_type(card)

        if card_type == "Letter":
            if card == "J" or card == "Q" or card == "K":
                score += 10
                continue
            if card == "A":
                score += 11^random.randint(0,1) #returns either 1 or 11 
                continue

        if card_type == "Integer":
            score += int(card)
            continue
        
    return score

#had to look this one up online
def check_string_type(s: str):
    if s.isalpha():
        return "Letter"
    try:
        int(s)
        return "Integer"
    except ValueError:
        return "Neither"

def print_status(player_deck: list, dealer_deck: list):
    print(f"Your hand: {player_deck}")
    print(f"Score: {calculate_score(player_deck)}")
    
    if debug == False:
        print(f"Dealer's hand: {dealer_deck[0]}...") # only shows the first card
        print(f"Dealer's Score: {calculate_score(dealer_deck)}")
    else:
        print(f"Dealer's hand: {dealer_deck}") # shows everything
        print(f"Dealer's Score: {calculate_score(dealer_deck)}")
    

if __name__ == '__main__':
    main()