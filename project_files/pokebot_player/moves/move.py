import random


class Move:
    def __init__(self, category, power, accuracy):
        self.category = category
        self.power = power
        self.accuracy = accuracy
        self.user = None
        self.target = None

    def get_user_and_target(self, user, target):
        self.user = user
        self.target = target

    def damage_calculator(self):
        if self.category == "physical":
            damage = ((2 * self.user.level / 5 + 2) * self.power * (
                        self.user.get_atk_stat() / self.target.get_def_stat()) / 50) + 2
            return damage

        elif self.category == "special":
            damage = ((2 * self.user.level / 5 + 2) * self.power * (
                        self.user.get_spatk_stat() / self.target.get_spdef_stat()) / 50) + 2
            return damage

    def does_it_hit(self):
        hit_number = random.randint(0, 101)
        if hit_number <= self.accuracy:
            return True
        else:
            return False
