import random

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
        player_input = input().lower()

        if player_input == "h":
            draw_card(player_deck, deck)
        elif player_input == "s":
            pass
        elif player_input == "q":
            break
        else:
            print("Invalid input.")

def draw_card(hand, deck):
    hand.append(deck.pop())

def calculate_score(hand):
    score = 0
    for card in hand:
        #ints check
        #letter check
        pass


def print_status(player_deck, dealer_deck):
    print(f"Your hand: {player_deck}")
    print(f"Dealer's hand: {dealer_deck}")


if __name__ == '__main__':
    main()