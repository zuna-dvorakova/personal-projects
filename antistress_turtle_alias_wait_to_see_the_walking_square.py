import turtle
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw():
    num_repeats = 18
    for i in range(num_repeats):
        turtle.color(random_color())
        turtle.left(100)
        turtle.forward(200)

turtle.colormode(255) 

turtle.shape("turtle")
turtle.color("white")
turtle.forward(100)
draw()

turtle.shape("square")
draw()

turtle.done()