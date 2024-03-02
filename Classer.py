global earned

earned = 0
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
    NONETIC = "Nonetic"

class Mineral:
    def __init__(self, name, value, mineral_type, refined_value, weight, upgrade_required=False):
        self.name = name
        self.value = value
        self.mineral_type = mineral_type
        self.refined_value = refined_value
        self.weight = weight
        self.upgrade_required = upgrade_required


class Player:
    def __init__(self, name, difficulty, rank, total_money=0, debt=0, gpr=False, lucky_charm=False, power_drill=False, refinery_upgrade=False, magnetic_survey=False):
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
        self.multiplier = 1

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