from player import Player
import random


class AI(Player):

    def __init__(self):
        name = "AI"
        super().__init__(name)
        self.score = 0
        self.name = name

    # def choose_gesture(self):
    #     self.chosen_gesture = str(random.randint(0,4))
    #     print (f"{self.name} has picked {self.gesture_list[int(self.chosen_gesture)]}")

    def choose_gesture(self):
        choice = random.randint(0,4)
        self.chosen_gesture = choice
        if choice == 0:
            print("AI picked Rock")
        elif choice == 1:
            print("AI picked Paper")
        elif choice == 2:
            print("AI picked Scissors") 
        elif choice == 3:
            print("AI picked Lizard")
        elif choice == 4:
            print("AI picked Spock")
        return choice

