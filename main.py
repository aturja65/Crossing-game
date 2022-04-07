import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle crossing game")
player = Player()
car = CarManager()
scoreboard = Scoreboard()
screen.tracer(0)
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()
    for cars in car.cars:
        if cars.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() == player.finish:
        player.start()
        scoreboard.score()
        car.speed_up()
screen.exitonclick()
