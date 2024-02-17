import turtle
import time
from math import *
import random

win = turtle.Screen()
win.setup(1500,1500)
win.bgcolor('black')
win.tracer(0)

sun = turtle.Turtle()
sun.shape('circle')
sun.shapesize(5)
sun.color('yellow')

class Planet(turtle.Turtle):
    def __init__(self,radius, color, size, star):
        super().__init__(shape='circle')
        self.radius = radius
        self.c = color
        self.color(self.c)
        self.size = size
        self.shapesize(size,size)
        self.up()
        self.angle = 0
        self.star = star

    def move(self):
        x = self.radius*cos(self.angle) # Angle in radians
        y = self.radius*sin(self.angle) 

        self.goto(self.star.xcor()+x,self.star.ycor()+y)

earth = Planet(300,'blue', 1, sun)
mercury = Planet(110, 'grey', 0.6, sun)
venus = Planet(180, 'orange', 0.8, sun)
mars = Planet(500, 'red', 0.9, sun)

moon = Planet(40, 'grey', 0.2, earth) 
phobos = Planet(40, 'grey', 0.2, mars)
deimos = Planet(35, 'white', 0.2, mars)

stars = []
angle = 1

for i in range(1200):
    star = Planet(random.randint(90, 1000), 'grey', 0.01, sun)  # Scatter 1200 stars in radius 90-1000 all around the sun
    stars.append(star)
    star.angle += angle
    angle += 1 
    

PlanetList = [earth, mercury, venus, mars, moon, phobos, deimos]

while True:
    win.update()
    for i in PlanetList:
        i.move()
        
    for i in stars:
        i.move()
        i.angle += 0.0009

    # Increase the angle by x radians (further away - smaller angle change) for more natural visuals
    moon.angle += 0.06
    phobos.angle += 0.06
    deimos.angle += 0.08
    
    mercury.angle += 0.05
    venus.angle += 0.03
    earth.angle += 0.01
    mars.angle += 0.007

    time.sleep(0.01)