import json
import random
import time
import tkinter as tk
from tkinter import simpledialog, messagebox

last_action_time = 0


class Difficulty:
    EASY = "Easy"
    NORMAL = "Normal"
    HARD = "Hard"
    EXPERT = "Expert"


class Rank:
    BEGINNER = "Beginner"
    INTERMEDIATE = "Intermediate"
    EXPERT = "Expert"
    ASCENDED_MINER = "Ascended Miner"


class MineralType:
    GANGUE = "Gangue"
    MAGNETIC = "Magnetic"


class Mineral:
    def __init__(self, name, value, mineral_type, refined_value, upgrade_required=False):
        self.name = name
        self.value = value
        self.mineral_type = mineral_type
        self.refined_value = refined_value
        self.upgrade_required = upgrade_required


class Player:
    def __init__(self, name, difficulty, rank, total_money=0, debt=0, gpr=False, lucky_charm=False, power_drill=False,
                 refinery_upgrade=False, magnetic_survey=False):
        self.name = name
        self.difficulty = difficulty
        self.rank = rank
        self.total_money = total_money
        self.debt = debt
        self.gpr = gpr
        self.lucky_charm = lucky_charm
        self.power_drill = power_drill
        self.refinery_upgrade = refinery_upgrade
        self.magnetic_survey = magnetic_survey

    def to_dict(self):
        return {
            "name": self.name,
            "difficulty": self.difficulty,
            "rank": self.rank,
            "total_money": self.total_money,
            "debt": self.debt,
            "gpr": self.gpr,
            "lucky_charm": self.lucky_charm,
            "power_drill": self.power_drill,
            "refinery_upgrade": self.refinery_upgrade,
            "magnetic_survey": self.magnetic_survey
        }


def initialize_minerals():
    return [
        Mineral("Gold", 50000, None, 100000),
        Mineral("Silver", 30000, None, 60000),
        Mineral("Diamond", 10000000, None, 2000000),
        Mineral("Quartz", 0, MineralType.GANGUE, 0),
        Mineral("Emerald", 20000, None, 40000),
        Mineral("Ruby", 25000, None, 50000),
        Mineral("Sapphire", 30000, None, 60000),
        Mineral("Amethyst", 10000, None, 20000),
        Mineral("Galena", 15000, None, 30000, True),  # Magnetic mineral
        Mineral("Haematite", 20000, None, 40000, True),  # Magnetic mineral
        Mineral("Gangue", 0, MineralType.GANGUE, 0),
        Mineral("Calcite", 0, MineralType.GANGUE, 0),
        Mineral("Gangite", 0, MineralType.GANGUE, -50),
        Mineral("Netherack", 0, MineralType.GANGUE, 0),
        Mineral("Halite", 0, MineralType.GANGUE, 0),
        Mineral("talc", 0, MineralType.GANGUE, 0),
        Mineral("Cobblestone", 0, MineralType.GANGUE, 0),
        Mineral("oxides of Silicon", 0, MineralType.GANGUE, 0, True),  # Magnetic mineral
        Mineral("Water", 0, MineralType.GANGUE, 0),
        Mineral("Refined Element", 24514, None, 2147000000, True)
    ]


def initialize_weights():
    return [1, 3, 0.1, 20, 10, 5, 5, 10, 10, 20, 21.7, 10, 50, 100, 1, 5, 25, 40, 70, 0.00001]


def load_games():
    players = []
    try:  # Almost Like Java
        with open('saves.txt', 'r') as save_file:
            for line in save_file:
                data = json.loads(line.strip())
                players.append(Player(**data))
    except FileNotFoundError:  # Execpt FileNotFoundError: for java
        pass
    return players


def save_games(players):
    with open('saves.txt', 'w') as save_file:
        for player in players:
            save_file.write(json.dumps(player.to_dict()) + '\n')


def display_info(title, message):
    messagebox.showinfo(title, message)


def display_warning(title, message):
    messagebox.showwarning(title, message)


def get_player_input(message, options):
    result = None

    def set_result(value):
        nonlocal result
        result = value
        root.destroy()

    root = tk.Tk()
    root.withdraw()

    dialog = tk.Toplevel(root)
    dialog.title("Mining Game")
    dialog.geometry("350x200")

    label = tk.Label(dialog, text=message)
    label.pack(pady=10)

    for option in options:
        button = tk.Button(dialog, text=option, command=lambda opt=option: set_result(opt))
        button.pack(side=tk.TOP, pady=5)

    root.wait_window(dialog)
    return result


def purchase_item(cost, message, item_name, condition):
    if player.total_money >= cost and not condition:
        purchase = get_player_input(message, ["yes", "no"])
        if purchase == "yes":
            player.total_money -= cost
            condition = True
            display_info("Mining Game", f"You have bought a {item_name}.")
    return condition


def mine_mineral(mineral):
    return (-10000 - (player.total_money / 2)) if mineral.mineral_type == MineralType.GANGUE else (
        mineral.value * 2 if player.power_drill else mineral.value)


