from turtle import Turtle
import random

STARTING_CAR_SPEEDS = [3,4,5,6,7]
CAR_SPEED_INCREMENT = 2

class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.car_speeds = STARTING_CAR_SPEEDS.copy()
        self.car_speed = random.choice(self.car_speeds)

    def set_speed(self):
        self.car_speed = random.choice(self.car_speeds)

    def increment_speeds(self):
        for item in range(0, len(self.car_speeds)):
            self.car_speeds[item] += CAR_SPEED_INCREMENT


