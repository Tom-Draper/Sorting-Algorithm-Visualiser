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

def showPass(start_x, start_y, add_x_const, add_y_const, pass_no, my_list, previous_list):
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.pensize(3)
    pen.right(90)
    turtle.tracer(False)

    pen.color("yellow")
    for item in previous_list:
        x = start_x
        y = start_y
        previous_index = previous_list.index(item)
        new_index = 0

        for new_item in my_list:
            if item == new_item:
                new_index = my_list.index(new_item)
                x += add_x_const * (previous_index + 1)
                y -= add_y_const * pass_no
                pen.up()
                pen.goto(x, y)
                pen.down()
                x += add_x_const * (new_index - previous_index) 
                y -= add_y_const
                pen.goto(x, y)
                break
        turtle.update()

def bubbleSort(start_x, start_y, add_x_const, add_y_const, my_list):
    pass_no = 0
    for i in range(len(my_list) -1, 0, -1):
        for j in range(i):
            pass_no += 1
            previous_list = my_list[:]
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
            showPass(start_x, start_y, add_x_const, add_y_const, pass_no, my_list, previous_list)
            
    turtle.done()

def visualiser(my_list):
    length = len(my_list)
    start_x = -450
    start_y = 450
    add_x_const = 900 / (length + 1)
    add_y_const = 50

    setup(start_x, start_y, add_x_const, add_y_const, my_list)
    bubbleSort(start_x, start_y, add_x_const, add_y_const, my_list)

visualiser([5, 4, 3, 2, 1])