#Class to create the Player 

class Player:
#Initialize Variables
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.hand = []

#Creating Array from players cards
    def print_hand(self):
        print(self.name)
        for i in range(len(self.hand)):
            print(str(self.hand[i]))
        print()


#printing the array's first value
    def print_first(self):
        print(str(self.hand[0]))


#Clear the Players Hand
    def clear(self):
        self.hand = []

#Adding new card to the hand
    def deal_card(self, newcard):
        self.hand.append(newcard)

#Printing Users Balance
    def print_balance(self):
        print("Balance: $" + str(self.balance))

#Calculate balance after transaction
    def get_balance(self):
        return self.balance

#Determines if the balance is greater than 0 and is allowed to bet amount
    def bet(self, i):
        if(self.balance-i >= 0):
            self.balance -= i
            return True
        else:
            return False

#Adds amount to balance if hand is one
    def win(self, i):
        self.balance += i

#Calculates if an ace is found and needs to be measured as 11 for more success
#or if 1 is needed to not put the hand over 21
    def hand_value(self):
        total = 0
        hasAce = False
        for i in range(len(self.hand)):
            if self.hand[i].face == "Ace":
                hasAce = True
            total += self.hand[i].get_value()

        if hasAce and total + 10 <= 21:
            total += 10
        
        return total

#Seeing if a hand is equal to exactly 21
    def blackjack(self):
        if self.hand_value() == 21:
            return True
        else:
            return False

#Seeing if we go over 21, therefore meaning we lose right away
    def bust(self):
        if self.hand_value() > 21:
            return True
        else:
            return False


    
