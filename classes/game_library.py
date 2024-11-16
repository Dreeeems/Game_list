import json
import os
from game import Game
class Game_Library:
    def __init__(self, filename="games.json"):
        self.filename=filename
        self.games=[]
        self.load_game()
        
        #functions
        
        def load_game(self):
            try:
                with open(self.filename,"r") as file:
                    games_data = json.load(file)
                    self.games = [Game(**game) for game in games_data]
            except FileNotFoundError:
                self.games =[]

    
    def save_game(self):
        with open(self.filename,"w") as file:
            json.dump([game.to_dict() for game in self.games],file, indent=4)


    
    def add_game(self,game):
        self.games.append(game)
        self.save_game()
            