def refine_mineral(mineral):
    if mineral.name == "Refined Element" and not player.refinery_upgrade:
        display_info("Mining Game", "You need a Refinery Upgrade to refine the Refined Element.")
        return 0
    return (-10000 if mineral.mineral_type == MineralType.GANGUE else (
        mineral.refined_value * 3 if player.refinery_upgrade else mineral.refined_value))


def handle_debt():
    if player.total_money < 0 and player.debt == 0:
        loan = get_player_input("You are in debt. Do you want to take a loan of £10000?", ["yes", "no"])
        if loan == "yes":
            player.total_money += 10000
            player.debt += 10000


def handle_tax():
    if player.total_money >= 1000000:
        tax = player.total_money * 0.2
        player.total_money -= tax
        display_info("Mining Game",
                     f"You have reached £1000000. You have been taxed £{tax}. Your total money is now £{player.total_money}.")


def pay_back_loan():
    if player.debt > 0 and player.total_money >= player.debt * 2:
        payment = get_player_input(
            f"You currently owe £{player.debt}. Do you want to pay back the loan now? (£{player.debt * 2})",
            ["yes", "no"])
        if payment == "yes":
            if player.total_money >= player.debt * 2:
                player.total_money -= player.debt * 2
                player.debt = 0
                display_info("Mining Game",
                             f"You have paid back your loan. Your total money is now £{player.total_money}.")
            else:
                display_warning("Mining Game", "You don't have enough money to pay back the loan.")


def purchase_upgrades():
    player.gpr = purchase_item(50000, "Do you want to buy a Ground Penetrating Radar for £50000?",
                               "Ground Penetrating Radar", player.gpr)
    player.lucky_charm = purchase_item(75000, "Do you want to buy a Lucky Charm for £75000?", "Lucky Charm",
                                       player.lucky_charm)
    player.power_drill = purchase_item(100000, "Do you want to buy a Power Drill for £100000?", "Power Drill",
                                       player.power_drill)
    player.refinery_upgrade = purchase_item(200000, "Do you want to buy a Refinery Upgrade for £200000?",
                                            "Refinery Upgrade", player.refinery_upgrade)
    player.magnetic_survey = purchase_item(150000, "Do you want to buy a Magnetic Survey for £150000?",
                                           "Magnetic Survey", player.magnetic_survey)


def update_difficulty_and_rank():
    if player.total_money > 10000000:
        player.rank = Rank.ASCENDED_MINER
    elif player.total_money > 5000000:
        player.rank = Rank.EXPERT
    elif player.total_money > 1000000:
        player.rank = Rank.INTERMEDIATE
    else:
        player.rank = Rank.BEGINNER


def update_ui():
    global ui_text
    if player.rank == Rank.ASCENDED_MINER:
        color = "purple"
    elif player.rank == Rank.EXPERT:
        color = "red"
    elif player.rank == Rank.INTERMEDIATE:
        color = "orange"
    elif player.rank == Rank.BEGINNER:
        color = "green"
    else:
        color = "black"

    ui_text.set(
        f"Name: {player.name}\nDifficulty: {player.difficulty}\nRank: {player.rank}\nTotal Money: £{player.total_money}\nDebt: £{player.debt}")


