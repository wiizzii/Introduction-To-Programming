from FractalWorld import *
world = FractalWorld(width=1900,height=1000)
turtle = Fractal(draw=True)
print turtle
set_pen_color(turtle,"Green")
color=["Brown","Blue","Green"]

def tree(t,l,a,depth):
 if depth==0:
  return
 #experementing with colors
 if depth<4:
  set_pen_color(t,"#1a9108")
 elif depth==4:
  set_pen_color(t,"#d14500")
 elif depth==5:
  set_pen_color(t,"#b23b00")
 elif depth==6:
  set_pen_color(t,"#993401")
 else: 
  set_pen_color(t,"#7A2900") 
 pd(t)
 fd(t,l/0.666**depth,2*depth-1)
 rt(t,a)
 tree(t,l,a,depth-1)
 lt(t, 2*a)
 tree(t,l,a,depth-1)
 rt(t,a)
 pu(t)
 bk(t,l/0.666**depth)

pu(turtle)
lt(turtle)
bk(turtle, 450)
pd(turtle)

tree(turtle,5,30,10)
wait_for_user()
