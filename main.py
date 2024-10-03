# main.py
# main.py

import random
import json
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QMenuBar, QInputDialog, QTabWidget, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QMessageBox
from mine import mine_mineral, refine_mineral, handle_debt, handle_tax, pay_back_loan, purchase_upgrades, update_difficulty_and_rank, random_event
from ui import Ui_MainWindow, apply_dark_theme
from mineral_loader import load_minerals
from player_loader import load_players
from difficulty_loader import load_difficulty
from rank_loader import load_rank
from Classer import Player
from Classer import Rank
from Classer import Mineral
from Event import special_events as special_events



def special_event(player):
    player.multiplier = 1
    if random.randint(1,1000) > 999:
      event = random.choice(special_events)
      display_info('Special Event', event['message'])
      event['effect'](player)
      player.earnings *= player.multiplier

def initialize_minerals():
    return load_minerals()

def initialize_weights():
    minerals = load_minerals()
    return [mineral.weight for mineral in minerals]

def load_games():
    return load_players()

def save_games(players):
    with open('saves.txt', 'w') as save_file:
        for player in players:
            save_file.write(json.dumps(player.to_dict()) + '\n')

def display_info(title, message):
    QMessageBox.information(None, title, message)

def display_warning(title, message):
    QMessageBox.warning(None, title, message)

def get_player_input(message, options):
    result, ok = QInputDialog.getItem(None, "Mining Game", message, options, 0, False)
    if ok:
        return result
    else:
        return None

def choose_save_to_load(players):
    save_options = [f"{i + 1}. {player.name}" for i, player in enumerate(players)]
    save_choice = get_player_input("Choose a save to load:", save_options)
    if save_choice:
        selected_index = int(save_choice.split('.')[0]) - 1
        return players[selected_index]
    return None

def show_leaderboard(players):
    sorted_players = sorted(players, key=lambda p: p.total_money, reverse=True)
    leaderboard_text = "Leaderboard:\n"
    for i, player in enumerate(sorted_players):
        leaderboard_text += f"{i + 1}. {player.name} - £{round(player.total_money)}\n"
    display_info("Mining Game - Leaderboard", leaderboard_text)

def main_game_loop():
    global players
    def on_closing():
        save_games(players)
        root.destroy()

    app = QApplication([])
    root = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(root)
    root.show()
    players = load_games()
    player = players[-1] if players else None

    if player is None:
        name, ok = QInputDialog.getText(None, "Name", "What is your name?")
        difficulty, ok = QInputDialog.getText(None, "Difficulty", "Choose difficulty (Easy/Normal/Hard/Expert):")
        player = Player(name, difficulty, Rank.BEGINNER)
        players.append(player)
        save_games(players)

    minerals = initialize_minerals()
    weights = initialize_weights()

    ui.mine_button.clicked.connect(lambda: [mine(player, minerals, weights, ui), special_event(player)])
    ui.start_new_game_button.clicked.connect(start_new_game)
    ui.load_existing_game_button.clicked.connect(load_existing_game)
    ui.leaderboard_button.clicked.connect(lambda: show_leaderboard(players))
    ui.exit_button.clicked.connect(lambda: on_closing())

    app.exec()

def mine(player, minerals, weights, ui):
    save_games([player])

    handle_debt(player)
    handle_tax(player)
    pay_back_loan(player)
    purchase_upgrades(player)

    mineral = random.choices(minerals, weights=weights, k=1)[0]

    options = ["Mine", "Refine", 'None']
    action = get_player_input(f"You have found {mineral.name}! What would you like to do?", options)

    if action == "Mine":
        mine_mineral(mineral, player)
    elif action == "Refine":
        refine_mineral(mineral, player)

    update_difficulty_and_rank(player)
    random_event(player)

    if action != "None":
        ui.text.insertPlainText(f"\nYou mined/refined {mineral.name}. Your total money is now £{player.total_money}.\n")
        ui.text.verticalScrollBar().setValue(ui.text.verticalScrollBar().maximum())

def start_new_game():
    global players
    name, ok = QInputDialog.getText(None, "Name", "What is your name?")
    difficulty, ok = QInputDialog.getText(None, "Difficulty", "Choose difficulty (Easy/Normal/Hard/Expert):")
    player = Player(name, difficulty, Rank.BEGINNER)
    players.append(player)
    save_games(players)

def load_existing_game():
    global players
    loaded_player = choose_save_to_load(players)
    if loaded_player:
        player = loaded_player
        display_info("Mining Game", f"Welcome back, {player.name}!")
    else:
        display_info("Mining Game", "No existing game found. Starting a new game.")

if __name__ == "__main__":
    main_game_loop()
# Path: mine.py
