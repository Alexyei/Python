from ..figure import Figure
class King(Figure):
    def __init__(self, position, player):
        super().__init__(position, player, 'K')

    def move(self, position, lastMovedFigure = None, boardSize = None):
        y, x = position
        height, width = boardSize
        f_y, f_x = self.getPosition()
        super(King, self).move(position)

        # длинная рокировка
        if f_x - x == 2:
            return {"status": 'move', "data": {"figure": (f_y, 0), "position": (f_y, 3)}}
        # короткая рокировка
        elif x - f_x == 2:
            return {"status": 'move', "data": {"figure": (f_y, width-1), "position": (f_y,  width-3)}}

        return {"status": 'success'}
