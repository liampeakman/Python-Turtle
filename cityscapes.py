
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n10203036
#    Student name: LIAM PEAKMAN
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  CITYSCAPES
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and efficiently repeating multiple actions in
#  order to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "build_city".
#  You are required to complete this function so that when the
#  program is run it draws a city whose plan is determined by
#  randomly-generated data stored in a list which specifies what
#  style of building to erect on particular sites.  See the
#  instruction sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single Python 3 file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must not rely on any non-standard Python
# modules that need to be installed separately, because the markers
# may not have access to such modules.

from turtle import *
from math import *
from random import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

canvas_height = 700 # pixels
canvas_width = 1100 # pixels
grass_depth = 95 # vertical depth of the "grass", in pixels
half_width = canvas_width // 2 # maximum x coordinate in either direction
grid_font = ('Arial', 10, 'normal') # font for drawing the grid
grid_size = 50 # gradations for the x and y scales shown on the screen
offset = 5 # offset of the x-y coordinates from the screen's edge, in pixels
max_height = canvas_height - grass_depth # maximum positive y coordinate
max_building_height = 575 # city ordinance maximum building height
site_width = 240 # maximum width of a building site

# Define the locations of building sites approved by the
# city council (arranged from back to front)
sites = [['Site 1', [-225, 0]],
         ['Site 2', [25, 0]],
         ['Site 3', [275, 0]],
         ['Site 4', [-375, -25]],
         ['Site 5', [-125, -25]],
         ['Site 6', [125, -25]],
         ['Site 7', [375, -25]],
         ['Site 8', [-275, -50]],
         ['Site 9', [-25, -50]],
         ['Site 10', [225, -50]]]

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image.
# By default the drawing grid is displayed - call the function
# with False as the argument to prevent this.
def create_drawing_canvas(show_grid = True):

    # Set up the drawing canvas with coordinate (0, 0) in the
    # "grass" area
    setup(canvas_width, canvas_height)
    setworldcoordinates(-half_width, -grass_depth, half_width, max_height)

    # Draw as fast as possible
    tracer(False)

    # Make the sky blue
    bgcolor('sky blue')

    # Draw the "grass" as a big green rectangle (overlapping the
    # edge of the drawing canvas slightly)
    overlap = 25 # pixels
    penup()
    goto(-(half_width + overlap), -(grass_depth + overlap)) # bottom-left
    fillcolor('pale green')
    begin_fill()
    setheading(90) # face north
    forward(grass_depth + overlap * 2)
    right(90) # face east
    forward(canvas_width + overlap * 2)
    right(90) # face south
    forward(grass_depth + overlap * 2)
    end_fill()

    # Draw a nice warm sun peeking into the image at the top left
    penup()
    goto(-canvas_width // 2, canvas_height - grass_depth)
    pencolor('yellow')
    dot(350)

    # Draw a big fluffy white cloud in the sky
    goto(canvas_width // 3, canvas_height - grass_depth - 100)
    pencolor('white')
    dot(200)
    setheading(200)
    forward(100)
    dot(180)
    setheading(0)
    forward(200)
    dot(160)

    # Optionally draw x coordinates along the bottom of the
    # screen (to aid debugging and marking)
    pencolor('black')
    if show_grid:
        for x_coord in range(-half_width + grid_size, half_width, grid_size):
            goto(x_coord, -grass_depth + offset)
            write('| ' + str(x_coord), font = grid_font)

    # Optionally draw y coordinates on the left-hand edge of
    # the screen (to aid debugging and marking)
    if show_grid:
        for y_coord in range(-grid_size, max_height, grid_size):
            goto(-half_width + offset, y_coord - offset)
            write(y_coord, font = grid_font)
        goto(-half_width + offset, max_building_height - 5)
        write('Maximum allowed building height', font = grid_font)

    # Optionally mark each of the building sites approved by
    # the city council
    if show_grid:
        for site_name, location in sites:
            goto(location)
            dot(5)
            goto(location[0] - (site_width // 2), location[1])
            setheading(0)
            pendown()
            forward(site_width)
            penup()
            goto(location[0] - 40, location[1] - 17)
            write(site_name + ': ' + str(location), font = grid_font)
     
    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas.
# By default the cursor (turtle) is hidden when the program
# ends - call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any drawing in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the build_city function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the random_plan function appearing below.  Your
# program must work correctly for any data set generated by the
# random_plan function.
#
# Each of the data sets below is a list specifying a set of
# buildings to be erected.  Each specification consists of the
# following parts:
#
# a) The site on which to erect the building, from Site 1 to 10.
# b) The style of building to be erected, from style 'A' to 'D'.
# c) The number of floors to be constructed, from 1 to 10.
# d) An extra value, either 'X' or 'O', whose purpose will be
#    revealed only in Part B of the assignment.  You should
#    ignore it while completing Part A.
#

# Each of these data sets draws just one building in each of the
# four styles
fixed_plan_1 = [[1, 'A', 6, 'O']]
fixed_plan_2 = [[2, 'B', 7, 'O']]
fixed_plan_3 = [[3, 'C', 5, 'O']]
fixed_plan_4 = [[4, 'D', 4, 'O']]
fixed_plan_5 = [[1, 'A', 9, 'X']]
fixed_plan_6 = [[2, 'B', 2, 'X']]
fixed_plan_7 = [[3, 'C', 3, 'X']]
fixed_plan_8 = [[4, 'D', 6, 'X']]

# Each of the following data sets draws just one style of
# building but at three different sizes, including the maximum
# (so that you can check your building's maximum height against
# the height limit imposed by the city council)
fixed_plan_9 = [[1, 'A', 10, 'O'], [2, 'A', 5, 'O'], [3, 'A', 1, 'O']]
fixed_plan_10 = [[1, 'B', 10, 'O'], [2, 'B', 5, 'O'], [3, 'B', 1, 'O']]
fixed_plan_11 = [[1, 'C', 10, 'O'], [2, 'C', 5, 'O'], [3, 'C', 1, 'O']]
fixed_plan_12 = [[1, 'D', 10, 'O'], [2, 'D', 5, 'O'], [3, 'D', 1, 'O']]
fixed_plan_13 = [[1, 'A', 10, 'X'], [2, 'A', 5, 'X'], [3, 'A', 1, 'X']]
fixed_plan_14 = [[1, 'B', 10, 'X'], [2, 'B', 5, 'X'], [3, 'B', 1, 'X']]
fixed_plan_15 = [[1, 'C', 10, 'X'], [2, 'C', 5, 'X'], [3, 'C', 1, 'X']]
fixed_plan_16 = [[1, 'D', 10, 'X'], [2, 'D', 5, 'X'], [3, 'D', 1, 'X']]

# Each of the following data sets draws a complete cityscape
# involving each style of building at least once. There is
# no pattern to them, they are simply specific examples of the
# kind of data returned by the random_plan function which will be
# used to assess your solution. Your program must work for any value
# that can be returned by the random_plan function, not just these
# fixed data sets.
fixed_plan_17 = \
         [[1, 'D', 2, 'O'],
          [2, 'B', 7, 'O'],
          [5, 'C', 6, 'O'],
          [6, 'A', 4, 'O']]
fixed_plan_18 = \
         [[1, 'D', 6, 'O'],
          [3, 'C', 5, 'O'],
          [4, 'B', 3, 'O'],
          [9, 'A', 9, 'O'],
          [10, 'D', 2, 'O']]
fixed_plan_19 = \
         [[5, 'C', 6, 'O'],
          [6, 'B', 9, 'O'],
          [7, 'A', 5, 'O'],
          [8, 'A', 7, 'O'],
          [9, 'D', 4, 'O']]
fixed_plan_20 = \
         [[1, 'A', 4, 'O'],
          [2, 'B', 4, 'O'],
          [3, 'A', 5, 'O'],
          [4, 'D', 7, 'O'],
          [10, 'B', 10, 'O']]
fixed_plan_21 = \
         [[1, 'B', 6, 'O'],
          [3, 'A', 4, 'O'],
          [4, 'C', 4, 'O'],
          [6, 'A', 8, 'O'],
          [8, 'C', 7, 'O'],
          [9, 'B', 5, 'O'],
          [10, 'D', 3, 'O']]
fixed_plan_22 = \
         [[1, 'A', 10, 'O'],
          [2, 'A', 9, 'O'],
          [3, 'C', 10, 'O'],
          [4, 'B', 5, 'O'],
          [5, 'B', 7, 'O'],
          [6, 'B', 9, 'O'],
          [7, 'C', 2, 'O'],
          [8, 'C', 4, 'O'],
          [9, 'A', 6, 'O'],
          [10, 'D', 7, 'O']]
fixed_plan_23 = \
         [[3, 'A', 8, 'O'],
          [4, 'C', 8, 'O'],
          [5, 'B', 4, 'O'],
          [6, 'D', 5, 'O'],
          [7, 'C', 5, 'X'],
          [8, 'A', 3, 'X'],
          [9, 'D', 2, 'X']]
fixed_plan_24 = \
         [[2, 'C', 3, 'O'],
          [3, 'B', 1, 'O'],
          [4, 'C', 3, 'X'],
          [5, 'C', 1, 'O'],
          [6, 'D', 2, 'O'],
          [7, 'B', 1, 'O'],
          [8, 'D', 2, 'O'],
          [9, 'C', 7, 'O'],
          [10, 'A', 1, 'X']]
fixed_plan_25 = \
         [[1, 'B', 7, 'X'],
          [3, 'C', 1, 'O'],
          [6, 'D', 3, 'O'],
          [7, 'A', 7, 'O'],
          [8, 'D', 3, 'X'],
          [9, 'C', 7, 'O'],
          [10, 'C', 9, 'X']]
fixed_plan_26 = \
         [[1, 'A', 6, 'O'],
          [2, 'A', 2, 'O'],
          [3, 'A', 9, 'X'],
          [4, 'D', 1, 'X'],
          [5, 'C', 7, 'O'],
          [6, 'D', 6, 'O'],
          [7, 'B', 5, 'O'],
          [8, 'A', 1, 'O'],
          [9, 'D', 10, 'X'],
          [10, 'A', 6, 'O']]
fixed_plan_27 = \
         [[4, 'A', 5, 'X'],
          [5, 'B', 5, 'X'],
          [6, 'C', 5, 'X'],
          [7, 'D', 5, 'X']]
   
#
#--------------------------------------------------------------------#



#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to mark your solution.
# Do not change any of the code in this section.
#
# The following function creates a random data set specifying a city
# to be built.  Your program must work for any data set returned by
# this function.  The results returned by calling this function will
# be used as the argument to your build_city function during marking.
# For convenience during code development and marking this function
# also prints the plan for the city to be built to the shell window.
#

def random_plan(print_plan = True):
    building_probability = 70 # percent
    option_probability = 20 # percent
    from random import randint, choice
    # Create a random list of building instructions
    city_plan = []
    for site in range(1, len(sites) + 1): # consider each building site
        if randint(1, 100) <= building_probability: # decide whether to build here
            style = choice(['A', 'B', 'C', 'D']) # choose building style
            num_floors = randint(1, 10) # choose number of floors
            if randint(1, 100) <= option_probability: # decide on option's value
                option = 'X'
            else:
                option = 'O'
            city_plan.append([site, style, num_floors, option])
    # Optionally print the result to the shell window
    if print_plan:
        print('\nBuildings to be constructed\n' +
              '(site, style, no. floors, option):\n\n',
              str(city_plan).replace('],', '],\n '))
    # Return the result to the student's build_city function
    return city_plan

#
#------DEFINITIONS--------------------------------------------------#

## DIRECTIONS
def go_up(l):    #Directs the turtle up, down, left, right when given a length
    pu()
    left(90)
    forward(l)
    left(-90)
    pd()
    
def go_down(l):
    pu()
    left(-90)
    forward(l)
    left(90)
    pd()

def go_left(l):
    pu()
    left(180)
    forward(l)
    left(-180)
    pd()

def go_right(l):
    pu()
    setheading(0)
    forward(l)
    pd()
    
## MAIN SHAPES
def rectangle(l, h, pc, fc):
    pu()                
    pencolor(pc)
    fillcolor(fc)
    begin_fill()
    left(90)
    forward(h)
    left(90)
    pd()
    forward(l/2) 
    left(90)
    forward(h)
    left(90)
    forward(l)
    left(90)
    forward(h)
    left(90)
    forward(l/2)
    left(180)
    end_fill()
    
def semi_circle(rad, dis, pc, fc):
    fillcolor(fc)
    pencolor(pc)
    begin_fill()
    forward(dis)
    left(90)
    pd()
    circle(rad, 180)                #Gives an angle of 180 to make it a semi circle
    end_fill()
    left(90)
    forward(dis)
    
def quadrant(rad, dis, pc, fc):
    fillcolor(fc)
    pencolor(pc)
    begin_fill()
    forward(dis)
    left(90)
    pd()
    circle(rad, 90)
    end_fill()
    left(90)
    forward(dis)
    left(90)
    
def triangle(l, h, pc, fc):
    pd()
    pencolor(pc)
    fillcolor(fc)
    begin_fill()
    forward(l/2)
    left(150)
    pd()
    forward(sqrt(((l//2)**2)+(h**2)))           #Pythag 
    left(60)
    forward(sqrt(((l//2)**2)+(h**2)))
    left(150)
    forward(l/2)
    end_fill()
    
def rounded_square(l, h, pc, fc):
    left(180)
    semi_circle(l/2, l/2, pc, fc)
    go_down(h)
    rectangle(l, h, pc, fc)
    left(180)
    go_up(h)

def door(l, h, pc1, fc1, pc2, fc2, x):

    if x > 1:                       #If there's more then one door turtle moves the length to center the doors
        pu()
        forward(l/2)
        left(270)
        forward(h)
        left(90)
        pd()
    
    pu()                        #Draws first door
    pencolor(pc1)
    fillcolor(fc1)
    begin_fill()
    left(90)
    forward(h)
    left(90)
    pd()
    forward(l/2)
    left(90)
    forward(h)
    left(90)
    forward(l)
    left(90)
    forward(h)
    left(90)
    forward(l/2)
    left(90)
    end_fill()
    
    pu()                        #Draws second door
    forward(h / (1 + (1/3)))
    left(180)
    forward(h/2)
    left(90)
    pencolor(pc2)
    fillcolor(fc2)
    begin_fill()
    pd()
    forward(l/4)
    left(90)
    forward(h/2)
    left(90)
    forward(l/2)
    left(90)
    forward(h/2)
    left(90)
    forward(l/4)
    end_fill()
    pu()
    left(90)
    forward(h / (1 + (1/3)))
    left(90)

    if x > 1:           #Prepare to draw another door 
        forward(-l)
    else:               #Finishes drawing at original point
        pu()
        forward(l/2)
        left(90)
        forward(h)
        left(270)
        
#STYLE A SHAPES
def telescope():
    pu()
    x = randint(50, 70)     #Finding a starting position of drawing along roof
    forward(110)
    left(90)
    circle(110, x)
    left(180)
    rectangle(10, 15, "black", "light steel blue")
    rectangle(20, 30, "black", "light steel blue")
    rectangle(40, 50, "black", "light steel blue")
    semi_circle(20, 20, "black", "white smoke")
    rectangle(50, 10, "black", "light steel blue")
    pu()
    left(270)
    forward(210)
    setheading(0)

#STYLE B SHAPES
def window_row_b(pc, fc):
    pencolor(pc)
    fillcolor(fc)               #Draws a row of 5 windows  
    begin_fill()
    go_down(35)
    rectangle(20, 30, pc, fc)
    go_down(30)
    go_left(30)
    rectangle(20, 30, pc, fc)
    go_down(30)
    go_left(30)
    rectangle(20, 30, pc, fc)
    go_down(30)
    go_right(90)
    rectangle(20, 30, pc, fc)
    go_down(30)
    go_right(30)
    rectangle(20, 30, pc, fc)
    end_fill()
    go_up(5)
    go_left(60)
    
def roof_style_b():
    pd()
    rectangle(10, 30, "grey", "grey")   #Draw sign shape
    go_down(5)
    fillcolor("alice blue")
    pensize(3)
    pencolor("sienna")
    begin_fill()
    left(5)
    forward(40)
    circle(20, 70)
    forward(20)
    circle(20, 100)
    forward(100)
    circle(20, 130)
    forward(42)
    circle(20, 60)
    forward(40)
    end_fill()
    pu()
    go_left(55)
    go_up(30)
                        #Draw out HOTEL

    x = 20
    pencolor("sienna")
    #H
    setheading(0)
    pensize(5)
    left(90)
    pd()
    forward(x)
    right(90)
    go_down(x/2)
    forward(x/2)
    go_up(x/2)
    right(90)
    forward(x)
    left(90)
    go_right(20)

    #O
    circle(x/2)
    go_right(22)

    #T
    left(90)
    forward(x)
    right(90)
    go_left(x/3)
    forward(2*(x/3))
    go_left(x/3)
    go_down(x)
    go_right(15)

    #E
    forward(x/2)
    go_left(x/2)
    go_up(x/2)
    forward(x/2)
    go_left(x/2)
    go_up(x/2)
    forward(x/2)
    go_left(x/2)
    right(90)
    forward(x)
    left(90)
    go_right(20)

    #L
    left(90)
    forward(x)
    right(90)
    go_down(x)
    forward(x/2)

#STYLE C SHAPES
def window_row_c(pc, fc):
    pencolor(pc)                    #Draw row of 3 windows
    fillcolor(fc)
    begin_fill()
    go_down(35)
    rectangle(30, 30, "black", "white")
    go_down(30)
    go_left(45)
    rectangle(30, 30, "black", "white")
    go_down(30)
    go_right(90)
    rectangle(30, 30, "black", "white")
    end_fill()
    go_left(45)
    go_up(5)
    
def bank_logo():

    pencolor("dark blue")               #Draw ANZ logo
    fillcolor("deep sky blue")
    go_left(7.5)
    begin_fill()
    left(45)                        #Draw two angles semicircles
    circle(10, 180)
    left(90)
    forward(20)
    end_fill()
    left(45)
    pu()
    go_right(15)
    left(45)
    begin_fill()
    forward(20)
    left(90)
    circle(10, 180)
    end_fill()
    left(45)
    go_left(7.5)
    pu()
    go_up(15)
    begin_fill()                #Draw 2 circles 
    circle(12)
    end_fill()
    fillcolor("dark blue")
    go_down(2)
    begin_fill()
    circle(5)
    end_fill()

#STYLE D SHAPES
def panel_row_d(l, h, pc, fc):      #Draw pizzaria level decor
 
    for row in range (10):
        rounded_square(l, h, pc, fc)
        go_right(l)
        go_down(h)

def mushroom(x, pc, fc):
    pd()
    pencolor(pc)
    fillcolor(fc)
    begin_fill()
    forward(x)              #Draw right side
    left(90)
    forward(x*2)        
    right(90)
    forward(x)
    left(90)
    circle(x*2, 180)        #Draw head of mushroom
    left(90)
    forward(x)              #Draw left side
    right(90)
    forward(x*2)
    left(90)
    forward(x)
    end_fill()

#CONTRUCTION SHAPES

def crane_sec(x, pc):
    go_left(15)                                 #DRAW LEFT END
    go_up(2.5)
    right(50)
    rectangle(5, 40, pc, 'medium turquoise')
    go_down(42.5)
    go_right(32.5)
   
    for height_of_crane in range(x):                #DRAW MIDDLE BAR
        go_up(2.5)
        right(50)
        rectangle(5, 40, pc, 'dark cyan')
        go_down(40)
        left(50)
        go_down(2.5)
        rectangle(5, 30, pc, 'medium turquoise')
        go_right(2.5)
        go_down(2.5)
        right(90)
        rectangle(5, 25, pc, 'medium turquoise')
        go_right(2.5)
        go_up(2.5)
        go_down(30)
        rectangle(5, 30, pc, 'medium turquoise')
        go_down(30)

    go_right(32.5)                          #DRAW RIGHT END
    go_up(2.5)
    left(50)
    rectangle(5, 40, pc, 'medium turquoise')



#-------BUILDINGS------------------------------------------------------#
#STYLE A (OBSERVATORY)
def style_a(site, levels, construction):
    pu()
    setheading(0)
    pensize(1)
    pencolor("black")

    xcord = sites[site-1][1][0]
    ycord = sites[site-1][1][1]

    goto(xcord, ycord)

    rectangle(200, 60, "black", "cadet blue")           ##BOTTOM LEVEL
    door(40, 60, "black", "pale turquoise", "black", "white smoke",2)
    door(40, 60, "black", "pale turquoise", "black", "white smoke",1)
    
    for amount_of_floors in range (levels - 1):
        rectangle(200, 20, "black", "pale turquoise")       ##LEVELS
        rectangle(220, 10, "black", "dark cyan")

    if construction == 'X':                     ##MEN AT WORK
        go_down(((levels - 1)*30)+60)
        go_right(60)
        sign()
        go_left(30)
        sand()
        go_left(70)
        crane(levels + 1, "black")

    else:
        quadrant(110, 110, "black", "dark slate gray")      ##ROOF STRUCTURE
        semi_circle(100, 100,"black", "cadet blue")
        telescope()

#STYLE B (HOTEL)
def style_b(site, levels, construction):
    pu()
    setheading(0)
    pensize(1)
    pencolor("black")

    xcord = sites[site-1][1][0]
    ycord = sites[site-1][1][1]

    goto(xcord, ycord)

    rectangle(190, 10, "black", "sienna")                ##GROUND FLOOR
    rectangle(160, 80, "black", "antique white")
    go_down(75)
    go_left(35)
    rectangle(10, 20, "black", "alice blue")
    go_down(20)
    go_right(70)
    rectangle(10, 20, "black", "alice blue")
    go_down(20)
    go_left(35)
    go_up(55)
    door(20, 60, "black", "sienna", "alice blue", "alice blue",2)
    door(20, 60, "black", "sienna", "alice blue", "alice blue",1)
    go_up(5)
    rectangle(100, 5, "black", "sienna")
    go_up(10)

    for amount_of_floors in range(levels - 1):
        rectangle(160, 40, "black", "sienna")      ##LEVELS
        window_row_b("black", "alice blue")

    if construction == 'X':                     ##MEN AT WORK
        go_down(((levels - 1)*40)+90)
        go_right(60)
        sign()
        go_left(30)
        sand()
        go_left(70)
        crane(levels + 5, "black")

    else:
        rectangle(190, 10, "black", "sienna")
        roof_style_b()                          ##ROOF STRUCTURE

#STYLE C (BANK)
def style_c(site, levels, construction):
    pu()
    setheading(0)
    pensize(1)
    pencolor("black")

    xcord = sites[site-1][1][0]
    ycord = sites[site-1][1][1]

    goto(xcord, ycord)
    
    rectangle(180, 10, "black", "light blue")                ##GROUND FLOOR
    rectangle(170, 7, "black", "light blue")
    rectangle(165, 5, "black", "light blue")
    rectangle(155, 85, "black", "cornflower blue")
    go_down(25)
    door(20, 60, "black", "midnight blue", "black", "alice blue",2)
    door(20, 60, "black", "midnight blue", "black", "alice blue",1)
    go_down(60)
    go_left(30)
    rectangle(2, 67, "black", "midnight blue")
    go_down(67)
    go_right(60)
    rectangle(2, 67, "black", "midnight blue")
    go_left(30)
    rectangle(75, 2, "black", "midnight blue")
    go_up(5)
    rectangle(90, 2, "black", "midnight blue")
    go_up(9)

    for amount_of_floors in range(levels - 1):
        rectangle(155, 40, "black", "cornflower blue")      ##LEVELS
        window_row_c("black", "alice blue")
        
    if construction == 'X':                     ##MEN AT WORK
        go_down(((levels - 1)*40)+107)
        go_right(60)
        sign()
        go_left(30)
        sand()
        go_left(70)
        crane(levels + 5, "black")
    else:
        rectangle(165, 5, "black", "light blue")        ##ROOF STRUCTURE
        rectangle(170, 7, "black", "light blue")
        triangle(160, 50, "black", "dark blue")
        go_up(2)
        bank_logo()
    
#STYLE D (PIZZARIA)
def style_d(site, levels, construction):
    pu()
    setheading(0)
    pensize(1)
    pencolor("black")

    xcord = sites[site-1][1][0]
    ycord = sites[site-1][1][1]

    goto(xcord, ycord)

    
    rectangle(100, 5, "black", "dark red")          ##GROUND FLOOR
    rectangle(90, 60, "black", "moccasin")
    go_left(25)
    go_down(60)
    door(20, 40, "black", "medium sea green", "black", "light yellow",1)
    go_right(30)
    rectangle(40, 3, "black", "medium sea green")
    go_down(30)
    rectangle(40, 25, "black", "light yellow")
    go_down(30)
    rectangle(40, 3, "black", "medium sea green")
    go_up(49)
    go_left(15)
    go_left(45)
    go_down(5)
    panel_row_d(10, 10, "black", "red")
    go_left(55)
    go_up(10)

    for amount_of_floors in range(levels - 1):
        rectangle(90, 30, "black", "moccasin")          ##LEVELS
        go_down(25)
        rectangle(80, 5, "black", "medium sea green")      
        rectangle(70, 20, "black", "light yellow")
        go_left(45)
        panel_row_d(10, 10, "black", "red")
        go_left(55)
        go_up(10)
        
    if construction == 'X':                     ##MEN AT WORK
        go_down(((levels - 1)*40)+70)
        go_right(60)
        sign()
        go_left(30)
        sand()
        go_left(70)
        crane(levels + 5, "black")

    else:
        go_up(26)                                   ##ROOF STRUCTURE
        left(70)
        pensize(3)
        pencolor("peru")
        fillcolor("navajo white")
        begin_fill()
        forward(25)
        left(90)
        circle(25, 300)
        left(90)
        forward(25)
        end_fill()


        pencolor("peru")
        pensize(1)
        right(60)

        for pizza_slice in range(5):
            forward(23)
            go_left(6)
            go_down(6)
            dot(4, "red")
            go_left(5)
            go_down(8)
            mushroom(1.5, "dark gray", "dark gray")
            pencolor("peru")
            go_left(5)
            go_up(10)
            rectangle(3, 1, "dark green", "dark green")
            pencolor("peru")
            go_up(4)
            go_left(7)
            left(60)

#CONSTRUCTION

def crane (height, pc):
    rectangle(50, 5, pc, 'grey')            #DRAW BASE
    rectangle(50, 5, pc, 'dim grey')
    rectangle(50, 5, pc, 'grey')
    rectangle(50, 5, pc, 'dim grey')
    rectangle(50, 5, pc, 'grey')
    rectangle(50, 5, pc, 'dim grey')

    for height_of_crane in range(height):           #DRAW HEIGHT PANNELS
        go_left(15)
        go_up(2.5)                          
        right(50)
        rectangle(5, 40, pc, 'dark cyan')
        go_down(40)
        left(50)
        go_down(2.5)
        rectangle(5, 30, pc, 'medium turquoise')
        go_right(2.5)
        go_down(2.5)
        right(90)
        rectangle(5, 25, pc, 'dark cyan')
        go_right(2.5)
        go_up(2.5)
        go_down(30)
        rectangle(5, 30, pc, 'medium turquoise')
        go_left(15)
        
    go_right(10)                            #DRAW CONTROL BOX
    rectangle(40, 50, pc, 'dark cyan')
    go_right(5)
    go_down(40)
    rectangle(30, 30, pc, 'medium turquoise')
    go_up(10)
    go_right(40)
    
    go_left(122.5)                            #DRAW HORIZONTAL PANNELS
    crane_sec(7, pc)
    setheading(0)
    go_down(30)
    go_left(107.5)
    rectangle(277.5, 5, pc, 'medium turquoise')

    go_right(randint(10, 80))                           #DRAW HOOK
    go_down(65)
    rectangle(2, 60, pc, 'dim grey')
    go_down(55)
    left(90)
    stamp()

def sign():                              #DRAWS CONSTRUCTION SIGN
    go_up(25)
    go_right(3)
    right(90)
    rectangle(5, 5, "black", "red")
    rectangle(5, 5, "black", "white")
    rectangle(5, 5, "black", "red")
    rectangle(5, 5, "black", "white")
    rectangle(5, 5, "black", "red")
    rectangle(5, 5, "black", "white")
    left(90)
    go_down(25)
    rectangle(3, 30, "black", "white")
    go_left(30)
    go_down(30)
    rectangle(3, 30, "black", "white")
    go_down(30)

def sand():
    semi_circle(10, 5, "black", "tan")          #SMALL SAND PILE
    go_left(15)
    semi_circle(30, 15, "black", "tan")         #BIG SAND PILE

    
#-----Student's Solution---------------------------------------------#
        
# Erect buildings as per the provided city plan

def build_city(plan):
    
    list_pos = 0  #[0]
    
    for entry in range(len(plan)):
        if plan[list_pos][1] == "A":
            style_a(plan[list_pos][0], plan[list_pos][2], plan[list_pos][3])   

        if plan[list_pos][1] == "B":
            style_b(plan[list_pos][0], plan[list_pos][2], plan[list_pos][3])

        if plan[list_pos][1] == "C":
            style_c(plan[list_pos][0], plan[list_pos][2], plan[list_pos][3])

        if plan[list_pos][1] == "D":
            style_d(plan[list_pos][0], plan[list_pos][2], plan[list_pos][3])

        list_pos = list_pos + 1     #GO THROUGH PLAN LIST

    
 #--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# building your city.  Do not change any of this code except
# as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
# ***** Change the default argument to False if you don't want to
# ***** display the coordinates and building sites
create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with your name and/or a description of
# ***** your city
title("LIAM PEAKMAN // CITY (OBSERVATORY, HOTEL, BANK, PIZZARIA)")

### Call the student's function to build the city
### ***** While developing your program you can call the build_city
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_plan()" as the
### ***** argument to the build_city function.  Your program must
### ***** work for any data set that can be returned by the
### ***** random_plan function.
#build_city(fixed_plan_27) # <-- used for code development only, not marking
build_city(random_plan()) # <-- used for assessment

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas()

#
#--------------------------------------------------------------------#

