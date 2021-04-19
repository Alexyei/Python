from chess.figure import Figure
class Queen(Figure):
    def __init__(self, position, player):
        super().__init__(position, player, 'Q')