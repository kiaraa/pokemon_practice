import random
class Pokemon:

    def __init__(self, nickname="youre_a_lazy_programmer", base_hp=100, base_atk = 100, base_def = 100, base_spatk = 100,\
                 base_spdef = 100, base_speed = 100, lv = 1, exp_total = 100):
        self.exp_total = exp_total
        self.base_spdef = base_spdef
        self.base_spatk = base_spatk
        self.base_def = base_def
        self.base_atk = base_atk
        self.nickname = nickname
        self.base_hp = base_hp
        self.base_speed = base_speed
        self.lv = lv
        self.hp_iv = random.randint(0,32)
        self.atk_iv = random.randint(0,32)
        self.def_iv = random.randint(0,32)
        self.spatk_iv = random.randint(0,32)
        self.spdef_iv = random.randint(0,32)
        self.speed_iv = random.randint(0,32)

    def get_hp_stat(self):
        hp_stat = int(((((self.base_hp + self.hp_iv) * 2) * self.lv) / 100) + self.lv + 10)
        return hp_stat

    def get_atk_stat(self):
        atk_stat = int(((((self.base_atk + self.atk_iv) * 2) * self.lv) / 100) + 5)
        return atk_stat

    def get_def_stat(self):
        def_stat = int(((((self.base_def + self.def_iv) * 2) * self.lv) / 100) + 5)
        return def_stat

    def get_spatk_stat(self):
        spatk_stat = int(((((self.base_spatk + self.spatk_iv) * 2) * self.lv) / 100) + 5)
        return spatk_stat

    def get_spdef_stat(self):
        spdef_stat = int(((((self.base_spdef + self.spdef_iv) * 2) * self.lv) / 100) + 5)
        return spdef_stat

    def get_speed_stat(self):
        speed_stat = int(((((self.base_speed + self.speed_iv) * 2) * self.lv) / 100) + 5)
        return speed_stat

    def get_exp_total(self):
        exp_total = self.exp_total
        return exp_total