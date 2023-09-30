'''
Code Written by Shiqi (John) Zhou, in 2020

Note: Looking back in 2023 there's a lot of improvements to be made in regards
to structuring and readability.

For example: Instead of having all the different pieces having its properties
put into the "play" function of "board.py", what I should've done was
put the functionality for each of the pieces into their own "piece handling"
function.

feel free to contact me at szhou110@ucr.edu!
'''
from board import Board
t = 0
boardgame = Board()

boardgame.printBoard()
while True:
  if boardgame.endgame() == True:   #this endgame
    break
  t = boardgame.play(t)
  boardgame.printBoard()
  
  
  
  