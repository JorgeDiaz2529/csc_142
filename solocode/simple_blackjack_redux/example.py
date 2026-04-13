#IGNORE THIS

# Simple Blackjack for CSI 380 by David Kopec
# This program plays a simple, single suit game of Blackjack
# against a computer dealer.
import random
import sys
import pygame
import pygwidgets

# Move a card from deck to hand
def draw_card(hand: list[str], deck: list[str]) -> None:
    hand.append(deck.pop()) # take last card from deck

# calculate the score of the hand
def calculate_score(hand: list[str]) -> int:
    score = 0
    has_ace = False

    for card in hand:
        try:
            ival = int(card)
            score += ival
        except ValueError:
            # not a number card
            if card == "A": # ace
                has_ace = True
        else: # face card
            score += 10
        
    if has_ace:
        # treat ace as 11 if it doesn't bust, otherwise 1
        if (score + 11) > 21:
            score += 1
        else:
            score += 11
    return score

# Print everyone's scores and hands
def print_status(player_cards: list[str], dealer_cards: list[str]) -> None:
    print(f"Player's total is {calculate_score(player_cards)}")
    print(player_cards)
    
    print(f"Dealer's total is {calculate_score(dealer_cards)}")
    print(dealer_cards)

def main() -> None:
    deck: list[str] = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K",
    "A"]
    player_cards: list[str] = []
    dealer_cards: list[str] = []

    # shuffle the deck
    random.shuffle(deck)

    print("Dealer draws first card")
    draw_card(dealer_cards, deck)
    print("Player receives two cards")
    draw_card(player_cards, deck)
    draw_card(player_cards, deck)

    print_status(player_cards, dealer_cards)

    # player decision loop
    while True:
        choice = input("Do you want to (H)it, (S)tay, or (Q)uit?\n").strip().upper()
        
        if choice == "H": # hit
            draw_card(player_cards, deck)
            print_status(player_cards, dealer_cards)

        if calculate_score(player_cards) > 21:
            print("You busted! you lose!")
            sys.exit(0)

        elif choice == "S": # stay
            break

        elif choice == "Q": # quit
            sys.exit(0)

    # if they type something else, just reprompt (matches Go behavior of doingnothing)
    print("Dealer draws rest of cards.")

    # keep drawing cards until 17 score or greater
    while calculate_score(dealer_cards) < 17:
        draw_card(dealer_cards, deck)
        print_status(player_cards, dealer_cards)
    if calculate_score(dealer_cards) > 21:
        print("Dealer busts! You win!")
    elif calculate_score(dealer_cards) > calculate_score(player_cards):
        print("Dealer wins!")
    elif calculate_score(dealer_cards) < calculate_score(player_cards):
        print("You win!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
