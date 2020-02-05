from FractalWorld import *
world = FractalWorld(width=1900,height=800)
turtle = Fractal(draw=True)
set_pen_color(turtle,"Green")

def draw(t, length, n):

    if n == 0:
        return
    angle = 20
    fd(t, length*n)
    lt(t, angle)
    draw(t, length, n-1)
    rt(t, 2*angle)
    draw(t, length, n-1)
    lt(t, angle)
    bk(t, length*n)

turtle.delay = 0.01
lt(turtle)
pu(turtle)
bk(turtle, 100)
pd(turtle)
draw(turtle, 10, 1)
wait_for_user()
