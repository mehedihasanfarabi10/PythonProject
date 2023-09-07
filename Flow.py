import colorsys
from turtle import *
from colorsys import *

tracer(300)
bgcolor('black')

def draw():
    h = 0
    for i in range(120):
        c = colorsys.hsv_to_rgb(h,1,1)
        h +=0.5
        up()
        goto(0,0)
        down()
        color('black')
        fillcolor(c)
        begin_fill()
        rt(98)
        circle(i,12)
        fd(290)
        fd(i)
        lt(29)
        for j in range(129):
            fd(i)
            circle(j,299,steps=2)
        end_fill()
draw()
done()
