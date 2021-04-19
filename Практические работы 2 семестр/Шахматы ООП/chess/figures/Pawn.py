from ..figure import Figure
class Pawn(Figure):
    def __init__(self, position, player):
        super().__init__(position, player, 'P')
        self.jumped = False

    def move(self, position, lastMovedFigure = None):
        y,x = position
        self.jumped = (abs(y-self.y) == 2)
        return super(Pawn, self).move(position)
