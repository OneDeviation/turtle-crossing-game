from turtle import Turtle
from car import Car
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
CAR_SIZES = [2, 3]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:


    def __init__(self):
        self.cars_speed = .001
        self.cars = []
        self.create_cars()

    def create_cars(self):
        for _ in range(20):
            new_car = Car()
            new_car.shape("square")
            new_car.penup()
            new_car.setheading(180)
            new_car.resizemode("user")
            self.car_placement(new_car, -245, 360)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(car.car_speed)
            if car.xcor() < -350:
                self.car_placement(car, 340, 380)


    def car_placement(self, car, start, stop):
        rand_x = random.randint(start, stop)
        rand_y = random.randrange(-250, 270, 30)
        car.color(random.choice(COLORS))
        car.shapesize(stretch_wid=1, stretch_len=random.choice(CAR_SIZES))
        car.set_speed()
        car.goto(rand_x, rand_y)
        for other_car in self.cars:
            if other_car == car:
                pass
            if other_car.ycor() == car.ycor() and other_car.xcor() > 0:
                car.car_speed = other_car.car_speed
                if car.distance(other_car) <= 60:
                    car.goto(car.xcor()+90, car.ycor())

    def speed_up(self):
        for car in self.cars:
            car.increment_speeds()
            car.set_speed()

