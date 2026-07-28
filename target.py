## Import library code
from p5 import *
from random import randint

def shoot_arrow():
    global hit_colour
    arrow_x = randint(100, 300)
    arrow_y = randint(100, 300)
    hit_colour = get(arrow_x, arrow_y).hex
    fill('brown')
    circle(arrow_x, arrow_y, 15)

def setup():
    # Set up your game here
    size(400, 400)
    no_stroke()


def draw():
    # Things to do in every frame
    fill("cyan")
    rect(0, 0, 400, 300)
    fill('lightgreen')
    rect(0, 250, 400, 150)
    fill("brown")
    triangle(150, 350, 200, 150, 250, 350)
    fill('blue')
    circle(200, 200, 170)
    fill("red")
    circle(200, 200, 110)
    fill("yellow")
    circle(200, 200, 30)
    shoot_arrow()

def mouse_pressed():
    if hit_colour == Color('blue').hex:
        print('You hit the outer circle, 50 points!')
    elif hit_colour == Color('red').hex:
        print('You hit the inner circle, 200 points!')
    elif hit_colour == Color('yellow').hex:
        print('You hit the middle, 500 points!')
    else:
        print('You missed! No points!')
        
# Keep this to run your code
run(frame_rate=5)
