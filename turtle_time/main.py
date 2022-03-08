import turtle
from datetime import datetime
import random

# Current Time
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
current_hour = int(now.strftime("%H"))
current_minute = int(now.strftime("%M"))
clock_hour = current_hour + (current_minute/200)
clock_minute = current_minute
turtle.colormode(255)


# Screen and Turtle
screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor('black')
t = turtle.Turtle()
t.hideturtle()
t.speed("fastest")


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_colour = (r, g, b)
    return rand_colour


# Clock Dial

def lined_hour(time):
      t.pencolor(random_colour())
      t.pensize(10)
      t.penup()
      t.setheading(-30 * time + 90)
      t.forward(180)
      t.pendown()
      t.forward(25)
      t.penup()
      t.forward(20)
      t.home()


def number_hour(time):
      t.pencolor(random_colour())
      t.penup()
      t.setheading(-30 * time + 90)
      t.forward(220)
      t.write(str(time), align="center", font=("Arial", 35, "bold"))
      t.home()


def midnight():
      t.pencolor(random_colour())
      t.penup()
      t.setheading(-30 * 12 + 90)
      t.forward(150)
      t.write('七転び八起き', align="center", font=("Arial", 12, "bold"))
      t.forward(20)
      t.write('RUNNINGFOK', align="center", font=("Arial", 18, "bold"))
      t.home()


def drawing_bezel():
      t.setpos(0, -240)
      t.pendown()
      t.pensize(15)
      t.pencolor(random_colour())
      t.circle(250)
      t.penup()


# Hour and Minute Hands

def time_now(hour):
      t.pencolor(random_colour())
      t.pensize(10)
      if hour > 12:
            hour -= 12
      t.penup()
      t.setheading(-30 * hour + 90)
      t.pendown()
      t.forward(100)
      t.penup()
      t.home()
      t.pencolor(random_colour())
      t.pensize(8)
      t.setheading( -6 * clock_minute + 90)
      t.pendown()
      t.forward(160)
      t.penup()
      t.home()


# Badly Designed Run-down

lined_hour(1)
lined_hour(2)
number_hour(3)
lined_hour(4)
lined_hour(5)
number_hour(6)
lined_hour(7)
lined_hour(8)
number_hour(9)
lined_hour(10)
lined_hour(11)
midnight()
time_now(clock_hour)
drawing_bezel()
# Exit On Click
screen.exitonclick()


