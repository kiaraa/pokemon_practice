class TurnManager:

    def __init__(self, ui):
        self.ui = ui


    def take_user_turn(self):
        self.ui.prompt_user()