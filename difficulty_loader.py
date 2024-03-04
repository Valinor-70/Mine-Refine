# difficulty_loader.py

import json

def load_difficulty():
    with open('difficulty.json', 'r') as file:
        difficulty = json.load(file)
    return difficulty
