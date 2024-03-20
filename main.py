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

