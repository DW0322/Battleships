import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

#P1 battleship boards
def initialise_board():
    return ["-"] * 100
boardShipP1 = initialise_board()
boardAttackP1 = initialise_board()

#P2 battleship boards
boardShipP2 = initialise_board()
boardAttackP2 = initialise_board()


winner = False
gameRunning = True
currentPlayer = "P1"

#Assigns the currnet board to the current player
def switch_player(currentPlayer, boardShipP1, boardAttackP1, boardShipP2, boardAttackP2):
    if currentPlayer == "P1":
        return boardShipP1, boardAttackP1
    elif currentPlayer == "P2":
        return boardShipP2, boardAttackP2

#Determine who's turn it is
def playerTurnChange(player):
    global currentPlayer
    if player == "P1":
        currentPlayer = "P2"
    else:
        currentPlayer = "P1"


#function to print the esablished layout in a more user friendly way. Also declaring the rows and columns.
def print_board(attack_board, ship_board):
    print("                 ATTACK BOARD")
    print("    ", "A ", " B ", " C ", " D ", " E ", " F ", " G ", " H ", " I ", " J ")
    for i in range(10):
        print("{:2d}".format(i + 1), end=" |")
        for j in range(10):
            print(" " + attack_board[i * 10 + j] + " |", end="")
        print()

    print("                 SHIP BOARD")
    print("    ", "A ", " B ", " C ", " D ", " E ", " F ", " G ", " H ", " I ", " J ")
    for i in range(10):
        print("{:2d}".format(i + 1), end=" |")
        for j in range(10):
            print(" " + ship_board[i * 10 + j] + " |", end="")
        print()

# print the current players board
def printCurrentPlayerBoard(currentPlayer):
    if currentPlayer == "P1":
        print_board(boardAttackP1, boardShipP1)
    else:
        print_board(boardAttackP2, boardShipP2)


