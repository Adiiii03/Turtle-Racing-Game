from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet!", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-80, -40, -0, 40, 80, 120]
all_turtles = []

for i in range(6):
    new_tim = Turtle("turtle")
    new_tim.color(colors[i])
    new_tim.penup()
    new_tim.goto(x=-230, y=y_pos[i])
    all_turtles.append(new_tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if user_bet == winner:
                print("You win!")
                screen.exitonclick()

            else:
                print(f"You Lose. The winner is {winner}.")
                screen.exitonclick()
        dist = random.randint(0, 10)
        turtle.forward(dist)
