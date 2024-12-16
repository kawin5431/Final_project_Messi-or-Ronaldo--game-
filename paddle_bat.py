import turtle

class Bat:
    def __init__(self, width, height, position, boundary_width, boundary_height, color="blue"):
        self.width = width
        self.height = height
        self.position = position
        self.color = color
        self.boundary_width = boundary_width
        self.boundary_height = boundary_height
        self.turtle = turtle.Turtle()
        self.turtle.shape("square")
        self.turtle.shapesize(stretch_wid=height/20, stretch_len=width/20)
        self.turtle.color(color)
        self.turtle.penup()
        self.turtle.goto(position)

    def move(self, x, y):
        new_x = self.position[0] + x
        new_y = self.position[1] + y

        half_height = self.height / 2
        if -self.boundary_height / 2 + half_height <= new_y <= self.boundary_height / 2 - half_height:
            self.position = [new_x, new_y]
            self.turtle.goto(self.position)

    def tilt(self, direction):
        if direction == "up":
            self.turtle.settiltangle(30)
        elif direction == "down":
            self.turtle.settiltangle(-30)
        else:
            self.turtle.settiltangle(0)

    def check_collision(self, ball):
        if (self.position[0] - self.width / 2 <= ball.x <= self.position[0] + self.width / 2 and
                self.position[1] - self.height / 2 <= ball.y <= self.position[1] + self.height / 2):
            ball.vx = -ball.vx
            relative_hit_position = (ball.y - self.position[1]) / (self.height / 2)
            ball.vy += relative_hit_position * 5
            return True
        return False