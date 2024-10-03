# mine.py

import random
from PySide6.QtWidgets import QMessageBox
from Classer import Player, Mineral, MineralType, Difficulty, Rank
global player
def mine_mineral(mineral, player):
    if mineral.mineral_type == MineralType.GANGUE:
        player.total_money -= 10000
        QMessageBox.information(None, "Mining Game", f"Oh no! It's a gangue mineral. You lost £10,000.")
    else:
        player.total_money += mine_mineral_value(mineral, player)
        QMessageBox.information(None, "Mining Game", f"You mined {mineral.name}. Your total money is now £{player.total_money}.")

def mine_mineral_value(mineral, player):
    if player.power_drill:
        return mineral.value * 2
    else:
        return mineral.value

def refine_mineral(mineral, player):
    if mineral.name == "Refined Element" and not player.refinery_upgrade:
        QMessageBox.information(None, "Mining Game", "You need a Refinery Upgrade to refine the Refined Element.")
        return 0
    else:
        player.total_money += refine_mineral_value(mineral, player)
        print(player.total_money)

def refine_mineral_value(mineral, player):
    if player.refinery_upgrade:
        return mineral.refined_value
    else:
        return mineral.value

def handle_debt(player):
    if player.total_money < 0 and player.debt == 0:
        reply = QMessageBox.question(None, "Mining Game", "You are in debt. Do you want to take a loan of £10000?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            player.total_money += 10000
            player.debt += 10000

def handle_tax(player):
    if player.total_money >= 1000000:
        tax = player.total_money * 0.2
        player.total_money -= tax
        QMessageBox.information(None, "Mining Game", f"You have reached £1000000. You have been taxed £{tax}. Your total money is now £{player.total_money}.")

def pay_back_loan(player):
    if player.debt > 0 and player.total_money >= player.debt * 2:
        reply = QMessageBox.question(None, "Mining Game", f"You currently owe £{player.debt}. Do you want to pay back the loan now? (£{player.debt * 2})", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            player.total_money -= player.debt * 2
            player.debt = 0
            QMessageBox.information(None, "Mining Game", f"You have paid back your loan. Your total money is now £{player.total_money}.")
        else:
            QMessageBox.warning(None, "Mining Game", "You don't have enough money to pay back the loan.")

def purchase_upgrades(player):
    player.gpr = purchase_item(player, 50000, "Do you want to buy a Ground Penetrating Radar for £50000?","Ground Penetrating Radar", player.gpr)
    player.lucky_charm = purchase_item(player,75000, "Do you want to buy a Lucky Charm for £75000?", "Lucky Charm", player.lucky_charm)
    player.power_drill = purchase_item(player,100000, "Do you want to buy a Power Drill for £100000?", "Power Drill", player.power_drill)
    player.refinery_upgrade = purchase_item(player,200000, "Do you want to buy a Refinery Upgrade for £200000?", "Refinery Upgrade", player.refinery_upgrade)
    player.magnetic_survey = purchase_item(player,150000, "Do you want to buy a Magnetic Survey for £150000?", "Magnetic Survey", player.magnetic_survey)

def purchase_item(player, cost, message, item_name, condition):
    if player.total_money >= cost and not condition:
        reply = QMessageBox.question(None, "Mining Game", message, QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            player.total_money -= cost
            condition = True
            QMessageBox.information(None, "Mining Game", f"You have bought a {item_name}.")
    return condition

def update_difficulty_and_rank(player):
    if player.total_money > 1000000:
        player.rank = Rank.ASCENDED_MINER
    elif player.total_money > 100000:
        player.rank = Rank.EXPERT
    elif player.total_money > 10000:
        player.rank = Rank.INTERMEDIATE
    else:
        player.rank = Rank.BEGINNER

    if player.difficulty == Difficulty.EASY:
        player.rank = Rank.BEGINNER
    elif player.difficulty == Difficulty.NORMAL:
        player.rank = Rank.INTERMEDIATE
    elif player.difficulty == Difficulty.HARD:
        player.rank = Rank.EXPERT
    elif player.difficulty == Difficulty.EXPERT:
        player.rank = Rank.ASCENDED_MINER

def random_event(player):
    event = random.choices(["tax", "debt", "loan", "upgrade"], weights=[0.1, 0.1, 0.1, 0.1], k=1)[0]

    if event == "tax":
        handle_tax(player)
    elif event == "debt":
        handle_debt(player)
    elif event == "loan":
        pay_back_loan(player)
    elif event == "upgrade":
        purchase_upgrades(player)
