###############################################
# Programmer: Feng Zhang
# Date: 2021-10-13
# Purpose: To create a ball animation that 
#          bounces off walls and changes colors 
###############################################

#Initialize Tkinter with these
from tkinter import*
from random import *
import time
myInterface = Tk()
screen = Canvas( myInterface, width=600, height=600, background="black")
myInterface.title('Rainbow Target')
screen.pack()

#Choose a random speed for a ball
xSpeed = randint(-6, 6)
ySpeed = randint(-6, 6)

#Make sure the speed isn't 0 or 1
while xSpeed in range(-1, 2) or ySpeed in range(-1,2):
  xSpeed = randint(-6, 6)
  ySpeed = randint(-6, 6) 

#Where the ball spawns 
y = randint(0, 575)
x = randint(0, 575)

#Centre of all the circles
circleX = 300
circleY = 300


#Draws the target
for circle in range(1, 7):
  radius = circle*50
  screen.create_oval(circleX-radius, circleY-radius, circleX+radius, circleY+radius, fill='', outline='white', width=2.5)


#Animating the ball moving 
for frames in range(10000):

  #Moves the ball in a linear motion
  y += ySpeed
  x += xSpeed

  #Ball bounces off the wall and goes in the opposite direction
  if y <= 0:
    ySpeed = abs(ySpeed)

  if y+25 >= 600:
    ySpeed = -ySpeed

  if x+25 >= 600:
    xSpeed = -xSpeed
  
  if x <= 0:
    xSpeed = abs(xSpeed)
  
  #Coordinates of the center of the ball 
  centerX = (x + x+25)/2
  centerY = (y + y+25)/2

  #Equation for all the drawn circles 
  circEqn = (centerX-300)**2+(centerY-300)**2


  #Color of the ball in order of where it is in the circles, it is default grey 
  ballCOLOR = 'grey'
  colors = ['purple','blue','green','yellow','orange','red']


  #Changes the color of the ball according to the ring it is in
  for rings in range(6):
    if circEqn <= (300-rings*50)**2:
      ballCOLOR = colors[rings]
    

  
  #Draws the ball onto the screen 
  ball = screen.create_oval(x, y, x+25, y+25, fill=ballCOLOR)

  #Updates and waits before deleting the ball
  screen.update() 
  time.sleep(0.02)
  screen.delete(ball)

#END OF PROGRAM