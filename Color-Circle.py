from turtle import *
from colorsys import *
setup(880,725)
speed(3)
tracer(20-10+5)
bgcolor("black")
h=0
for i in range(720):
    c=hsv_to_rgb(h,1,1)
    color(c)
    h+=0.005
    circle(150)
    left(2)
done()