from turtle import Turtle

FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-230,265)
        self.update_level()


    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def next_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="left", font=FONT)