import random 

class Player:
    
    
    
    def __init__(self, name):
        self.name = name
        self.gesture_list = ["Rock","Paper","Scissors","Lizard","Spock"]
        self.chosen_gesture = ""
        