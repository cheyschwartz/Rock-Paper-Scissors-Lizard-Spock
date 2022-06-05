from human import Human
from ai import AI

import random



class Game:
    def __init__(self):
        self.player_one = None
        self.player_two = None

    def run_game(self):
        self.display_welcome()
        self.display_instructions()
        self.number_of_players()
        self.game()
        self.display_winners()

    def display_welcome(self):
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")

    def display_instructions(self):
        print("""
                Game Rules

                Rock crushes Scissors
                Scissors cuts Paper
                Paper covers Rock
                Rock crushes Lizard
                Lizard poisons Spock
                Spock smashes Scissors
                Scissors decapitates Lizard
                Lizard eats Paper
                Paper disproves Spock
                Spock vaporizes Rock
                    """)

    def number_of_players(self):
        player_choice = input("Press 1 to play with AI, press 2 to play with a friend or press 3 to watch an AI battle")
        if player_choice == "1":
            self.player_one = Human()
            self.player_two = AI()
        elif player_choice == "2":
            self.player_one = Human()
            self.player_two = Human()
        elif player_choice == "3":
            self.player_one = AI()
            self.player_two = AI()
    
    def game(self):
        while self.player_one.score < 2 and self.player_two.score < 2:
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
                print("It's a tie, play again!")
            elif self.player_one.chosen_gesture == 0 and ((self.player_two.chosen_gesture == 2) or (self.player_two.chosen_gesture == 3)):
                print("Human wins")
                self.player_one.score += 1
            elif self.player_one.chosen_gesture == 1 and ((self.player_two.chosen_gesture == 0) or (self.player_two.chosen_gesture == 4)):
                print("Human wins")
                self.player_one.score += 1
            elif self.player_one.chosen_gesture == 2 and ((self.player_two.chosen_gesture == 1) or (self.player_two.chosen_gesture == 3)):
                print("Human wins")
                self.player_one.score += 1
            elif self.player_one.chosen_gesture == 3 and ((self.player_two.chosen_gesture == 4) or (self.player_two.chosen_gesture == 1)):
                print("Human wins")
                self.player_one.score += 1
            elif self.player_one.chosen_gesture == 4 and ((self.player_two.chosen_gesture == 2) or (self.player_two.chosen_gesture == 0)):
                print("Human wins")
                self.player_one.score += 1
            else:
                print("AI wins")
                self.player_two.score += 1

    def display_winners(self):
        if self.player_one.score >= 2:
            print("Human wins the game! Game Over!")
        else:
            print("AI wins this game! Game Over")