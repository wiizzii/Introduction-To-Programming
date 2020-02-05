from FractalWorld import *
world = FractalWorld(width=900,height=800,delay=0.3)
turtle = Fractal(draw=True)
print turtle
set_pen_color(turtle, "Red")
set_color(turtle, "Green")

def triangle(t, l, depth):
 if depth <= 0:
  #here the turtle draws the triangles
  for i in range(3):
   fd(t, l)
   lt(t, 120)
 else:
  for i in range(3):
   #here the turtle postions itself for the next triangle
   
   fd(t, l*2**depth, depth-1) #depth here is the thickness of drawline
   lt(t, 120)
   triangle(t, l, depth-1)
#positons the turtle at the begining
pu(turtle)
bk(turtle, 300)
lt(turtle)
bk(turtle, 250)
rt(turtle)
pd(turtle)

triangle(turtle, 50, 3)    
wait_for_user()
