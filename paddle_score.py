import turtle

class Score:
    def __init__(self, position, color="black"):
        self.score = 0
        self.position = position
        self.color = color
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.goto(position)
        self.turtle.color(color)
        self.turtle.write(f"Score: {self.score}", align="center", font=("Arial", 16, "normal"))

    def update(self, score):
        self.score = score
        self.turtle.clear()
        self.turtle.write(f"Score: {self.score}", align="center", font=("Arial", 16, "normal"))
