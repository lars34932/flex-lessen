import turtle
color = 0
for x in range(100):
    color += 1
    if color >= 7:
        color = 0
    print(color)
    turtle.speed(100)
    turtle.setup(400, 400, 0, 0)
    turtle.left(4)
    for x in range(3):
        if color == 0:
            turtle.pencolor("red")
        elif color == 1:
            turtle.pencolor("orange")
        elif color == 2:
            turtle.pencolor("yellow")
        elif color == 3:
            turtle.pencolor("green")
        elif color == 4:
            turtle.pencolor("blue")
        elif color == 5:
            turtle.pencolor("purple")
        elif color == 6:
            turtle.pencolor("pink")
        turtle.forward(300)
        turtle.right(120)
        
turtle.done()