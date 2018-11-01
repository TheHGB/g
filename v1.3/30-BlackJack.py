#I did this to play with unicode, if you want to see the cards, zoom
#This shit should splitted into functions, but I will write it as a script just to piss off a roomate

import random

hiddenCard = u"\U0001f0a0"
cards = [u"\U0001f0a1",u"\U0001f0a2",u"\U0001f0a3",u"\U0001f0a4",u"\U0001f0a5",u"\U0001f0a6",u"\U0001f0a7",u"\U0001f0a8",u"\U0001f0a9",u"\U0001f0aA",u"\U0001f0aB",u"\U0001f0aD",u"\U0001f0aE",u"\U0001f0b1",u"\U0001f0b2",u"\U0001f0b3",u"\U0001f0b4",u"\U0001f0b5",u"\U0001f0b6",u"\U0001f0b7",u"\U0001f0b8",u"\U0001f0b9",u"\U0001f0bA",u"\U0001f0bB",u"\U0001f0bD",u"\U0001f0bE",u"\U0001f0c1",u"\U0001f0c2",u"\U0001f0c3",u"\U0001f0c4",u"\U0001f0c5",u"\U0001f0c6",u"\U0001f0c7",u"\U0001f0c8",u"\U0001f0c9",u"\U0001f0cA",u"\U0001f0cB",u"\U0001f0cD",u"\U0001f0cE",u"\U0001f0d1",u"\U0001f0d2",u"\U0001f0d3",u"\U0001f0d4",u"\U0001f0d5",u"\U0001f0d6",u"\U0001f0d7",u"\U0001f0d8",u"\U0001f0d9",u"\U0001f0dA",u"\U0001f0dB",u"\U0001f0dD",u"\U0001f0dE"]

random.shuffle(cards)

dealer = []
player = []
end = False

player.append(cards.pop())
dealer.append(cards.pop())
player.append(cards.pop())
dealer.append(cards.pop())

for card in range(1,len(dealer)):
    print hiddenCard +" "+ dealer[card]

for card in player:
    print (card),

while not end:
    action = raw_input("What do you want to do? Stand(S) or Hit(H)? ")
