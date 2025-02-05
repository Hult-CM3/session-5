# import libraries
import time
from turtle import Screen
from turtle import Turtle

# classes here
class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        if side == "left":
            self.goto(-360,0)
        else:
            self.goto(360,0)
        self.color("white")
        self.shape("square")       
        self.shapesize(8, 1)
        self.penup()
    def up(self):
        """move paddle up"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    def down(self):
        """move paddle down"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
      
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0,0)  
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 5
        self.y_move = 5
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update()
    
    def update(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"{self.l_score} — {self.r_score}", align="center", font=("Helvetica", 32, "bold"))
    
    def reset(self):
        pass

# Set up the screen
screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600, startx=0, starty=0)
screen.tracer(0)

# Setup Scoreboard
scoreboard = Scoreboard()

# Setup the ball
ball = Ball()

# Create left and right paddles
r_paddle = Paddle("left")
l_paddle = Paddle("right")

# Screen listeners for updating
screen.update()
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "q")
screen.onkey(l_paddle.down, "a")

def main():
  game_on = True
  while game_on:
      ball.move()
      screen.update()

screen.exitonclick()

if __name__ == "__main__":
  main()

