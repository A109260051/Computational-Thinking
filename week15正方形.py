import turtle
shelly = turtle.Turtle()
turtle.bgcolor("black")

for n in range(6):
    colors = ["red","green","blue","gold","purple","yellow"]
    shelly.color(colors[n])
    for i in range(4):
        shelly.forward(45)
        shelly.left(90)
    shelly.penup()
    shelly.forward(60)
    shelly.pendown()
    
shelly.hideturtle()
