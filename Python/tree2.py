from FractalWorld import *
world = FractalWorld(width=1900,height=1000)
turtle = Fractal(draw=True)
print turtle
set_pen_color(turtle,"Green")

def tree(t,l,a,depth):
 if depth==0:
  return
#  print '1',depth
 fd(t,l/0.666**depth,2*depth-1)
 rt(t,a)
 tree(t,l,a,depth-1)
# print '2',depth
 lt(t, 2*a)
 tree(t,l,a,depth-1)
# print '3',depth
 rt(t,a)
 bk(t,l/0.666**depth)
# print '4',depth

pu(turtle)
lt(turtle)
bk(turtle, 450)
pd(turtle)

tree(turtle,5,30,10)
wait_for_user()
