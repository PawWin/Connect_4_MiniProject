import random as rd
#🔵
#🔴
print("Welcome to Connect Four")
print("-----------------------")
Letters = ["A","B","C","D","E","F","G"]
Board = [["","","","","","",""], ["","","","","","",""], ["","","","","","",""], ["","","","","","",""], ["","","","","","",""], ["","","","","","",""]]
rows = 6
cols = 7

def printBoard():
    print("\n     A    B    C    D    E    F    G  ", end="")
    for x in range(rows):
        print("\n   +----+----+----+----+----+----+----+")
        print(x, " |", end="")
        for y in range(cols):
            if Board[x][y] == "X":
                print(" 🔴 |", end="")
            elif Board[x][y] == "O":
                print(" 🟡 |", end="")
            else:
                print("    |", end="")
    print("\n   +----+----+----+----+----+----+----+")


def modifyBoard(column, turn):
    for row in range(rows-1, -1, -1):
        if Board[row][column] == "":
            Board[row][column] = turn
            return
    print("Column is full. Please pick another column.")

def checkForWinner(chip):
    # Check horizontal lines
    for y in range(cols):  # Iterate through columns
        for x in range(rows - 3):  # Ensure we have enough rows to check horizontally
            if Board[x][y] == chip and Board[x + 1][y] == chip and Board[x + 2][y] == chip and Board[x + 3][y] == chip:
                if chip == "X":
                    print("\nGame over! Player 1 wins! Thank you for playing :)")
                    return True
                else:
                    print("\nGame over! Player 2 wins! Thank you for playing :)")
                    return True

    # Check vertical lines
    for x in range(rows):  # Iterate through rows
        for y in range(cols - 3):  # Ensure we have enough columns to check vertically
            if Board[x][y] == chip and Board[x][y + 1] == chip and Board[x][y + 2] == chip and Board[x][y + 3] == chip:
                if chip == "X":
                    print("\nGame over! Player 1 wins! Thank you for playing :)")
                    return True
                else:
                    print("\nGame over! Player 2 wins! Thank you for playing :)")
                    return True

    # Check upper right to bottom left diagonal lines
    for x in range(rows - 3):
        for y in range(3, cols):
            if Board[x][y] == chip and Board[x + 1][y - 1] == chip and Board[x + 2][y - 2] == chip and Board[x + 3][y - 3] == chip:
                if chip == "X":
                    print("\nGame over! Player 1 wins! Thank you for playing :)")
                    return True
                else:
                    print("\nGame over! Player 2 wins! Thank you for playing :)")
                    return True

    # Check upper left to bottom right diagonal lines
    for x in range(rows - 3):
        for y in range(cols - 3):
            if Board[x][y] == chip and Board[x + 1][y + 1] == chip and Board[x + 2][y + 2] == chip and Board[x + 3][y + 3] == chip:
                if chip == "X":
                    print("\nGame over! Player 1 wins! Thank you for playing :)")
                    return True
                else:
                    print("\nGame over! Player 2 wins! Thank you for playing :)")
                    return True
    return False


def coordinateParser(input):
    match input:
        case "A":
            return 0
        case "B":
            return 1
        case "C":
            return 2
        case "D":
            return 3
        case "E":
            return 4
        case "F":
            return 5
        case "G":
            return 6
        case _:
            print("Invalid")
            return -1

def isSpaceAvailable(column):
    return any(Board[row][column] == "" for row in range(rows))

def game():
    turnCounter = 0
    while(True):
        printBoard()
        if(turnCounter % 2 == 0):
          print("\nPlayer 1's turn")
          spacePicked = input("Please pick a space (e.g. A): ")
          spacePicked = coordinateParser(spacePicked)
          if(isSpaceAvailable(spacePicked)):
              modifyBoard(spacePicked, "X")
              if(checkForWinner("X")):
                printBoard()
                break
              turnCounter += 1
          else:
              print("Space is already taken")
        else:
          print("\nPlayer 2's turn")
          spacePicked = input("Please pick a space (e.g. A): ")
          spacePicked = coordinateParser(spacePicked)
          if(isSpaceAvailable(spacePicked)):
              modifyBoard(spacePicked, "O")
              if(checkForWinner("O")):
                printBoard()
                break
              turnCounter += 1
          else:
              print("Space is already taken")

game()