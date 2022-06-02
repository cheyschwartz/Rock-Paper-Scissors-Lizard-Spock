from human import Human
from ai import AI

import random



class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = AI()

    def run_game(self):
        self.display_welcome()
        self.display_instructions()
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
    #shorcut for game logic 
       # check to see "if" its a tie
       # check to see "elif" player one was the winner
       # else player 2 was the winner
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
                self.player_two.score +=1

    def display_winners(self):
        while self.player_one.score >= 3:
            print("Human wins the game! Game Over!")
        else:
            print("AI wins the game! Game Over!")