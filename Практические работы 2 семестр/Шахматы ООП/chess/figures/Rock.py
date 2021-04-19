from chess.figure import Figure
class Rock(Figure):
    def __init__(self, position, player):
        super().__init__(position, player, 'R')