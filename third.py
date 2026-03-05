import turtle

screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)

def draw_petal():
    t.color("lightpink", "pink")
    t.begin_fill()
    t.circle(150, 60) 
    t.left(120)
    t.circle(150, 60) 
    t.left(120)
    t.end_fill()

def draw_stamen():
    t.color("orange")
    t.pensize(2)
    for _ in range(6):
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.forward(40)
        t.dot(5, "yellow")
        t.penup()
        t.goto(0, 0)
        t.left(60)

for _ in range(6):
    draw_petal()
    t.left(60)

draw_stamen()

t.goto(0, 0)
t.setheading(270)
t.color("green")
t.pensize(6)
t.pendown()
t.forward(250)

t.hideturtle()
turtle.done()
