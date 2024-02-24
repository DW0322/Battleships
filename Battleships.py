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
def printBoardP1(boardAttackP1, boardShipP1):
    print("                 ATTACK BOARD")
    print("   ", "A ", " B ", " C ", " D ", " E ", " F ", " G ", " H ", " I ", " J ")
    print("1", " |", boardAttackP1[0], "|", boardAttackP1[1], "|", boardAttackP1[2], "|", boardAttackP1[3], "|", boardAttackP1[4], "|", boardAttackP1[5], "|", boardAttackP1[6], "|", boardAttackP1[7], "|", boardAttackP1[8], "|", boardAttackP1[9], "|")
    print("2", " |", boardAttackP1[10], "|", boardAttackP1[11], "|", boardAttackP1[12], "|", boardAttackP1[13], "|", boardAttackP1[14], "|", boardAttackP1[15], "|", boardAttackP1[16], "|", boardAttackP1[17], "|", boardAttackP1[18], "|", boardAttackP1[19], "|")
    print("3", " |", boardAttackP1[20], "|", boardAttackP1[21], "|", boardAttackP1[22], "|", boardAttackP1[23], "|", boardAttackP1[24], "|", boardAttackP1[25], "|", boardAttackP1[26], "|", boardAttackP1[27], "|", boardAttackP1[28], "|", boardAttackP1[29], "|")
    print("4", " |", boardAttackP1[30], "|", boardAttackP1[31], "|", boardAttackP1[32], "|", boardAttackP1[33], "|", boardAttackP1[34], "|", boardAttackP1[35], "|", boardAttackP1[36], "|", boardAttackP1[37], "|", boardAttackP1[38], "|", boardAttackP1[39], "|")
    print("5", " |", boardAttackP1[40], "|", boardAttackP1[41], "|", boardAttackP1[42], "|", boardAttackP1[43], "|", boardAttackP1[44], "|", boardAttackP1[45], "|", boardAttackP1[46], "|", boardAttackP1[47], "|", boardAttackP1[48], "|", boardAttackP1[49], "|")
    print("6", " |", boardAttackP1[50], "|", boardAttackP1[51], "|", boardAttackP1[52], "|", boardAttackP1[53], "|", boardAttackP1[54], "|", boardAttackP1[55], "|", boardAttackP1[56], "|", boardAttackP1[57], "|", boardAttackP1[58], "|", boardAttackP1[59], "|")
    print("7", " |", boardAttackP1[60], "|", boardAttackP1[61], "|", boardAttackP1[62], "|", boardAttackP1[63], "|", boardAttackP1[64], "|", boardAttackP1[65], "|", boardAttackP1[66], "|", boardAttackP1[67], "|", boardAttackP1[68], "|", boardAttackP1[69], "|")
    print("8", " |", boardAttackP1[70], "|", boardAttackP1[71], "|", boardAttackP1[72], "|", boardAttackP1[73], "|", boardAttackP1[74], "|", boardAttackP1[75], "|", boardAttackP1[76], "|", boardAttackP1[77], "|", boardAttackP1[78], "|", boardAttackP1[79], "|")
    print("9", " |", boardAttackP1[80], "|", boardAttackP1[81], "|", boardAttackP1[82], "|", boardAttackP1[83], "|", boardAttackP1[84], "|", boardAttackP1[85], "|", boardAttackP1[86], "|", boardAttackP1[87], "|", boardAttackP1[88], "|", boardAttackP1[89], "|")
    print("10", "|", boardAttackP1[90], "|", boardAttackP1[91], "|", boardAttackP1[92], "|", boardAttackP1[93], "|", boardAttackP1[94], "|", boardAttackP1[95], "|", boardAttackP1[96], "|", boardAttackP1[97], "|", boardAttackP1[98], "|", boardAttackP1[99], "|")
    print("                 SHIP BOARD")
    print("   ", "A ", " B ", " C ", " D ", " E ", " F ", " G ", " H ", " I ", " J ")
    print("1", " |", boardShipP1[0], "|", boardShipP1[1], "|", boardShipP1[2], "|", boardShipP1[3], "|", boardShipP1[4], "|", boardShipP1[5], "|", boardShipP1[6], "|", boardShipP1[7], "|", boardShipP1[8], "|", boardShipP1[9], "|")
    print("2", " |", boardShipP1[10], "|", boardShipP1[11], "|", boardShipP1[12], "|", boardShipP1[13], "|", boardShipP1[14], "|", boardShipP1[15], "|", boardShipP1[16], "|", boardShipP1[17], "|", boardShipP1[18], "|", boardShipP1[19], "|")
    print("3", " |", boardShipP1[20], "|", boardShipP1[21], "|", boardShipP1[22], "|", boardShipP1[23], "|", boardShipP1[24], "|", boardShipP1[25], "|", boardShipP1[26], "|", boardShipP1[27], "|", boardShipP1[28], "|", boardShipP1[29], "|")
    print("4", " |", boardShipP1[30], "|", boardShipP1[31], "|", boardShipP1[32], "|", boardShipP1[33], "|", boardShipP1[34], "|", boardShipP1[35], "|", boardShipP1[36], "|", boardShipP1[37], "|", boardShipP1[38], "|", boardShipP1[39], "|")
    print("5", " |", boardShipP1[40], "|", boardShipP1[41], "|", boardShipP1[42], "|", boardShipP1[43], "|", boardShipP1[44], "|", boardShipP1[45], "|", boardShipP1[46], "|", boardShipP1[47], "|", boardShipP1[48], "|", boardShipP1[49], "|")
    print("6", " |", boardShipP1[50], "|", boardShipP1[51], "|", boardShipP1[52], "|", boardShipP1[53], "|", boardShipP1[54], "|", boardShipP1[55], "|", boardShipP1[56], "|", boardShipP1[57], "|", boardShipP1[58], "|", boardShipP1[59], "|")
    print("7", " |", boardShipP1[60], "|", boardShipP1[61], "|", boardShipP1[62], "|", boardShipP1[63], "|", boardShipP1[64], "|", boardShipP1[65], "|", boardShipP1[66], "|", boardShipP1[67], "|", boardShipP1[68], "|", boardShipP1[69], "|")
    print("8", " |", boardShipP1[70], "|", boardShipP1[71], "|", boardShipP1[72], "|", boardShipP1[73], "|", boardShipP1[74], "|", boardShipP1[75], "|", boardShipP1[76], "|", boardShipP1[77], "|", boardShipP1[78], "|", boardShipP1[79], "|")
    print("9", " |", boardShipP1[80], "|", boardShipP1[81], "|", boardShipP1[82], "|", boardShipP1[83], "|", boardShipP1[84], "|", boardShipP1[85], "|", boardShipP1[86], "|", boardShipP1[87], "|", boardShipP1[88], "|", boardShipP1[89], "|")
    print("10", "|", boardShipP1[90], "|", boardShipP1[91], "|", boardShipP1[92], "|", boardShipP1[93], "|", boardShipP1[94], "|", boardShipP1[95], "|", boardShipP1[96], "|", boardShipP1[97], "|", boardShipP1[98], "|", boardShipP1[99], "|")
