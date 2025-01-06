import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(cars.cars_speed)
    screen.update()

    #move cars
    cars.move_cars()
    #detect collision with a car - game over
    for car in cars.cars:
        if player.distance(car) < 20 and car.ycor() - 15 <= player.ycor() <= car.ycor() + 15:
            game_is_on = False
            scoreboard.game_over()

    #detect crossing finish line - increment score - reset to next level w/ faster cars
    if player.crossed_safe():
        scoreboard.next_level()
        cars.speed_up()

screen.exitonclick()