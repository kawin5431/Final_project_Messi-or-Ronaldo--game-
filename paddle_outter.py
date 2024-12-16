import turtle

class Outter:
    def __init__(self, width, height, color="black"):
        self.width = width
        self.height = height
        self.color = color
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.goto(-width/2, height/2)
        self.turtle.pendown()
        self.turtle.pensize(5)
        self.turtle.color(color)
        for _ in range(2):
            self.turtle.forward(width)
            self.turtle.right(90)
            self.turtle.forward(height)
            self.turtle.right(90)
