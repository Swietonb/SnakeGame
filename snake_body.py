from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
HEAD_COLOR = 'red'
BODY_COLOR = 'green'


class Snake:
    def __init__(self):
        self.segments = []
        self.create_starting_segments()
        self.head = self.segments[0]

    def create_segment(self, position, color):
        segment = Turtle()
        segment.color(color)
        segment.shape('square')
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.create_segment(self.segments[-1].position())

    def create_starting_segments(self):
        self.create_segment(STARTING_POSITIONS[0], HEAD_COLOR)
        for position in STARTING_POSITIONS[1:]:
            self.create_segment(position, BODY_COLOR)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_pos = self.segments[seg_num - 1].position()
            self.segments[seg_num].goto(new_pos)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
