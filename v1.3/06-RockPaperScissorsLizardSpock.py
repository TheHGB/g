#Scissors cuts paper, paper covers rock, rock crushes lizard, 
#lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard, 
#lizard eats paper, paper disproves Spock, Spock vaporizes rock, 
#and as it always has, rock crushes scissors

import random
import time
import sys

play = ""


moves = ['ROCK', 'PAPER', 'SCISSORS', 'LIZARD', 'SPOCK']

while play.lower() != "no":
    print "Ready?"
    sys.stdout.flush()
    time.sleep(0.7)
    print "1",
    sys.stdout.flush()
    time.sleep(0.5)
    print "2",
    sys.stdout.flush()
    time.sleep(0.5)
    print "3",
    sys.stdout.flush()
    time.sleep(0.5)
    print "rockpaperscissorslizardspock"
    sys.stdout.flush()
    time.sleep(1.5)

    print moves[random.randint(0,4)]
    
    play = raw_input("Do you want to play another round?\n")
