#!python3
"""
Create a function to check the winner in a Tic Tac Toe game.
Game data is stored in a list:
[0,0,0,0,0,0,0,0,0,0]

The index shows the position of the X's and O's in the following gameboard
using the references:
Position 0 is always empty, to help the numbering start at 1

123
456
789

So [0,"X",0,"O",0,"X",0,0,"X","O"]
would correspond to:
X.O
.X.
.XO


Create a function called winner(game) that receives the entire list as an
input parameter. It's return value is either:
0 (no winner)
"X" (X is a winner)
"O" (O is a winner)

"""

def winner(game):
    # input: list that contains 10 elements
    # output: either 0, "X", "O" to indicate who the winner is.
