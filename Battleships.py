#battle-ship board design
#two board for each player
#one to place the ships, one to shoot the ships
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

#define board print functions
def print_board(player_number, attack_board, ship_board):
    print("                 ATTACK BOARD")
    print("   ", "A ", " B ", " C ", " D ", " E ", " F ", " G ", " H ", " I ", " J ")
    for i in range(10):
        print("{:2d}".format(i + 1), end=" |")
        for j in range(10):
            print(" " + attack_board[i * 10 + j] + " |", end="")
        print()

    print("                 SHIP BOARD")
    print("   ", "A ", " B ", " C ", " D ", " E ", " F ", " G ", " H ", " I ", " J ")
    for i in range(10):
        print("{:2d}".format(i + 1), end=" |")
        for j in range(10):
            print(" " + ship_board[i * 10 + j] + " |", end="")
        print()
#battle ship design for vertical and horizontal placement
#battle ship placement round player 1

print_board(currentPlayer, boardShipP1, boardAttackP1)

def boatPlacement():
    
    boats = {
        "1" : ("V", 5, "Carrier"),
        "2" : ("W", 4, "Battleship"),
        "3" : ("X", 3, "Cruiser"),
        "4" : ("Y", 3, "Submarine"),
        "5" : ("Z", 2, "Destroyer")
    }
    column_values = {"A" : 0, "B" : 1, "C" : 2, "D" : 3, "E" : 4, "F" : 5, "G" : 6, "H" : 7, "I" : 8, "J" : 9}
    row_values = {"a" : 0, "2" : 10, "3" : 20, "4" : 30, "5" : 40, "6" : 50, "7" : 60, "8" : 70, "9" : 80, "10" : 90}

    boatsText = {key: f"{key}- {value[2]} - {value[1]} Spaces" for key, value in boats.items()}
    remaining_boats = set(boats.keys())

    selected_boats = []

 
    while remaining_boats:
        for boat_id, boat_text in boatsText.items():
            if boat_id in remaining_boats:
                print(boat_text)
        boat = input("Pick the number boat you would like to place: ")

        if boat in remaining_boats:
            size = boats[boat][1]
            selected_boats.append((boats[boat][0], boats[boat][1]))
            remaining_boats.remove(boat)
        else:
            print("Invalid choice. Please pick a boat from the list.")
            continue
        
        column = set(column_values.keys())
        
        while True:
            placement_column = (input(f"What column (A - J) would you like to place your {boats[boat][2]} of size {size}? ")).upper()
            if placement_column in column:
                break
            else:
                print("Invalid column. Please enter a column from A to J.")

        row = set(row_values.keys())

        while True:
            placement_row = (input(f"What row (1 - 10) would you like to place your {boats[boat][2]} of size {size}? ")).upper()
            if placement_row in row:
                break
            else:
                print("Invalid row. Please enter a row from 1 to 10.")
        
        available_directions = {"W" : "up", "A" : "left", "S" : "down", "D" : "right"}

        while True:
            direction = (input("Using the WASD keys, select your desired direction: ")).upper()
            if direction in available_directions:
                break
            else:
                print("Invalid direction. Please enter a direction using WASD keys.")
        

    return print(selected_boats)

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
