# mineral_loader.py

import json
from Classer import Mineral, MineralType
def load_minerals():
    with open('minerals.json', 'r') as file:
        minerals = json.load(file)
    return [Mineral(**mineral) for mineral in minerals]

