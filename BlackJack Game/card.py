#Create each card
import random


class Card:

#Initlialize variables and create the suits and card types(faces and values)
    def __init__(self, suit, face):
        self.cardTypes = {
            1:["Ace", 1],
            2:["Two", 2],
            3:["Three", 3],
            4:["Four", 4],
            5:["Five", 5],
            6:["Six", 6],
            7:["Seven", 7],
            8:["Eight", 8],
            9:["Nine", 9],
            10:["Ten", 10],
            11:["Jack", 10],
            12:["Queen", 10],
            13:["King", 10]
        }
        self.suitTypes = {
            1:"Spade",
            2:"Hearts",
            3:"Diamonds",
            4:"Clubs"
        }
        self.suit = self.suitTypes[suit]
        self.face = self.cardTypes[face][0]
        self.value = self.cardTypes[face][1]

#setting a value
    def get_value(self):
        return self.value

#Finds the value in the dictionary made above to set a cards value      
    def set_value(self,i):
        self.value = i
        
#Print out the Face, and suit nicely
    def __str__(self):
        return self.face + " of " + self.suit
