import turtle

# Настройка экрана
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0) # Максимальная скорость

def draw_rose():
    # Рисуем цветок (лепестки)
    t.penup()
    t.goto(0, -50)
    t.pendown()
    t.color("red")
    t.begin_fill()
    
    # Основная форма бутона
    for i in range(500):
        t.forward(i / 7)
        t.left(10)
    t.end_fill()

   
draw_rose()

# Скрыть черепашку и оставить окно открытым
t.hideturtle()
turtle.done()
