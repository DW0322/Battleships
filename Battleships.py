#battleship board layout. Seperated into lists for appending placement of boats and attacks.
boardShipP1 = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
               "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
               "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
               "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
               "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
               "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
               "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
               "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
               "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
               "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
boardAttackP1 = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
               "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
               "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
               "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
               "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
               "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
               "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
               "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
               "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
               "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]

boardShipP2 = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
               "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
               "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
               "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
               "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
               "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
               "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
               "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
               "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
               "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
boardAttackP2 = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
               "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
               "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
               "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
               "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
               "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
               "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
               "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
               "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", 
               "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]

winner = None
gameRunning = True
currentPlayer = "P1"

#function to print the esablished layout in a more user friendly way. Also declaring the rows and columns.
def print_board(player_number, attack_board, ship_board):
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

print_board(currentPlayer, boardAttackP1, boardShipP1)

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

            
#Function to take user input for the placement of the 5 types of ships. 
def boatPlacement():
    
    boats = {
        "1" : ("V", 5, "Carrier"),
        "2" : ("W", 4, "Battleship"),
        "3" : ("X", 3, "Cruiser"),
        "4" : ("Y", 3, "Submarine"),
        "5" : ("Z", 2, "Destroyer")
    }
    column_values = {"A" : 0, "B" : 1, "C" : 2, "D" : 3, "E" : 4, "F" : 5, "G" : 6, "H" : 7, "I" : 8, "J" : 9}
    row_values = {"1" : 0, "2" : 10, "3" : 20, "4" : 30, "5" : 40, "6" : 50, "7" : 60, "8" : 70, "9" : 80, "10" : 90}

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
                success, message = boardShipPlacement(size, boardShipP1, cell_selected, boat_symbol, direction)
                if success:
                    print_board(currentPlayer, boardAttackP1, boardShipP1)
                    break
                else:
                    print(message)
            else:
                print("Invalid direction. Please enter a direction using WASD keys.")
        

boatPlacement()

    #placement direction horizontal left, vertically up, etc...
    #make sure the space on the board is empty
    #make sure the size fits the placement area
#battle ship placement round player 2
    #placement direction horizontal left, vertically up, etc...
    #make sure the space on the board is empty
    #make sure the size fits the placement area

#battle ship attack round player 1
    #detect hit or miss
    #update attack board
#battle ship attack round player 2
    #detect hit or miss
    #update attack board
