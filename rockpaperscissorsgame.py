import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Rock Paper Scissors")
        self.user_score = 0
        self.computer_score = 0
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Choose rock, paper, or scissors:")
        self.label.pack()

        self.user_choice_var = tk.StringVar()
        self.user_choice_var.set("rock")

        self.user_choice_radio = tk.Radiobutton(self.root, text="Rock", variable=self.user_choice_var, value="rock")
        self.user_choice_radio.pack()

        self.user_choice_radio = tk.Radiobutton(self.root, text="Paper", variable=self.user_choice_var, value="paper")
        self.user_choice_radio.pack()

        self.user_choice_radio = tk.Radiobutton(self.root, text="Scissors", variable=self.user_choice_var, value="scissors")
        self.user_choice_radio.pack()

        self.play_button = tk.Button(self.root, text="Play", command=self.play)
        self.play_button.pack()

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

        self.score_label = tk.Label(self.root, text=f"User Score: {self.user_score} | Computer Score: {self.computer_score}")
        self.score_label.pack()

        self.play_again_button = tk.Button(self.root, text="Play Again", command=self.reset_game, state=tk.DISABLED)
        self.play_again_button.pack()

    def play(self):
        user_choice = self.user_choice_var.get()
        computer_choice = random.choice(["rock", "paper", "scissors"])
        
        result = self.determine_winner(user_choice, computer_choice)
        self.update_score(result)
        self.display_result(user_choice, computer_choice, result)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "tie"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            return "win"
        else:
            return "lose"

    def update_score(self, result):
        if result == "win":
            self.user_score += 1
        elif result == "lose":
            self.computer_score += 1

    def display_result(self, user_choice, computer_choice, result):
        result_text = f"User chose {user_choice}. Computer chose {computer_choice}. "
        if result == "tie":
            result_text += "It's a tie!"
        elif result == "win":
            result_text += "You win!"
        else:
            result_text += "Computer wins!"
        self.result_label.config(text=result_text)

        self.score_label.config(text=f"User Score: {self.user_score} | Computer Score: {self.computer_score}")

        self.play_again_button.config(state=tk.NORMAL)

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text=f"User Score: {self.user_score} | Computer Score: {self.computer_score}")
        self.result_label.config(text="")
        self.play_again_button.config(state=tk.DISABLED)

game = RockPaperScissorsGame()
game.root.mainloop()
