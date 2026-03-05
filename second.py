import turtle

screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0) 

def draw_rose():

    t.penup()
    t.goto(0, -50)
    t.pendown()
    t.color("green")
    t.begin_fill()
    
    for i in range(500):
        t.forward(i / 7)
        t.left(10)
    t.end_fill()

   
draw_rose()
t.hideturtle()
turtle.done()
