# %%

import random
import tkinter as tk
import numpy as np

# %%

class CelestialBody:
    """The base class to define a celestial body in order to
    make a gravitation simulation.
    """
    def __init__(self, mass, radius, x, y) -> None:
        if radius <= 0:
            raise ValueError("The radius can't be zero or negative")
        if mass <= 0:
            raise ValueError("The mass can't be zero or negative")
        self.mass = mass
        self.radius = radius
        self.x = x
        self.y = y
        self.x_speed = 0
        self.y_speed = 0
    
    def __str__(self) -> str:
        return f"Celestial body of mass {self.mass}kg, radius {self.radius}m and position ({self.x},{self.y})"

    def move(self):
        """The function to move the celestial body
        """
        self.x += self.x_speed
        self.y += self.y_speed

    def bbox(self):
        """Function to return the bbox of the celestial body.
        (x0, y0) is the top left corner and (x1, y1) is the bottom right.
        Returns:
            x0, y0, x1, y1: The space position of the bodies
        """
        return self.x-self.radius, self.y-self.radius,  self.x+self.radius, self.y+self.radius
class Universe:
    """The class that emulates the universe and the physics laws and forces such as gravity."""
    def __init__(self, size) -> None:
        self.bodies = []
        if size <= 0:
            raise ValueError("Universe size should not be 0 or a negative number")
        self.size = size
    
    def __iter__(self):
        return iter(self.bodies)

   
    def random_big_bang(self, number_of_bodies):
        """A function to fill the bodies list with CelestialBody objects with randomly chosen parameters
        """
        for index in range(number_of_bodies):
            mass = random.randint(1, 100)
            radius = random.randint(1, 20)
            x, y = random.randint(radius,self.size-2*radius) * random.random() + radius, random.randint(radius,self.size-2*radius) * random.random() + radius
            self.bodies.append(CelestialBody(mass, radius, x, y))

# %%
universe = Universe(400)
universe.random_big_bang(100)

for body in universe:
    print(body)
# %%

# Visualize
mainWindow = tk.Tk()
mainWindow.title("Gravitation simulation")
mainWindow.configure(width=universe.size, height=universe.size)

canvas = tk.Canvas(mainWindow, width=universe.size, height=universe.size, bg="ivory")
canvas.pack()

for body in universe:
    x0, y0, x1, y1 = body.bbox()
    body.figure = canvas.create_oval(x0, y0, x1, y1, fill="red")

mainWindow.mainloop()
# %%
