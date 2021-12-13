#The game 

from card import Card
from deck import Deck
from player import Player
import random


#setting up our local variables
deck = Deck()
player = Player("Player 1", 1200)
dealer = Player("Dealer", 9999999999)

#Gets the player's balance and stores the bet requested for by the player
while(player.get_balance() > 0 and deck.deck_size() > 0):
    player.print_balance()
    betamount = float(input("Enter your bet: "))
    print()
#Finds what the bet ammount is and deals cards to dealer and player
    if(player.bet(betamount)):
        player.deal_card(deck.deal())
        dealer.deal_card(deck.deal())
        player.deal_card(deck.deal())
        dealer.deal_card(deck.deal())
        dealer.print_hand()
        player.print_hand()


#Scenarios of what combinations could happen to win, lose, or draw
        if (player.blackjack()):
            print("Player wins by natural blackjack. Player wins $",betamount * 1.5)
            player.win(betamount + betamount*1.5)
        else:
            while(not player.blackjack() and not player.bust()):
                choice = input("Hit or Stand: ")
                if(choice == "Hit" or choice == "hit"):
                    player.deal_card(deck.deal())
                    player.print_hand()
                else:
                    print()
                    break
            
            while(not player.bust() and not dealer.blackjack() and not dealer.bust() and dealer.hand_value() < 17):
                print("Dealer chooses hit")
                dealer.deal_card(deck.deal())
                dealer.print_hand()

            if(player.bust()):
                print("Player 1 busted. Player 1 lost $" + str(betamount))
            elif(dealer.hand_value() == player.hand_value()):
                print("Tie")
                player.win(betamount)
            elif(dealer.bust() or player.blackjack() or player.hand_value() > dealer.hand_value()):
                print(str(player.hand_value()) + " vs " + str(dealer.hand_value()) +". Player 1 wins $" + str(betamount))
                player.win(betamount * 2)
            else:
                print(str(player.hand_value()) + " vs " + str(dealer.hand_value()) + ". Dealer wins. Player 1 lost $" + str(betamount))

        player.clear()
        dealer.clear()
                
#Lets the player know they have bet too much money      
    else:
        print("Not enough money\n")

#Player has ran out of money and can no longer play
print("You have ran out of money.")

