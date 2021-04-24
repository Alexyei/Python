from chess.figure import Figure
class Knight(Figure):
    def __init__(self, position, player):
        super().__init__(position, player, 'N')