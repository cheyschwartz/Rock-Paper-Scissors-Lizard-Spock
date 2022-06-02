from player import Player
import random

class Human(Player):
    def __init__(self):
        self.name = "Player One"
        super().__init__(self.name)
        self.score = 0
        


    def choose_gesture(self):
        self.chosen_gesture = input("Press 0 for Rock, Press 1 for Paper, press 2 for Scissors ect..")
        print(f"{self.name} has picked {self.gesture_list[int(self.chosen_gesture)]}")


    # def human_choice():
    #     choice = [0,4]
    #     if choice == 0:
    #         print("Player picked Rock")
    #     elif choice == 1:
    #         print("Player picked Paper")
    #     elif choice == 2:
    #         print("Player picked Scissors")
    #     elif choice == 3:
    #         print("Player picked Lizard")
    #     elif choice == 4:
    #         print("Player picked Spock")