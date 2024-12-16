import turtle
import random

class Ball:
    def __init__(self, radius, color, boundary_width, boundary_height):
        self.radius = radius
        self.color = color
        self.x = 0
        self.y = 0
        self.vx = random.choice([-5, 5]) * 1  # Random horizontal direction
        self.vy = random.choice([-3, 3]) * 1   # Random vertical direction
        self.boundary_width = boundary_width
        self.boundary_height = boundary_height
        self.turtle = turtle.Turtle()
        self.turtle.penup()
        self.turtle.shape("circle")
        self.turtle.shapesize(stretch_wid=radius/10, stretch_len=radius/10)
        self.turtle.fillcolor(color)

    def move(self):
        self.x += self.vx
        self.y += self.vy

        # Bounce off vertical boundaries
        if abs(self.x) > self.boundary_width / 2 - self.radius:
            self.vx = -self.vx

        # Bounce off horizontal boundaries
        if abs(self.y) > self.boundary_height / 2 - self.radius:
            self.vy = -self.vy

        self.turtle.goto(self.x, self.y)

    def bounce_vertical(self):
        self.vx = -self.vx

    def bounce_horizontal(self):
        self.vy = -self.vy


    def curve(self, direction):
        if direction == "left":
            self.vx -= 1
        elif direction == "right":
            self.vx += 1