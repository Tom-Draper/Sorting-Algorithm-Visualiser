import turtle

def setup(start_x, start_y, add_x_const, add_y_const, list):
    # Set up display window
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn_width = 1000
    wn_height = 1050
    wn.setup(wn_width, wn_height)
    wn.title("Sorting Algorithm Visualiser")

    # Set up drawing tool
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.pensize(3)
    pen.right(90)
    turtle.tracer(False) # Allows for updating drawn changes when suitable

    # Draw list equally distributed along top of the window
    pen.color("grey")
    x = start_x # X coordinate of top left of drawing area of window (negative value)
    for item in list:
        x += add_x_const # Add the x spacing between each item
        pen.up()
        pen.goto(x, start_y)
        pen.write(str(item), False, "center", font=("Arial", 16, "normal")) #Write value
    turtle.update() # Update window to show all list values at once

    # Draw initial vertical lines originating at the base of each of the values
    pen.color("yellow")
    x = start_x # X coordinate of top left of drawing area of window
    for item in list:
        x += add_x_const # Add the x spacing between each item
        pen.up()
        pen.goto(x, start_y)
        pen.down()
        pen.forward(add_y_const) # Draw line
    turtle.update() # Update window to show all lines at once

def showPass(start_x, start_y, add_x_const, add_y_const, pass_no, my_list, previous_list):
    # Set up drawing tool
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.pensize(3)
    pen.right(90)
    turtle.tracer(False)

    pen.color("yellow")
    # For each item in the list before changes made, find the item position in the new
    # list and draw corresponding line from old coodinate to new coordinate on window
    for item in previous_list:
        x = start_x # X coordinate of top left of drawing area of window
        y = start_y # Y coordinate of top left of drawing area of window
        previous_index = previous_list.index(item) #Get previous index of item in list
        new_index = 0

        # Move through new list to find first item that matches current item from previous list
        for new_item in my_list:
            if item == new_item:
                new_index = my_list.index(new_item) #Get items new index
                # Get x,y coordinate of position the items last line ended
                # Move x coordinate to right along the page to coordinate that items last line ended
                x += add_x_const * (previous_index + 1)
                # Move y coordinate down the page by the number of passes algorithm is currently on
                y -= add_y_const * pass_no
                pen.up()
                pen.goto(x, y)
                pen.down()
                # Get x,y coordinate of position the items new line will end
                # Move x coordinate left or right along the page using difference of new index and previous index
                x += add_x_const * (new_index - previous_index) 
                # Move y coordinate down the page by one multiple of the constant
                y -= add_y_const
                pen.goto(x, y) # Draw line
                break
        turtle.update() # Update window to show all lines drawn for each item for this pass

def bubbleSort(start_x, start_y, add_x_const, add_y_const, my_list):
    pass_no = 0
    for i in range(len(my_list) -1, 0, -1):
        for j in range(i):
            pass_no += 1 # Next pass
            previous_list = my_list[:] # Record list before any changes made in this pass

            # If in incorrect order, swap
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
            # Display changes made during this pass
            showPass(start_x, start_y, add_x_const, add_y_const, pass_no, my_list, previous_list)
            
    turtle.done() # Finished displaying
    
def insertionSort(start_x, start_y, add_x_const, add_y_const, my_list):
    pass_no = 0
    for i in range(1, len(my_list)): 
        key = my_list[i] 
        j = i-1
        pass_no += 1 # Next pass
        previous_list = my_list[:] # Record list before any changes made in this pass

        while j >= 0 and key < my_list[j]:
            my_list[j + 1] = my_list[j] 
            j -= 1
        my_list[j + 1] = key
        # Display changes made during this pass
        showPass(start_x, start_y, add_x_const, add_y_const, pass_no, my_list, previous_list)

    turtle.done()

def selectionSort(start_x, start_y, add_x_const, add_y_const, my_list):
    pass_no = 0
    for i in range(len(my_list)):
        minPosition = i
        for j in range(i+1, len(my_list)):
           if my_list[minPosition] > my_list[j]:
               minPosition = j

        pass_no += 1 # New pass
        previous_list = my_list[:] # Record list before any changes made in this pass
        # Swap items
        temp = my_list[i]
        my_list[i] = my_list[minPosition]
        my_list[minPosition] = temp
        # Display changes made during this pass
        showPass(start_x, start_y, add_x_const, add_y_const, pass_no, my_list, previous_list)
    
    turtle.done()

def visualiser(my_list):
    length = len(my_list)
    start_x = -450
    start_y = 450
    # X spacing between items in list
    # Divides middle 900 of window by the length of the list + 1
    add_x_const = 900 / (length + 1)

    # Calculates length of y spacing between each pass based on maximum space 
    # needed for bubble sort worst case scenario list of that size
    # For list of 4 items:
    # Window Space Available (900) = initial setup line (constant) + (3*constant) + (2*constant) + (constant)
    temp = 1 # Initial setup line constant
    for i in range(1, length): # Adds the constant from 1 to (length-1) times
        temp += i
    add_y_const = 900/temp

    # Display written list values and initial drawn lines
    setup(start_x, start_y, add_x_const, add_y_const, my_list)
    # Sort list and display after each pass
    bubbleSort(start_x, start_y, add_x_const, add_y_const, my_list)

# Get a list of integer values from user
inputValues = input("Enter a list of integers:\n")
listToSort = []
buildValue = ''
for idx in range(len(inputValues)):
    c = inputValues[idx]
    if (c.isdigit()):
        buildValue += c   # Building integer value
        if idx == len(inputValues) - 1:
            listToSort.append(int(buildValue))
    else:
        # If an integer value has been built, add to sorting list
        if len(buildValue) > 0:
            listToSort.append(int(buildValue))
            buildValue = '' # Reset
            
visualiser(listToSort)