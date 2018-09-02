import unittest
from project_files.pokebot_player.pokemon import Pokemon


class PokemonTest(unittest.TestCase):

    def test_pokemon_nickname(self):
        missingno = Pokemon(nickname = "Missy")
        self.assertEqual(missingno.nickname, "Missy")

    def test_pokemon_base_hp(self):
        missingno = Pokemon(base_hp=100)
        self.assertEqual(missingno.base_hp, 100)

    def test_pokemon_base_atk(self):
        missingno = Pokemon(base_atk=100)
        self.assertEqual(missingno.base_atk, 100)

    def test_pokemon_base_def(self):
        missingno = Pokemon(base_def=100)
        self.assertEqual(missingno.base_def, 100)

    def test_pokemon_base_spatk(self):
        missingno = Pokemon(base_spatk=100)
        self.assertEqual(missingno.base_spatk, 100)

    def test_pokemon_base_spdef(self):
        missingno = Pokemon(base_spdef=100)
        self.assertEqual(missingno.base_spdef, 100)

    def test_pokemon_base_speed(self):
        missingno = Pokemon(base_speed=100)
        self.assertEqual(missingno.base_speed, 100)

    def test_pokemon_level(self):
        missingno = Pokemon(lv = 100)
        self.assertEqual(missingno.lv, 100)

    def test_pokemon_get_hp_stat(self):
        missingno = Pokemon()
        hp_iv = missingno.hp_iv
        expected_hp_stat = ((((missingno.base_hp + missingno.hp_iv) * 2) * missingno.lv) / 100) + missingno.lv + 10
        self.assertEqual(missingno.get_hp_stat(), int(expected_hp_stat))

    def test_pokemon_get_atk_stat(self):
        missingno = Pokemon()
        atk_iv = missingno.atk_iv
        expected_atk_stat = ((((missingno.base_atk + missingno.atk_iv) * 2) * missingno.lv) / 100) + 5
        self.assertEqual(missingno.get_atk_stat(), int(expected_atk_stat))

    def test_pokemon_get_def_stat(self):
        missingno = Pokemon()
        def_iv = missingno.def_iv
        expected_def_stat = ((((missingno.base_def + missingno.def_iv) * 2) * missingno.lv) / 100) + 5
        self.assertEqual(missingno.get_def_stat(), int(expected_def_stat))

    def test_pokemon_get_spatk_stat(self):
        missingno = Pokemon()
        spatk_iv = missingno.spatk_iv
        expected_spatk_stat = ((((missingno.base_spatk + missingno.spatk_iv) * 2) * missingno.lv) / 100) + 5
        self.assertEqual(missingno.get_spatk_stat(), int(expected_spatk_stat))

    def test_pokemon_get_spdef_stat(self):
        missingno = Pokemon()
        spdef_iv = missingno.spdef_iv
        expected_spdef_stat = ((((missingno.base_spdef + missingno.spdef_iv) * 2) * missingno.lv) / 100) + 5
        self.assertEqual(missingno.get_spdef_stat(), int(expected_spdef_stat))

    def test_pokemon_get_speed_stat(self):
        missingno = Pokemon()
        speed_iv = missingno.speed_iv
        expected_speed_stat = ((((missingno.base_speed + missingno.speed_iv) * 2) * missingno.lv) / 100) + 5
        self.assertEqual(missingno.get_speed_stat(), int(expected_speed_stat))

    def test_pokemon_get_exp_total(self):
        missingno = Pokemon(exp_total = 100)
        expected_exp_total = 100
        self.assertEqual(missingno.get_exp_total(), 100)

