#!/usr/bin/env python
import math
from FractalWorld import *
# set width and height of graphics window
# switch off delay
world = FractalWorld(width=700,height=500,delay=0)

# generate a turtle that is shown in the window if, and only if, draw=True
turtle = Fractal(draw=False)

# recursively draw a Koch curve
#   t      is the turtle
#   s      is the length
#   depth  is the limit for the recusion
def koch(t, s, depth):
  if depth <= 0:
    # base case - draw a line
    fd(t, s)
  else:
    # step case - draw four Koch curves
    koch(t, s/3, depth-1)
    lt(t,60)
    koch(t, s/3, depth-1)
    rt(t,120)
    koch(t, s/3, depth-1)
    lt(t,60)
    koch(t, s/3, depth-1)
  # the following conditional update can be used if draw=False
  # if s > 10: world.update()

# position the turtle
pu(turtle)
bk(turtle, 121)
rt(turtle)
bk(turtle, 60)
lt(turtle)
pd(turtle)

# draw three Koch curves to obtain a snowflake
for i in range(3):
  koch(turtle, 243, 2)
  rt(turtle,120)
wait_for_user()
