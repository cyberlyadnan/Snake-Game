from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()  # Initialize the parent class (Turtle)
        self.shape("circle")  # Set the shape of the food to a circle
        self.penup()  # Lift the pen up to avoid drawing lines
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Set the size of the food
        self.color("blue")  # Set the color of the food
        self.speed("fastest")  # Set the animation speed of the food
        self.refresh()  # Call the refresh method to randomly position the food

    def refresh(self):
        # Generate random coordinates for the food
        random_x = random.randint(-270, 270)
        random_y = random.randint(-260, 260)
        self.goto(random_x, random_y)  # Move the food to the random coordinates