def random_event():
    chance = random.randint(1, 100)
    global idontknow
    global emod
    if chance <= 25:
        event_ls = ["good","bad"]
        event_type = random.choices(event_ls, weights=eweight, k=1)[0]
        if event_type == "good":
            idontknow = random.randint(0, 10000)
            idontknow = idontknow * modifier
        elif event_type == "bad":
            idontknow = random.randint(-10000, 0)
            emode = emod * -1
            print(emod)
            idontknow = idontknow * emode
        event_description_good = random.choice([
            f"You found a hidden treasure! Gain {idontknow}",
            f"You found a good thing. Gain {idontknow}.",
            f"A generous investor offers you a loan. Gain {idontknow + 15000} but incur a debt of £15000."
        ])
        event_description_bad = random.choice([
            f"You found a hidden treasure! It was a BOMB! Lose {idontknow} .",
            f"You dug into a Dyke. It was still full of hot magma. Lose {idontknow}",
            f"A generous investor offers you a loan. Gain {idontknow}."
        ])

        if event_type == "good":
            player.total_money += idontknow
            display_info("Mining Game - Random Event", event_description_good)
        elif event_type == "bad":
            player.total_money += idontknow
            display_info("Mining Game - Random Event", event_description_bad)


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
    def on_closing():
        save_games(players)
        root.destroy()

    root = tk.Tk()
    root.title("Mining Game")
    root.geometry("800x600")
    root.protocol("WM_DELETE_WINDOW", on_closing)

    global ui_text
    ui_text = tk.StringVar()
    update_ui()

    text = tk.Text(root, height=20, width=60)
    text.pack(pady=10)

    def start_new_game():
        global player
        name = simpledialog.askstring("Name", "What is your name?")
        difficulty = simpledialog.askstring("Difficulty", "Choose difficulty (Easy/Normal/Hard/Expert):").capitalize()
        player = Player(name, difficulty, Rank.BEGINNER)
        players.append(player)
        save_games(players)

    def load_existing_game():
        global player
        loaded_player = choose_save_to_load(players)
        if loaded_player:
            player = loaded_player
            update_ui()
            display_info("Mining Game", f"Welcome back, {player.name}!")
        else:
            display_info("Mining Game", "No existing game found. Starting a new game.")
    def mine():
        save_games(players)

        handle_debt()
        handle_tax() # Before Mine
        pay_back_loan()
        purchase_upgrades()

        mineral = random.choices(minerals, weights=weights, k=1)[0]

        options = ["Mine", "Refine", 'None']
        action = get_player_input(f"You have found {mineral.name}! What would you like to do?", options)

        def elemented():
            display_info("Mining Game", "You need a Refinery Upgrade to refine Element.")
            display_warning("ELEMENT INFECTION", "Element Overruns Your Mine")
            options = ["Shut down mine", "Pay for Army", "die"]
            action = get_player_input(f"You have found {mineral.name}! What would you like to do?", options)
            if action == "Shut down mine":
                player.total_money -= player.total_money // 2
            elif action == "Pay for Army":
                player.total_money -= 500000
                display_info("Mining Game", "You cleared the Element.")
            elif action == "die":
                tk.messagebox.showerror("Mining Game", "You Lose (if you get to positive ur a no life)")
                player.total_money -= 1364386145389789789223
                save_games(players)

        if action == "Mine":
            if mineral.name == "Refined Element" and not player.refinery_upgrade:
                elemented()
                return
            if mineral.mineral_type == MineralType.GANGUE:
                player.total_money -= 10000
                display_info("Mining Game", f"Oh no! It's a gangue mineral. You lost £10,000.")
            else:
                player.total_money += mine_mineral(mineral) * modifier
                last_action_time = time.time()
        elif action == "Refine":
            if mineral.name == "Refined Element" and not player.refinery_upgrade:
                elemented()
                return
            if mineral.mineral_type == MineralType.GANGUE:
                player.total_money -= 10000
                display_info("Mining Game", f"Oh no! It's a gangue mineral. You lost £10,000.")
            else:
                player.total_money += refine_mineral(mineral)
                last_action_time = time.time()
                if mineral.name != "Refined Element":
                    display_info("Mining Game",
                                 f"Great! You have refined {mineral.name} and earned an additional £{mineral.refined_value - mineral.value}.")

                if mineral.mineral_type == MineralType.MAGNETIC and player.magnetic_survey:
                    display_info("Mining Game", "Your Magnetic Survey detected a magnetic mineral.")

        update_difficulty_and_rank()
        update_ui()
        random_event()

        if action != "None":
            text.insert(tk.END, f"\nYou mined/refined {mineral.name}. Your total money is now £{player.total_money}.\n")
            text.yview(tk.END)  # Auto-scroll to the bottom

    def show_leaderboard_callback():
        show_leaderboard(players)

    mine_button = tk.Button(root, text="Mine", command=mine)
    mine_button.pack(side=tk.TOP, pady=5)

    start_new_game_button = tk.Button(root, text="Start New Game", command=start_new_game)
    start_new_game_button.pack(side=tk.TOP, pady=5)

    load_existing_game_button = tk.Button(root, text="Load Existing Game", command=load_existing_game)
    load_existing_game_button.pack(side=tk.TOP, pady=5)

    leaderboard_button = tk.Button(root, text="Leaderboard", command=show_leaderboard_callback)
    leaderboard_button.pack(side=tk.TOP, pady=5)

    exit_button = tk.Button(root, text="Exit", command=root.destroy)
    exit_button.pack(side=tk.TOP, pady=5)

    log_label = tk.Label(root, textvariable=ui_text)
    log_label.pack(side=tk.BOTTOM, pady=5)

    root.mainloop()


if __name__ == "__main__":
    MINING_INTERVAL = 10
    GPR_COST = 50000
    CHARM_COST = 75000  # IDE suggestion (Define Const)
    DRILL_COST = 100000
    UPGRADE_COST = 200000
    SURVEY_COST = 150000
    global emod

    players = load_games()
    player = players[-1] if players else None

    if player is None:
        name = simpledialog.askstring("Name", "What is your name?")
        difficulty = simpledialog.askstring("Difficulty", "Choose difficulty (Easy/Normal/Hard/Expert):").capitalize()
        player = Player(name, difficulty, Rank.BEGINNER)
        players.append(player)
        save_games(players)

    minerals = initialize_minerals()
    weights = initialize_weights()
    match player.difficulty:
        case Difficulty.EASY:
            modifier = 2
            eweight = [2,1]
        case Difficulty.NORMAL:
            modifier = 1
            eweight = [1,1]
            emod = 1
        case Difficulty.HARD:
            modifier = 0.5
            eweight = [1,3]
            emod = 2
        case Difficulty.EXPERT:
            modifier = 0.01
            eweight = [1,5]
            emod = 3
        case _:
            modifier = 1
            eweight = [1, 1]
            emod = 5

    main_game_loop()

