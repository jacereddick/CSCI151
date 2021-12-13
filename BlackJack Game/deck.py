#Function to create deck
import random
from card import Card

class Deck:
#Initializing global variables
    def __init__(self):
        self.deck = []
        self.create()


#Test function to print all cards in the deck
    def print_deck(self):
        for i in range(len(self.deck)):
            print(str(self.deck[i]))

#Test to see that a card is being taken away
    def deck_size(self):
        return len(self.deck)

    
#Creates the full deck
    def create(self):
        self.deck = []
        for i in range(1,14):
            for j in range(1,5):
                card = Card(j, i)
                self.deck.append(card)
        self.shuffle()


#Keeps cards dealt until they hit 0 (This should rarely to never happen)
    def deal(self):
        if self.deck_size() > 0:
            return self.deck.pop()
        else:
            return "No cards left!"

        if self.deck_size() < 20:
            self.create()

#Shuffle the deck to a new order
    def shuffle(self):
        random.shuffle(self.deck)
