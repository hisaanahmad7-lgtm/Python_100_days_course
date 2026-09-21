import turtle
import colorsys
import math

def draw():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Star Vortex")
    screen.setup(width = 900 , height = 900)
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    screen.tracer(20 , 0)
    
    iterations = 1000
    cycles = 60

    for i in range(iterations):
        hue = i / iterations
        color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        t.pencolor(color)
        
        t.pensize(1)
        angle = i * (1000/ cycles) + (i * 0.2)
        distance = math.sqrt(i) * 18 
        
        t.penup()
        t.goto(0, 0)
        t.setheading(angle)
        t.forward(distance)
        t.pendown()
        
        t.fillcolor(colorsys.hsv_to_rgb((hue + 0.5) % 1.0 , 0.9 , 0.5))
        t.begin_fill()

        star_size = (math.sqrt(i) * 0.8) + 5 
        for j in range(20):
            t.forward(star_size)
            t.right(144)
            t.forward(star_size)
            t.left(72)
        t.end_fill()   
    
    screen.update()
    turtle.done()

draw()