from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 25, "bold")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("projects/turtle/snake/data.txt") as file:
            self.high_score = int(file.read())
        self.color("gold")
        self.penup()
        self.goto(0,200)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"SCORE : {self.score}    HIGHSCORE : {self.high_score}",align=ALIGN ,font=FONT)

    # def over(self):
        # self.clear()
        # self.goto(0,0)
        # self.color("red")
        # self.write(f"GAME OVER! \n YOUR SCORE : {self.score}",align=ALIGN ,font=FONT)
        # self.high()

    def high(self):
        if self.score > self.high_score:
            self.high_score = self.score
            
            with open("projects/turtle/snake/data.txt", mode ="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
            # self.goto(0,-100)
            # self.write(f"CONGRATULATIONS!\n YOU BREAK THE HIGHSCORE!!{self.high_score}",align=ALIGN ,font=FONT)



    def scoreboard(self):
        self.score += 1
        self.clear()
        self.update_score()
        