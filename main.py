import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)

n = 50
h = 0

# Рисуем плотный компактный узор
for i in range(200):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(c)
    h += 1/n
    
    # Фиксированная длина 10px
    t.forward(10) 
    t.left(45)
    t.forward(10)
    t.right(150)
    t.circle(10, 90) # Добавил изгиб для красоты

turtle.done()
