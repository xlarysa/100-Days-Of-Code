import turtle as t

STARTING_POSITIONS = [(0, 0), (-21, 0), (-41, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.color_counter = 0
        self.body = []
        self.create_body()
        self.head = self.body[0]
        self.last_direction = self.head.heading()

    def create_body(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    def add_segment(self, position):
        seg = t.Turtle("square")
        if self.color_counter % 4 == 0:
            seg.color("LightGoldenrod3")
        else:
            seg.color("DarkSeaGreen4")
        self.color_counter += 1
        seg.penup()
        seg.goto(position)
        self.body.append(seg)

    def extend(self):
        self.add_segment(self.body[-1].position())

    def move(self):
        for seg in range(len(self.body) - 1, 0, -1):
            self.body[seg].goto(self.body[seg - 1].xcor(), self.body[seg - 1].ycor())
        self.body[0].forward(MOVE_DISTANCE)
        self.last_direction = self.head.heading()

    def reset(self):
        for seg in self.body:
            seg.goto(1000,1000)
        self.body.clear()
        self.color_counter = 0
        self.create_body()
        self.head = self.body[0]

    def up(self):
        if not self.last_direction == DOWN:
            self.head.setheading(UP)

    def down(self):
        if not self.last_direction == UP:
            self.head.setheading(DOWN)

    def left(self):
        if not self.last_direction == RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if not self.last_direction == LEFT:
            self.head.setheading(RIGHT)