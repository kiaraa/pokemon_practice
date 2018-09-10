import unittest

from project_files.pokebot_player.moves.tackle import Tackle


class MoveTest(unittest.TestCase):

    def test_get_move_category_physical(self):
        self.tackle = Tackle()
        self.assertEqual(self.tackle.category, "physical")


