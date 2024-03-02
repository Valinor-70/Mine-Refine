# rank_loader.py

import json

def load_rank():
    with open('rank.json', 'r') as file:
        rank = json.load(file)
    return rank
