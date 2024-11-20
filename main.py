# Griffin King
# U3 project
# Making a tree using turtle


"""
IMPORTANT
To run your code in this project,
open the Terminal and enter the following:

python main.py    then enter

Your output will be visualized in the 
Virtual Desktop
"""

import turtle as t
from os import system
from random import randint
from time import sleep

TURTLEANGLES = [-45,45]
TURTLEDISTANCE = 40
TURTLEDISTANCESUB = 4
NUMBERBRANCHING = 10


TURTLEBRANCHCOLOR = "brown"
TURTLEWIDTH = 10
TURTLEWIDTHSUB = 1
TURTLEBRANCHING = 2
NUMBERBRANCHINGOUT = 8

TURTLELEAFCOLOR = "green"
TURTLELEAFWIDTH = 7
TURTLELEAFDISTANCE = 10

# The base case is when then a variable I made and the global variable is the same, I tick up the inside variable that sees the place it is
# it should save the angle, current branch will be tracked, the length will be subtracted, the width, and the position should be saved to go back and make new branches
#  Making it branch off, making it get smaller and thinner, make the base case change the color and actually stop and go backwards


def tree(currentBranching = 0, currentAngle = 90, currentLength = TURTLEDISTANCE,currentWidth = TURTLEWIDTH, branchesContinued = 2):
  if currentBranching == NUMBERBRANCHINGOUT:
    t.color(TURTLELEAFCOLOR)
    t.pensize(TURTLELEAFWIDTH)

    t.lt(currentAngle)
    t.forward(TURTLELEAFDISTANCE)

    t.penup()
    t.backward(TURTLELEAFDISTANCE)
    t.rt(currentAngle)
    t.pendown()
  else:
    t.color(TURTLEBRANCHCOLOR)
    t.pensize(currentWidth)
    
    t.lt(currentAngle)
    t.forward(currentLength)
    if branchesContinued == 1:
      tree(currentBranching + 1,randint(TURTLEANGLES[0],TURTLEANGLES[1]), currentLength - TURTLEDISTANCESUB, currentWidth - TURTLEWIDTHSUB, randint(0,TURTLEBRANCHING) )
    else:
      tree(currentBranching + 1, randint(TURTLEANGLES[0],TURTLEANGLES[1]), currentLength - TURTLEDISTANCESUB, currentWidth - TURTLEWIDTHSUB, randint(0,TURTLEBRANCHING))
      tree(currentBranching + 1, randint(TURTLEANGLES[0],TURTLEANGLES[1]), currentLength - TURTLEDISTANCESUB, currentWidth - TURTLEWIDTHSUB, randint(0,TURTLEBRANCHING)) 
  
    t.penup()
    t.backward(currentLength)
    t.rt(currentAngle)
    t.pendown()

def main():
  t.speed(0.02)
  tree()
  sleep(10)
if __name__ == "__main__":
  system("clear")
  main()