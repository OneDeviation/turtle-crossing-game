from turtle import Turtle
from car import Car
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
CAR_SIZES = [2, 2.5, 3]
STARTING_MOVE_DISTANCE = 5
MAX_CARS = 30
CAR_START_X_RANGE = (300, 340)
CAR_START_Y_RANGE = (-250, 250)
CAR_START_Y_STEP = 30

class CarManager:


    def __init__(self):
        self.cars = []
        self.max_cars = MAX_CARS

    def create_car(self):
        if random.randint(1, 6) == 1:
            new_car = Car()
            new_car.shape("square")
            new_car.penup()
            new_car.setheading(180)
            new_car.resizemode("user")
            self.car_placement(new_car)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(car.car_speed)
            if car.xcor() < -350:
                self.car_placement(car)

    def car_placement(self, car):
        rand_x = random.randint(CAR_START_X_RANGE[0], CAR_START_X_RANGE[1])
        rand_y = random.randrange(CAR_START_Y_RANGE[0], CAR_START_Y_RANGE[1], CAR_START_Y_STEP)
        car.color(random.choice(COLORS))
        car.shapesize(stretch_wid=1, stretch_len=random.choice(CAR_SIZES))
        car.set_speed()
        car.goto(rand_x, rand_y)
        for other_car in self.cars:
            if other_car == car:
                pass
            if other_car.ycor() == car.ycor() and other_car.xcor() > 0:
                car.car_speed = other_car.car_speed

    def speed_up(self):
        for car in self.cars:
            car.increment_speeds()
            car.set_speed()

    def car_count(self):
        return len(self.cars)
