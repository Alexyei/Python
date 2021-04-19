from ..figure import Figure
class Bishop(Figure):
    def __init__(self, position, player):
        super().__init__(position, player, 'B')