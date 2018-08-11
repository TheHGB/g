import random
import re

#There is no purpose in putting all the "sprites" on a list other than to uncessarly overcomplicate things.
list_of_hangmen =[[''],["________","|           ","|            ","|         ", "|          ","|             "], ["________","|      |      ","|            ","|          ", "|        ","|             "],["________","|      |      ","|      0      ","|         ", "|          ","|             "],["________","|      |      ","|      0      ","|      |     ", "|           ","|             "],["________","|      |      ","|      0      ","|     /|     ", "|          ","|             "],["________","|      |      ","|      0      ","|     /|\     ", "|          ","|             "],["________","|      |      ","|      0      ","|     /|\     ", "|     /      ","|             "],["________","|      |      ","|      0      ","|     /|\     ", "|     / \     ","|             "]]


def drawHangman(hangman):
    for string in hangman:
        print string

def selectWord():
    word = random.choice(list(open('words.txt')))
    return word.rstrip()

def game(word):
    mistery = []
    errors = 0
    for char in word:
        mistery.append("_ ")

    while errors <  len(list_of_hangmen): 
        drawHangman(list_of_hangmen[errors])
        print "".join(mistery)
        meh = raw_input("\nChoose a letter\n")
        positions = [x.start() for x in re.finditer(meh, word)]
        if meh and positions and meh + " " not in mistery:
            for position in positions:
                mistery[position] = meh + " "
        else:
            errors += 1


if __name__ == "__main__":
    
    game(selectWord())





