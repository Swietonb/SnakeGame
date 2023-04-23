from turtle import Turtle

SCORE_FONT = ("Arial", 20, "normal")
ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align=ALIGN, font=SCORE_FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGN, font=SCORE_FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGN, font=SCORE_FONT)