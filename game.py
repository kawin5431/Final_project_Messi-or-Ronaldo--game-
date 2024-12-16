import turtle
import time
import random
from ball import Ball
from paddle_timer import Timer
from paddle_score import Score
from paddle_outter import Outter
from paddle_bat import Bat
from yellow_ball import YellowBall

class Game:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(width=800, height=600)
        self.screen.title("Messi or Ronaldo?")
        self.screen.bgcolor("white")

        self.p1_instructions = turtle.Turtle()
        self.p1_instructions.hideturtle()
        self.p1_instructions.penup()
        self.p1_instructions.goto(-200, -250)  
        self.p1_instructions.color("black")
        self.p1_instructions.write("W: Move Up\nS: Move Down", align="center", font=("Arial", 12, "normal"))


        self.p2_instructions = turtle.Turtle()
        self.p2_instructions.hideturtle()
        self.p2_instructions.penup()
        self.p2_instructions.goto(200, -250)
        self.p2_instructions.color("black")
        self.p2_instructions.write("↑: Move Up\n↓: Move Down", align="center", font=("Arial", 12, "normal"))

        self.screen.register_shape("IMG_3326.gif")
        self.screen.register_shape("IMG_3325.gif")
        self.screen.register_shape("IMG_3328.gif")
        self.screen.register_shape("IMG_3329-removebg-preview.gif")

        self.boundary_width = 800
        self.boundary_height = 400
        self.spawn_area = (-100, 100, -100, 100)

        self.timer = Timer(100, 50, position=(0, 260))
        self.score_left = Score(position=(-200, 260))
        self.score_right = Score(position=(200, 260))
        self.outter = Outter(self.boundary_width, self.boundary_height)
        self.ball = Ball(radius=10, color="white", boundary_width=self.boundary_width, boundary_height=self.boundary_height)
        self.yellow_balls = []
        self.bat_left = Bat(width=20, height=120, position=(0, 0), boundary_width=self.boundary_width, boundary_height=self.boundary_height, color="white")
        self.bat_right = Bat(width=20, height=120, position=(0, 0), boundary_width=self.boundary_width, boundary_height=self.boundary_height, color="white")

        self.bat_left.turtle.shape("IMG_3326.gif")
        self.bat_left.turtle.pensize(0) 
        self.bat_right.turtle.shape("IMG_3325.gif")
        self.bat_right.turtle.pensize(0)
        self.ball.turtle.shape("IMG_3328.gif")
        self.ball.turtle.pensize(0)


        self.animate_bat_to_position(self.bat_left, (-300, 0))
        self.animate_bat_to_position(self.bat_right, (300, 0))


        self.last_hit_by = None


        self.screen.listen()
        self.screen.onkeypress(lambda: self.bat_left.move(0, 70), "w")
        self.screen.onkeypress(lambda: self.bat_left.move(0, -70), "s")

        self.screen.onkeypress(lambda: self.bat_right.move(0, 70), "Up")
        self.screen.onkeypress(lambda: self.bat_right.move(0, -70), "Down")

    def animate_bat_to_position(self, bat, target_position):
        x, y = bat.position
        target_x, target_y = target_position
        steps = 50
        dx = (target_x - x) / steps
        dy = (target_y - y) / steps

        for _ in range(steps):
            x += dx
            y += dy
            bat.turtle.goto(x, y)
            time.sleep(0.01)

        bat.position = [target_x, target_y]
        bat.turtle.goto(target_x, target_y)

    def play(self):
        self.timer.update()
        self.spawn_yellow_ball()

        yellow_ball_spawn_time = time.time()

        start_time = time.time()
        while time.time() - start_time < 63:
            self.ball.move()

            if self.bat_left.check_collision(self.ball):
                print("Ball hit left bat!")
                self.last_hit_by = "left"
            if self.bat_right.check_collision(self.ball):
                print("Ball hit right bat!")
                self.last_hit_by = "right"

            for yellow_ball in self.yellow_balls[:]:
                if self.check_yellow_ball_collision(yellow_ball):
                    if self.last_hit_by == "left":
                        self.score_left.update(self.score_left.score + 1)
                    elif self.last_hit_by == "right":
                        self.score_right.update(self.score_right.score + 1)
                    self.increase_ball_speed()
                    self.show_speed_effect()
                    yellow_ball.hide()
                    self.yellow_balls.remove(yellow_ball)

            if time.time() - yellow_ball_spawn_time > 15:
                self.spawn_yellow_ball()
                yellow_ball_spawn_time = time.time()

            time.sleep(0.01)

        print("Game Over")
        self.show_winner()

    def spawn_yellow_ball(self):
        yellow_ball = YellowBall(boundary_width=self.boundary_width, boundary_height=self.boundary_height, spawn_area=self.spawn_area)
        yellow_ball.spawn()
        self.yellow_balls.append(yellow_ball)

    def check_yellow_ball_collision(self, yellow_ball):
        distance = ((self.ball.x - yellow_ball.x) ** 2 + (self.ball.y - yellow_ball.y) ** 2) ** 0.5
        return distance <= (self.ball.radius + yellow_ball.radius)

    def increase_ball_speed(self):
        original_vx = self.ball.vx
        original_vy = self.ball.vy
        self.ball.vx *= 2.25
        self.ball.vy *= 2.25
        self.screen.ontimer(lambda: self.reset_ball_speed(original_vx, original_vy), 1000)

    def reset_ball_speed(self, original_vx, original_vy):
        self.ball.vx = original_vx
        self.ball.vy = original_vy

    def show_speed_effect(self):
        effect = turtle.Turtle()
        effect.hideturtle()
        effect.penup()
        effect.goto(self.ball.x, self.ball.y)
        effect.color("red")
        effect.write("SPEED UP!", align="center", font=("Arial", 16, "bold"))
        self.screen.ontimer(effect.clear, 500)

    def show_trail_effect(self):
        trail = turtle.Turtle()
        trail.hideturtle()
        trail.penup()
        trail.goto(self.ball.x, self.ball.y)
        trail.color("purple")
        trail.pensize(5)
        trail.pendown()
        for _ in range(5):
            trail.goto(trail.xcor(), trail.ycor() - 30)
            trail.pendown()
        trail.clear()

    def show_winner(self):
        if self.score_left.score > self.score_right.score:
            winner_text = "Crying Penaldo!"
        elif self.score_left.score < self.score_right.score:
            winner_text = "Messi Robber Ronaldo Better!"
        else:
            winner_text = "Two Goat!"

        self.screen.clear()
        self.screen.bgcolor("white")
        message = turtle.Turtle()
        message.hideturtle()
        message.penup()
        message.color("black")
        message.write(winner_text, align="center", font=("Arial", 24, "bold"))
        time.sleep(10)


game = Game()
game.play()
