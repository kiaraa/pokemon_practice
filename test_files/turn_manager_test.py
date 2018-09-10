import unittest
from project_files.pokebot_player.pokemon import Pokemon
from project_files.pokebot_player.turn_manager import TurnManager

class MockUI:
    def __init__(self):
        self.number_of_times_called = 0
        self.last_message_displayed = ''

    def prompt_user(self):
        self.number_of_times_called += 1

    def get_number_of_times_called(self):
        return self.number_of_times_called


class TurnManagerTest(unittest.TestCase):

    def setup_method(self, method):
        self.ui = MockUI()
        self.turn_manager = TurnManager(ui = self.ui)

    def test_calls_ui_initially(self):
        self.turn_manager.take_user_turn()
        self.assertEqual(self.ui.get_number_of_times_called(), 1)

