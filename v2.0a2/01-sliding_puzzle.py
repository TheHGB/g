# Used magic numbers. If this were to be scalable, the hardcoded modules and indexes would have to become variables

import sys,tty,termios,os
import random

# Code shamelessly copied from StackOverflow to read the arrow keys
def getKey():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(3)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

# Generate the puzzle and shuffle it
puzzle = [str(i) for i in range(1,10)]
puzzle = puzzle + ['A','B','C','D','E','F']
puzzle.append('_')
solution = puzzle.copy()
random.shuffle(puzzle)

# play until the puzzle is ordered
while puzzle != solution:
    # Clear the screen on each turn
    os.system('clear')
    # Print the puzzle list in fragments of 4
    for i in range(int(len(puzzle)/4)):
        print(puzzle[4*i:4*i+4])
    
    direction = getKey()
    print (direction)

    # UP
    if direction == '\x1b[A':
        sliding = puzzle.index('_')
        if sliding - 4 in range(16):
            puzzle[sliding-4],puzzle[sliding]=puzzle[sliding],puzzle[sliding-4]
    # LEFT
    elif direction == '\x1b[D':
        sliding = puzzle.index('_')
        if sliding%4 !=0:
            puzzle[sliding-1],puzzle[sliding]=puzzle[sliding],puzzle[sliding-1]
    # DOWN
    elif direction == '\x1b[B':
        sliding = puzzle.index('_')
        if sliding + 4 in range(16):
            puzzle[sliding+4],puzzle[sliding]=puzzle[sliding],puzzle[sliding+4]
    #Right
    elif direction == '\x1b[C':
        sliding = puzzle.index('_')
        if sliding%4 !=3:
            puzzle[sliding+1],puzzle[sliding]=puzzle[sliding],puzzle[sliding+1]

    #Exit. Due to the shamelessly copied code, most keys must be pressed 3 times to register 
    elif direction == '\x1b\x1b\x1b':
        exit(0)

    else:
        print('Use the arrow keys to move or Esc 3 times to exit')
        exit(0)

os.system('clear')
for i in range(int(len(puzzle)/4)):
    print(puzzle[4*i:4*i+4])

print ("\nCongratulations, you have solved the puzzle")