#Fucniton checks if you've already selected that boat and if the are you are selecting has enough space for the ship.
def boardShipPlacement(size, ship_board, cell_selected, boat_symbol, direction):
    directions = {
        "W": (-1, 0),  # Up
        "A": (0, -1),  # Left
        "S": (1, 0),   # Down
        "D": (0, 1)    # Right
    }

    num_columns = 10
    num_rows = 10

    if direction in directions:
        row_step, col_step = directions[direction]
        indexes_to_check = [cell_selected]

        for i in range(1, size):
            next_row = (cell_selected // num_columns) + (row_step * i)
            next_col = (cell_selected % num_columns) + (col_step * i)
            next_index = next_row * num_columns + next_col

            # Check if the next index is within the grid boundaries
            if 0 <= next_row < num_rows and 0 <= next_col < num_columns:
                indexes_to_check.append(next_index)
            else:
                return False, "Ship placement out of bounds"

        # Check if all subsequent indexes are available
        if all(ship_board[index] == "-" for index in indexes_to_check):
            # Place the ship on the board
            for index in indexes_to_check:
                ship_board[index] = boat_symbol
            return True, "Ship placed successfully"
        else:
            return False, "Some cells are already occupied"
    else:
        return False, "Invalid direction"

#Standard values for columns and rows in the baords
column_values = {"A" : 0, "B" : 1, "C" : 2, "D" : 3, "E" : 4, "F" : 5, "G" : 6, "H" : 7, "I" : 8, "J" : 9}
row_values = {"1" : 0, "2" : 10, "3" : 20, "4" : 30, "5" : 40, "6" : 50, "7" : 60, "8" : 70, "9" : 80, "10" : 90} 

#Function to take user input for the placement of the 5 types of ships. 
def boatPlacement():
    global currentPlayer
    boats = {
        "1" : ("V", 5, "Carrier")
    }

    boatsText = {key: f"{key}- {value[2]} - {value[1]} Spaces" for key, value in boats.items()}
    remaining_boats = set(boats.keys())

    selected_boats = []
 
    while remaining_boats:
        for boat_id, boat_text in boatsText.items():
            if boat_id in remaining_boats:
                print(boat_text)

        boat = input("Pick the number boat you would like to place: ")

        if boat in remaining_boats:
            boat_symbol = boats[boat][0]
            size = boats[boat][1]
            selected_boats.append((boat_symbol, size))
            remaining_boats.remove(boat)
        else:
            print("Invalid choice. Please pick a boat from the list.")
            continue
        
        placement = []

        column = set(column_values.keys())
        row = set(row_values.keys())
        
        
        while True:
            
            while True:
                placement_column = (input(f"What column (A - J) would you like to place your {boats[boat][2]} of size {size}? ")).upper()
                if placement_column in column:
                    placement.append(placement_column)
                    break
                else:
                    print("Invalid column. Please enter a column from A to J.")
                    continue

            while True:
                placement_row = (input(f"What row (1 - 10) would you like to place your {boats[boat][2]} of size {size}? ")).upper()
                if placement_row in row:
                    placement.append(placement_row)
                    break
                else:
                    print("Invalid row. Please enter a row from 1 to 10.")
                    continue
            break
    
        
        column_selected = column_values[placement[0]]
        row_selected = row_values[placement[1]]
        cell_selected = column_selected + row_selected

        available_directions = ["W", "A", "S", "D"]
        while True:
            direction = (input("Using the WASD keys, select your desired direction: ")).upper()
            if direction in available_directions:
                ship_board, attack_board = switch_player(currentPlayer, boardShipP1, boardAttackP1, boardShipP2, boardAttackP2)
                success, message = boardShipPlacement(size, ship_board, cell_selected, boat_symbol, direction)
                if success:
                    printCurrentPlayerBoard(currentPlayer)
                    break
                else:
                    print(message)
            else:
                print("Invalid direction. Please enter a direction using WASD keys.")

#Check the board for the total amount of hits necessary to win
def detectWinner():
    global winner
    global gameRunning
    global currentPlayer
    global boardAttackP1
    global boardAttackP2
    if currentPlayer == "P1":
        hit = 0
        for i in boardAttackP1:
            if i == "#":
                hit += 1
                if hit == 17:
                    winner = "P1"   
                    gameRunning = False
                    print(f"The winner is... {winner}!!")
                    return gameRunning
    elif currentPlayer == "P2":
        hit = 0
        for i in boardAttackP2:
            if i == "#":
                hit += 1
                if hit == 17:
                    winner = "P2"   
                    gameRunning = False
                    print(f"The winner is... {winner}!!")
                    return gameRunning

#checks the board to see if your shot is a hit or miss
def shotCheck(currentAttackBoard, enemyShipBoard):
    global currentPlayer
    global gameRunning
    column = set(column_values.keys())
    row = set(row_values.keys())

    while gameRunning == True:
        placement = []  # Initialize placement list within the loop
        placement_column = input("What column (A - J) would you like to place your shot? ").upper()
        if placement_column in column:
            placement.append(placement_column)
        else:
            print("Invalid column. Please enter a column from A to J.")
            continue

        placement_row = input("What row (1 - 10) would you like to place your shot? ").upper()
        if placement_row in row:
            placement.append(placement_row)
        else:
            print("Invalid row. Please enter a row from 1 to 10.")
            continue
        
        column_selected = column_values[placement[0]]
        row_selected = row_values[placement[1]]
        cell_selected = column_selected + row_selected

        if currentAttackBoard[cell_selected] == "-":
            if enemyShipBoard[cell_selected] == "-":
                clear_terminal()
                print("You missed! Next players turn.")
                currentAttackBoard[cell_selected] = "O"  # Update attack board with miss symbol
                break
            else:
                print("It's a hit! Your turn again.")
                currentAttackBoard[cell_selected] = "#"  # Update attack board with hit symbol
                enemyShipBoard[cell_selected] = "#"  # Update enemy ship board with hit symbol
                printCurrentPlayerBoard(currentPlayer)
                detectWinner()
                continue
        else:
            print("You already shot here! Please select another cell.")
            continue
    

#shot placemnt decision
def shotPlacement():
    global currentPlayer
    if currentPlayer == "P1":
        shotCheck(boardAttackP1, boardShipP2) 
    else:
        shotCheck(boardAttackP2, boardShipP1)
    playerTurnChange(currentPlayer)

#funcitons to make the boat placement round
def placementRound():
    global currentPlayer
    loop = 0
    while loop != 2:
        switch_player(currentPlayer, boardShipP1, boardAttackP1, boardShipP2, boardAttackP2)
        printCurrentPlayerBoard(currentPlayer)
        boatPlacement()
        currentPlayer = "P2" if currentPlayer == "P1" else "P1"
        loop += 1
        clear_terminal()
    clear_terminal()

#functions to make the attack round
def attackRound():
    global currentPlayer
    global gameRunning
    while gameRunning is True:
        shotPlacement()
        detectWinner()
    

#general function using the two rounds, placement and attack.
def battleshipGame():
    placementRound()
    attackRound()

#exectue game
battleshipGame()
