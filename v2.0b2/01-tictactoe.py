# The 'AI' is extremly inefitient, but meh
# Spaghetti code and copy-pasting are underrated 
# I might clean the code eventually

import random

# Print the board, with the symbols of each player
def print_board(values):
    print("\n")
    print("     |     |")
    print("  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print("_____|_____|_____")

    print("     |     |")
    print("  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print("_____|_____|_____")

    print("     |     |")

    print("  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("     |     |")
    print("\n")

# AI that controls the machine's playes. It is sort of designed to try and deny playes from the other player with an element of randomness. So it will have more sucess than one choosing the position at random, but it will not be perfect
def IA(player, rival, values, player_sign):
    # If the board is empty, place a symbol randomly
    if not rival:
        pos = random.randint(1,9)
        player.append(pos)
        values[pos-1] = player_sign
    # If the board is not empty but each player has less than tree symbols on the board, try to guess which positions would grant the rival the victory from the positions already taken and choose one of those at random.
    elif len(rival) < 3 and len(player) < 3:
        elegible_lists = [option for option in winning_list if set(rival).issubset(option)]
        # The rival cannot win
        if not elegible_lists:
            pos = random.choice([i for i in range(1,10) if i not in rival+player ])
        # The rival can still win
        else:
            # Inizalize the pos so the following while works (its late and I don't want to rethink)
            if player:
                pos = player[0]
            else:
                pos = rival[0]
            # Chose a postition from the possible winning combinations for the rival at random
            i = 0
            while (pos in player) or (pos in rival):
                chosen_target = random.choice(elegible_lists)
                pos = random.choice(chosen_target)
                i = i+1
                # Prevent getting stuck in the loop. If that happens, choose at random
                if i == 1000:
                     pos = random.choice([i for i in range(1,10) if i not in rival+player])
                     break
        player.append(pos)
        values[pos-1] = player_sign
    # If one of the players already has 3 symbols on the board, the check is inverted. Now it looks if any of the winning combinations can be achieved from the symbols already on the board
    else:
        # Get the empty spaces on the board
        elegible_positions = [i+1 for i,j in enumerate(values) if j == ' ']
        pos = None
        # For each empty position, add the position to the current positions of the rival's symbols and check if a winning combination would form part of that
        for position in elegible_positions:
            if pos:
                break
            for option in winning_list:
                temp = option + [position]
                if pos:
                    break
                if set(rival).issubset(temp):
                    pos = position
        # If the rival cannot win, choose at random
        if not pos:
            pos = random.choice(elegible_positions)
        player.append(pos)
        values[pos-1]=player_sign

    return player, values



print_board([i for i in range(1,10)])

# List with all winning combinations
winning_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

players = input("How many players?: ")

# Two machine players fight each other
if players == '0':
    print("No players")
    X = []
    O = []
    winner = None
    values = [' ' for i in range(9)]
    turn = random.choice([True,False])
    # Keep playing while there is still space on the board and no winner has been declared
    while (len(X) + len(O)) != 9 and not winner:
        if turn:
            print("X's turn")
            X, values = IA(X,O,values,'X')
            X.sort()
            # Check if the player has a winning combination or a winning combination is within the players' positions
            if X in winning_list:
                winner = 'X'
            else:
                for combination in winning_list:
                    if set(combination).issubset(X):
                        winner = 'X'
        # Copy-pasted code for the other machine player
        else:
            print("O's turn")
            O, values = IA(O,X,values,'O')
            O.sort()
            if O in winning_list:
                winner = 'O'
            else:
                for combination in winning_list:
                    if set(combination).issubset(O):
                        winner = 'O'
        print_board(values)
        if winner:
            print("Congratulations {}. You win".format(winner))
        else:
            turn = not turn
    if not winner:
        print("Draw")

elif players is '1':
    print("One player")
    player_table = []
    machine_table = []
    winner = None
    values = [' ' for i in range(9)]
    turn = random.choice([True,False])
    
    player_symbol = input('What do you want to be?[X/O]: ')
    while player_symbol != 'X' and player_symbol != 'O':
        player_symbol = input('The options are X or O: ')
    
    if player_symbol == 'X':
        machine_symbol = 'O'
    else:
        machine_symbol = 'X'

    while (len(player_table) + len(machine_table)) != 9 and not winner:
        if turn:
            pos = int(input('Its your turn, where do you want to write? [1-9]: '))
            while pos in player_table + machine_table:
                pos = int(input("This position is already taken, pick another [1-9]: "))
            player_table.append(pos)
            values[pos-1] = player_symbol
            player_table.sort()
            if player_table in winning_list:
                winner = player_symbol
            else:
                for combination in winning_list:
                    if set(combination).issubset(player_table):
                        winner = player_symbol
        # Copy pasted code from the 0 players option
        else:
            print("Machine's trun")
            machine_table, values = IA(machine_table,player_table,values,machine_symbol)
            machine_table.sort()
            if machine_table in winning_list:
                winner = machine_symbol
            else:
                for combination in winning_list:
                    if set(combination).issubset(machine_table):
                        winner = machine_symbol
        print_board(values)
        if winner:
            print("Congratulations {}. You win".format(winner))
        else:
            turn = not turn
    if not winner:
        print("Draw")

# Pasting the copied code from the player part of the 1 player option twice
elif players is '2':
    print("Two players")
    player_1 = []
    player_2 = []
    winner = None
    values = [' ' for i in range(9)]
    turn = random.choice([True,False])
    
    player_1_symbol = input('What do you want to be, player 1?[X/O]: ')
    while player_1_symbol != 'X' and player_1_symbol != 'O':
        player_1_symbol = input('The options are X or O: ')
    
    if player_1_symbol == 'X':
        player_2_symbol = 'O'
    else:
        player_2_symbol = 'X'

    while (len(player_1) + len(player_2)) != 9 and not winner:
        if turn:
            pos = int(input("Its player_1's, where do you want to write? [1-9]: "))
            while pos in player_1 + player_2:
                pos = int(input("This position is already taken, pick another [1-9]: "))
            player_1.append(pos)
            values[pos-1] = player_1_symbol
            player_1.sort()
            if player_1 in winning_list:
                winner = player_1_symbol
            else:
                for combination in winning_list:
                    if set(combination).issubset(player_1):
                        winner = player_1_symbol
        else:
            pos = int(input("Its player_2's, where do you want to write? [1-9]: "))
            while pos in player_1 + player_2:
                pos = int(input("This position is already taken, pick another [1-9]: "))
            player_2.append(pos)
            values[pos-1] = player_2_symbol
            player_2.sort()
            if player_2 in winning_list:
                winner = player_2_symbol
            else:
                for combination in winning_list:
                    if set(combination).issubset(player_2):
                        winner = player_2_symbol
        print_board(values)
        if winner:
            print("Congratulations {}. You win".format(winner))
        else:
            turn = not turn
    if not winner:
        print("Draw")
else:
    print("Invalid number of players. Only 0, 1 or 2.")
    players = input("How many players): ")

