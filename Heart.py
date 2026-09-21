from turtle import *
import math
import time

setup(800, 700)
bgcolor("#121212")
title("I Love Python - Special Animation")
tracer(0)
hideturtle()

def heart_x(t):
    return 16 * math.sin(t)**3

def heart_y(t):
    return 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)

def draw_heart(size, color_code):
    clear()
    
    penup()
    goto(0, 180)
    color("#FFFFFF")
    write("I Love Python", align="center", font=("Helvetica", 32, "bold"))
    
    goto(0, 140)
    color("#FF2E93")
    write("❤ Click anywhere to change color ❤", align="center", font=("Arial", 12, "italic"))

    penup()
    color(color_code)
    fillcolor(color_code)
    begin_fill()
    
    for i in range(0, 628):
        t = i / 100
        x = heart_x(t) * size
        y = heart_y(t) * size
        goto(x, y - 50)
        if i == 0:
            pendown()
            
    end_fill()
    update()

current_color_index = 0
colors_list = ["#FF2E93", "#FF4141", "#FF8000", "#00F5FF", "#A020F0"]
scale = 13
growing = True

def change_color(x, y):
    global current_color_index
    current_color_index = (current_color_index + 1) % len(colors_list)

listen()
onscreenclick(change_color)

while True:
    if growing:
        scale += 0.15
        if scale >= 14.5:
            growing = False
    else:
        scale -= 0.15
        if scale <= 12.5:
            growing = True
            
    draw_heart(scale, colors_list[current_color_index])
    
    time.sleep(0.02)