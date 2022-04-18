from turtle import Turtle
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT  = 0

class Snake:
    def __init__(self):
        self.all_turts = []
        self.create_snake()
    def create_snake(self):
        x = 0
        for i in range(0,3):
            tim = Turtle(shape = "square")
            tim.color("white")
            tim.pu()
            tim.goto(x, 0)
            self.all_turts.append(tim)
            x += -20
    def move(self):
        for seg in range(len(self.all_turts) - 1, 0, -1):
            x = self.all_turts[seg - 1].xcor()
            y = self.all_turts[seg - 1].ycor()
            self.all_turts[seg].goto(x, y)
        self.all_turts[0].forward(MOVE_DIST)

    def up(self):
        if self.all_turts[0].heading() != DOWN:
            self.all_turts[0].setheading(UP)

    def left(self):
        if self.all_turts[0].heading() != RIGHT:
            self.all_turts[0].setheading(LEFT)
    def right(self):
        if self.all_turts[0].heading() != LEFT:
            self.all_turts[0].setheading(RIGHT)
    def down(self):
        if self.all_turts[0].heading() != UP:
            self.all_turts[0].setheading(DOWN)

    def add(self):
        tim = Turtle(shape = "square")
        tim.goto(self.all_turts[-1].position())
        tim.color("white")
        tim.pu()
        self.all_turts.append(tim)

    def reset(self):
        for seg in self.all_turts:
            seg.goto(1000 , 1000)
        self.all_turts.clear()
        self.create_snake()
        self.head = self.all_turts[0]