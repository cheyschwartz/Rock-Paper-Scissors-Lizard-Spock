from player import Player
import random

class Human(Player):
    def __init__(self):
        self.name = "Player One"
        super().__init__(self.name)
        self.score = 0

    def choose_gesture(self):
        self.chosen_gesture = int(input("Press 0 for Rock, 1 for Paper, 2 for Scissors, 3 Lizard, 4 Spock"))
        print(f"{self.name} has picked {self.gesture_list[self.chosen_gesture]}")


