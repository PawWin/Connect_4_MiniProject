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
      if(Board[x][y] == "X"):
        print("",Board[x][y], end=" |")
      elif(Board[x][y] == "O"):
        print("", Board[x][y], end=" |")
      else:
        print(" ", Board[x][y], end="  |")
  print("\n   +----+----+----+----+----+----+----+")

def modifyBoard(spacePicked, turn):
    Board[spacePicked[0]][spacePicked[1]] = turn

def checkForWinner(chip):
  # Check horizontal spaces
  for y in range(rows):
    for x in range(cols - 3):
      if Board[x][y] == chip and Board[x+1][y] == chip and Board[x+2][y] == chip and Board[x+3][y] == chip:
        print("\nGame over!", chip, "wins! Thank you for playing :)")
        return True

  # Check vertical spaces
  for x in range(rows):
    for y in range(cols - 3):
      if Board[x][y] == chip and Board[x][y+1] == chip and Board[x][y+2] == chip and Board[x][y+3] == chip:
        print("\nGame over!", chip, "wins! Thank you for playing :)")
        return True

  # Check upper right to bottom left diagonal spaces
  for x in range(rows - 3):
    for y in range(3, cols):
      if Board[x][y] == chip and Board[x+1][y-1] == chip and Board[x+2][y-2] == chip and Board[x+3][y-3] == chip:
        print("\nGame over!", chip, "wins! Thank you for playing :)")
        return True

  # Check upper left to bottom right diagonal spaces
  for x in range(rows - 3):
    for y in range(cols - 3):
      if Board[x][y] == chip and Board[x+1][y+1] == chip and Board[x+2][y+2] == chip and Board[x+3][y+3] == chip:
        print("\nGame over!", chip, "wins! Thank you for playing :)")
        return True
  return False

