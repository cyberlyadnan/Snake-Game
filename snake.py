from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []  # Initialize an empty list to store the segments of the snake
        self.create_snake()  # Call the method to create the initial snake
        self.head = self.segments[0]  # Set the head of the snake as the first segment

    def create_snake(self):
        # Create the segments of the snake using the starting positions
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("circle")  # Create a new turtle segment
        new_segment.color("gold")  # Set the color of the segment
        new_segment.penup()  # Lift the pen up to avoid drawing lines
        new_segment.goto(position)  # Move the segment to the given position
        self.segments.append(new_segment)  # Add the segment to the list of segments

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        # Move each segment of the snake to the position of the previous segment
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)  # Move the head of the snake forward by the move distance

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
