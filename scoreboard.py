from turtle import Turtle
import random
import time

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self, screen):
        super().__init__()  # Correct usage of super()
        self.screen = screen
        self.score = 0
        self.highscores = self.load_highscores()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)  # Position the scoreboard at the top of the screen
        self.update_score()

    def load_highscores(self):
        try:
            with open("highscores.txt", "r") as file:
                highscores = [line.strip().split(",") for line in file.readlines()]
                # Ensure there are exactly 3 entries
                while len(highscores) < 3:
                    highscores.append(["None", "0"])
                return highscores
        except FileNotFoundError:
            # Return default highscores if file is missing
            return [["None", "0"], ["None", "0"], ["None", "0"]]

    def save_highscores(self):
        with open("highscores.txt", "w") as file:
            for name, score in self.highscores:
                file.write(f"{name}:{score}\n")

    def update_highscores(self):
        for i in range(3):
            if self.score > int(self.highscores[i][1]):
                name = self.screen.textinput("New Highscore!", "Enter your name:")
                self.highscores.insert(i, [name, str(self.score)])
                self.highscores = self.highscores[:3]  # Keep only top-3
                self.save_highscores()
                break

    def game_over(self):
        for _ in range(10):
            self.goto(random.randint(-10, 10), random.randint(-10, 10))
            time.sleep(0.05)
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        self.update_highscores()


    def update_score(self):
        self.clear()  # Clear previous text
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        self.score = 0
        self.update_score()

