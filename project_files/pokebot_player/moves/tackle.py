from project_files.pokebot_player.moves.move import Move


class Tackle(Move):
    def __init__(self):
        super(Tackle, self).__init__(category="physical", power=35, accuracy=95)

    def use(self):
        does_it_hit = self.does_it_hit()
        if does_it_hit:
            damage = self.damage_calculator()
        else:
            damage = 0

        return damage
