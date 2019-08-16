import turtle

def setup(start_x, start_y, add_x_const, add_y_const, list):
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn_width = 1000
    wn_height = 1050
    wn.setup(wn_width, wn_height)
    wn.title("Sorting Algorithm Visualiser")

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.pensize(3)
    pen.right(90)
    turtle.tracer(False)

    pen.color("grey")
    x = start_x
    for item in list:
        x += add_x_const
        pen.up()
        pen.goto(x, start_y)
        pen.write(str(item), False, "center", font=("Arial", 16, "normal"))
    turtle.update()

    pen.color("yellow")
    x = start_x
    for item in list:
        x += add_x_const
        pen.up()
        pen.goto(x, start_y)
        pen.down()
        pen.forward(add_y_const)
    turtle.update()

    turtle.done()

def visualiser(my_list):
    length = len(my_list)
    start_x = -450
    start_y = 450
    add_x_const = 900 / (length + 1)
    add_y_const = 50

    setup(start_x, start_y, add_x_const, add_y_const, my_list)


visualiser([5, 4, 3, 2, 1])