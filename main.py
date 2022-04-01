# %%

import random
import tkinter as tk
from turtle import bgcolor

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

        Returns:
            x0, y0, x1, y1: The space position of the bodies
        """
class Universe:
    """The class that emulates the universe and the physics laws and forces such as gravity."""
    def __init__(self) -> None:
        self.bodies = []
    
    def __iter__(self):
        return iter(self.bodies)

   
    def random_big_bang(self, number_of_bodies):
        """A function to fill the bodies list with CelestialBody objects with randomly chosen parameters
        """
        for index in range(number_of_bodies):
            mass = random.randint(1, 100)
            radius = random.randint(1, 100)
            x, y = random.randint(1,100) * random.random(), random.randint(1,100) * random.random()
            self.bodies.append(CelestialBody(mass, radius, x, y))

# %%
universe = Universe()
universe.random_big_bang(10)

for body in universe:
    print(body)
# %%

# Visualize
mainWindow = tk.Tk()
mainWindow.title("Gravitation simulation")
mainWindow.geometry("800x800")

canvas = tk.Canvas(mainWindow, width=800, height=800, bg="ivory")
canvas.pack()

for body in universe:
    body.figure = canvas.create_oval()

mainWindow.mainloop()
# %%
