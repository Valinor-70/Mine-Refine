# player_loader.py

import json
from Classer import Player

def load_players():
        try:
            with open('saves.txt', 'r') as save_file:
                players = [Player(**json.loads(line)) for line in save_file]
        except FileNotFoundError:

            print("The file 'saves.txt' was not found.")
            players = []
            pass

        return players
