from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()  # Initialize the parent class (Turtle)
        self.score = 0  # Initialize the current score to 0
        self.highscore = 0  # Initialize the high score to 0
        self.read_score()  # Read the high score from a file
        self.color("yellow")  # Set the color of the scoreboard text
        self.penup()  # Lift the pen up to avoid drawing lines
        self.goto(0, 270)  # Position the scoreboard at the top center of the screen
        self.hideturtle()  # Hide the turtle icon
        self.update_scoreboard()  # Call the method to update the scoreboard text

    def update_scoreboard(self):
        self.clear()  # Clear any previous text on the scoreboard
        self.write(f" Score: {self.score}  High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)  # Move the turtle to the center of the screen
        self.write(">>>>>>   GAME OVER    <<<<<<", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1  # Increment the score by 1
        self.update_scoreboard()  # Call the method to update the scoreboard text

    def reset(self):
        if self.score > self.highscore:  # Check if the current score is higher than the high score
            self.highscore = self.score  # Update the high score with the current score
        self.score = 0  # Reset the score to 0
        self.store_highscore()  # Call the method to store the high score in a file
        self.update_scoreboard()  # Call the method to update the scoreboard text

    def store_highscore(self):
        with open("high_score.txt", "w") as file:  # Open the file in write mode
            file.write(str(self.highscore))  # Write the high score to the file

    def read_score(self):
        with open("high_score.txt", "r") as file:  # Open the file in read mode
            score = file.read()  # Read the high score from the file
            self.highscore = int(score)  # Convert the high score to an integer
