import turtle

class Timer:
    def __init__(self, width, height, position, duration=60, color="black"):
        """
        Timer paddle to display countdown time.
        :param width: Width of the paddle (not visually used here, for structure).
        :param height: Height of the paddle (not visually used here, for structure).
        :param position: Tuple for the timer's position (x, y).
        :param duration: Countdown duration in seconds.
        :param color: Timer text color.
        """
        self.width = width
        self.height = height
        self.position = position
        self.duration = duration
        self.time_left = duration
        self.color = color
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.goto(position)
        self.turtle.color(color)
        self.turtle.write(f"Time: {self.time_left}", align="center", font=("Arial", 16, "normal"))

    def update(self):
        """Update the timer display and decrement time."""
        if self.time_left > 0:
            self.time_left -= 1
            self.turtle.clear()
            self.turtle.write(f"Time: {self.time_left}", align="center", font=("Arial", 16, "normal"))
            turtle.ontimer(self.update, 1000)  # Call this method again after 1 second
        else:
            self.turtle.clear()
            self.turtle.write("Time: 0", align="center", font=("Arial", 16, "normal"))
            print("Game Over!")  # Optional: Can trigger an event for game end
