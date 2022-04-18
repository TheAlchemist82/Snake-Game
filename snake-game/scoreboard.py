from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("snake-game/data.txt" , "r") as f:
            self.high_score = int(f.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def point(self):
        self.score += 1
        self.update()

    def reset(self):
        if self.score >= self.high_score:
            self.high_score = self.score
            with open("snake-game/data.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.update()
    
