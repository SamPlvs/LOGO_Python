import sys, os, math, random, functools
import matplotlib.pyplot as pp

# Go to line 99 onwards to play around with it.

# defining the two classes:
class Turtle(object):
      # before the init function define the class attributes which are common to all instances i.e. like a global variable
      deg = math.pi/180.0
      # every class needs to begin with an initializer! this is to state all the variables the following methods will use:
      def __init__(self,Terrarium):
            self.pos = (0,0) # start with the initial position of the origin
            self.angle = 0 
            self.pen= True # pen to down!
            self.axes= Terrarium.axes
      '''at first instance just state the functions (i.e. methods) and fill them with pass so that they are python legal
        fill the methods with the relevant instructions later
        note all methods( functions) take their first argument as 'self ' this is to refer back to the instnce of which we call a method'''
      def forward(self,distance): # forward movement
            new_position= (self.pos[0] + distance* math.cos(self.deg*self.angle),
                           self.pos[1] + distance * math.sin(self.deg*self.angle))
            '''Using trignometry, [0] is the x coordinate and [1] is the y coordinate if the angle is in degrees I multiply by a constant
             defined by the class attribute deg to turn it into radians.'''
            if self.pen: # if pen is down we will draw
                  Line= pp.Line2D((self.pos[0],new_position[0]),(self.pos[1],new_position[1])) 
                  self.axes.add_line(Line)
                  
            self.pos= new_position
            
      def back(self,distance):
            self.forward(-distance)
            
      def left(self,angle): # moving to the left at an angle
            self.angle = (self.angle + angle) % 360 # I may want to input a new angle so I replace the original
            
      def right(self,angle): # moving to the right at an angle
            self.angle = (self.angle - angle) % 360
            
      def pen_on(self):
            self.pen = True # I want to draw the trajectory
            
      def pen_off(self):
            self.pen = False     # I don't want to draw the trajectory


class Terrarium(object): # Remember the turtle must be taught to draw!!
      def __init__(self):
            # Now to actually implement the drawing:
            self.figure = pp.figure(figsize=(10,10))
            self.axes= pp.axes()
           
            # to get rid of the axis lines:
            self.axes.set_xticks([])
            self.axes.set_yticks([])

            for spine in ['bottom','top','left','right']:
                  self.axes.spines[spine].set_color('0.9') # this is the line that will be drawn with the pen


            # Putting the rescaling in a separate method:
      def rescale(self):
            self.axes.axis('scaled')

            xmin,xmax,ymin,ymax = self.axes.axis()
            dx= (xmax - xmin)/50
            self.axes.axis([xmin-dx,xmax+dx,ymin-dx,ymax+dx])

#%%
T= Terrarium()

turtle1= Turtle(T)# where the turtle lives


"""To define how the turtle moves just change the numbers in the sections below or add your own commands. 
The turtle will follow the commands sequentially, in order. Simply tell it which direction to go in and
when you hit run, you'll see a graph appear; displaying the turtle's trajectory.

Note, the turtle begins at the origin i.e. at (0,0) meaning the bottom left of the graph """

############### The following is where you input the commands to make the turtle move #################


turtle1.forward(100)
turtle1.left(90) #degrees
turtle1.forward(150)
turtle1.right(45) #degrees
turtle1.back(100)
turtle1.left(25)
turtle1.forward(50)
turtle1.left(45)

T.rescale()




