#Joshua Martin CIS261 Week 8 Deck of Cards Lab

import random

# Define the Card class
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

# Define the Deck class
class Deck:
    def __init__(self):
        # Define the ranks and suits
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        self.shuffle()  # Shuffle the deck when it's created

    # Shuffle the deck
    def shuffle(self):
        random.shuffle(self.cards)

    # Deal a single card
    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None  # No cards left

    # Count how many cards are left
    def count(self):
        return len(self.cards)

# Main program logic
def main():
    deck = Deck()  # Create a new deck of cards
    while True:
        print(f"\nCards remaining in deck: {deck.count()}")
        user_input = input("Would you like to draw a card (y/n)? ").lower()

        if user_input == 'y':
            card = deck.deal()
            if card:
                print(f"You drew: {card}")
            else:
                print("No more cards left in the deck.")
        elif user_input == 'n':
            print("Thank you for playing!\n")
            break
        else:
            print("Invalid input, please enter 'y' to draw a card or 'n' to quit.")

# Run the program
if __name__ == "__main__":
    main()