def printBoardP2(boardAttackP2, boardShipP2):
    print("                 ATTACK BOARD")
    print("   ", "A ", " B ", " C ", " D ", " E ", " F ", " G ", " H ", " I ", " J ")
    print("1", " |", boardAttackP2[0], "|", boardAttackP2[1], "|", boardAttackP2[2], "|", boardAttackP2[3], "|", boardAttackP2[4], "|", boardAttackP2[5], "|", boardAttackP2[6], "|", boardAttackP2[7], "|", boardAttackP2[8], "|", boardAttackP2[9], "|")
    print("2", " |", boardAttackP2[10], "|", boardAttackP2[11], "|", boardAttackP2[12], "|", boardAttackP2[13], "|", boardAttackP2[14], "|", boardAttackP2[15], "|", boardAttackP2[16], "|", boardAttackP2[17], "|", boardAttackP2[18], "|", boardAttackP2[19], "|")
    print("3", " |", boardAttackP2[20], "|", boardAttackP2[21], "|", boardAttackP2[22], "|", boardAttackP2[23], "|", boardAttackP2[24], "|", boardAttackP2[25], "|", boardAttackP2[26], "|", boardAttackP2[27], "|", boardAttackP2[28], "|", boardAttackP2[29], "|")
    print("4", " |", boardAttackP2[30], "|", boardAttackP2[31], "|", boardAttackP2[32], "|", boardAttackP2[33], "|", boardAttackP2[34], "|", boardAttackP2[35], "|", boardAttackP2[36], "|", boardAttackP2[37], "|", boardAttackP2[38], "|", boardAttackP2[39], "|")
    print("5", " |", boardAttackP2[40], "|", boardAttackP2[41], "|", boardAttackP2[42], "|", boardAttackP2[43], "|", boardAttackP2[44], "|", boardAttackP2[45], "|", boardAttackP2[46], "|", boardAttackP2[47], "|", boardAttackP2[48], "|", boardAttackP2[49], "|")
    print("6", " |", boardAttackP2[50], "|", boardAttackP2[51], "|", boardAttackP2[52], "|", boardAttackP2[53], "|", boardAttackP2[54], "|", boardAttackP2[55], "|", boardAttackP2[56], "|", boardAttackP2[57], "|", boardAttackP2[58], "|", boardAttackP2[59], "|")
    print("7", " |", boardAttackP2[60], "|", boardAttackP2[61], "|", boardAttackP2[62], "|", boardAttackP2[63], "|", boardAttackP2[64], "|", boardAttackP2[65], "|", boardAttackP2[66], "|", boardAttackP2[67], "|", boardAttackP2[68], "|", boardAttackP2[69], "|")
    print("8", " |", boardAttackP2[70], "|", boardAttackP2[71], "|", boardAttackP2[72], "|", boardAttackP2[73], "|", boardAttackP2[74], "|", boardAttackP2[75], "|", boardAttackP2[76], "|", boardAttackP2[77], "|", boardAttackP2[78], "|", boardAttackP2[79], "|")
    print("9", " |", boardAttackP2[80], "|", boardAttackP2[81], "|", boardAttackP2[82], "|", boardAttackP2[83], "|", boardAttackP2[84], "|", boardAttackP2[85], "|", boardAttackP2[86], "|", boardAttackP2[87], "|", boardAttackP2[88], "|", boardAttackP2[89], "|")
    print("10", "|", boardAttackP2[90], "|", boardAttackP2[91], "|", boardAttackP2[92], "|", boardAttackP2[93], "|", boardAttackP2[94], "|", boardAttackP2[95], "|", boardAttackP2[96], "|", boardAttackP2[97], "|", boardAttackP2[98], "|", boardAttackP2[99], "|")
    print("                 SHIP BOARD")
    print("   ", "A ", " B ", " C ", " D ", " E ", " F ", " G ", " H ", " I ", " J ")
    print("1", " |", boardShipP2[0], "|", boardShipP2[1], "|", boardShipP2[2], "|", boardShipP2[3], "|", boardShipP2[4], "|", boardShipP2[5], "|", boardShipP2[6], "|", boardShipP2[7], "|", boardShipP2[8], "|", boardShipP2[9], "|")
    print("2", " |", boardShipP2[10], "|", boardShipP2[11], "|", boardShipP2[12], "|", boardShipP2[13], "|", boardShipP2[14], "|", boardShipP2[15], "|", boardShipP2[16], "|", boardShipP2[17], "|", boardShipP2[18], "|", boardShipP2[19], "|")
    print("3", " |", boardShipP2[20], "|", boardShipP2[21], "|", boardShipP2[22], "|", boardShipP2[23], "|", boardShipP2[24], "|", boardShipP2[25], "|", boardShipP2[26], "|", boardShipP2[27], "|", boardShipP2[28], "|", boardShipP2[29], "|")
    print("4", " |", boardShipP2[30], "|", boardShipP2[31], "|", boardShipP2[32], "|", boardShipP2[33], "|", boardShipP2[34], "|", boardShipP2[35], "|", boardShipP2[36], "|", boardShipP2[37], "|", boardShipP2[38], "|", boardShipP2[39], "|")
    print("5", " |", boardShipP2[40], "|", boardShipP2[41], "|", boardShipP2[42], "|", boardShipP2[43], "|", boardShipP2[44], "|", boardShipP2[45], "|", boardShipP2[46], "|", boardShipP2[47], "|", boardShipP2[48], "|", boardShipP2[49], "|")
    print("6", " |", boardShipP2[50], "|", boardShipP2[51], "|", boardShipP2[52], "|", boardShipP2[53], "|", boardShipP2[54], "|", boardShipP2[55], "|", boardShipP2[56], "|", boardShipP2[57], "|", boardShipP2[58], "|", boardShipP2[59], "|")
    print("7", " |", boardShipP2[60], "|", boardShipP2[61], "|", boardShipP2[62], "|", boardShipP2[63], "|", boardShipP2[64], "|", boardShipP2[65], "|", boardShipP2[66], "|", boardShipP2[67], "|", boardShipP2[68], "|", boardShipP2[69], "|")
    print("8", " |", boardShipP2[70], "|", boardShipP2[71], "|", boardShipP2[72], "|", boardShipP2[73], "|", boardShipP2[74], "|", boardShipP2[75], "|", boardShipP2[76], "|", boardShipP2[77], "|", boardShipP2[78], "|", boardShipP2[79], "|")
    print("9", " |", boardShipP2[80], "|", boardShipP2[81], "|", boardShipP2[82], "|", boardShipP2[83], "|", boardShipP2[84], "|", boardShipP2[85], "|", boardShipP2[86], "|", boardShipP2[87], "|", boardShipP2[88], "|", boardShipP2[89], "|")
    print("10", "|", boardShipP2[90], "|", boardShipP2[91], "|", boardShipP2[92], "|", boardShipP2[93], "|", boardShipP2[94], "|", boardShipP2[95], "|", boardShipP2[96], "|", boardShipP2[97], "|", boardShipP2[98], "|", boardShipP2[99], "|")

#battle ship design for vertical and horizontal placement
#battle ship placement round player 1

def boatSelection():
    
    boats = {
        "1" : ("V", 5, "Carrier"),
        "2" : ("W", 4, "Battleship"),
        "3" : ("X", 3, "Cruiser"),
        "4" : ("Y", 3, "Submarine"),
        "5" : ("Z", 2, "Destroyer")
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
            selected_boats.append((boats[boat][0], boats[boat][1]))
            remaining_boats.remove(boat)
        else:
            print("Invalid choice. Please pick a boat from the list.")
        
    return print(selected_boats)


#pens
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
