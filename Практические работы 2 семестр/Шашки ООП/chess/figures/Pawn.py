from chess.figure import Figure
class Pawn(Figure):
    def __init__(self, position, player):
        super().__init__(position, player, 'P')
        # self.jumped = False

    def move(self, position, lastMovedFigure = None, boardSize = None):
        height, width = boardSize
        # y, x = position
        # self.jumped = (abs(y - self.y) == 2)
        super(Pawn, self).move(position)

        # проверка берёт ли эта пешка другую на проходе
        # if type(lastMovedFigure) == Pawn and lastMovedFigure.jumped:
        #     if lastMovedFigure.x == self.x:
        #         if self.player == 'White':
        #             if lastMovedFigure.y - self.y == 1:
        #                 return {"status": 'kill', "data": lastMovedFigure.getPosition()}
        #         else:
        #             if  self.y - lastMovedFigure.y == 1:
        #                 return {"status": 'kill', "data": lastMovedFigure.getPosition()}

        # проверка пешка дошла до края доски превращение в другую фигуру
        if (self.player == 'White' and self.y == 0) or (self.player == 'Black' and self.y ==  height -1):
            return {"status": 'transform', "data": self.transform()}

        return {"status": 'success'}

    def transform(self):
        # while True:
        #     print("Замена пешки, выберите одну из фигур: q,r,n,b")
        #     figure = input()
        #     if figure in "qQ":
        #         return "Queen"
        #     elif figure in "nN":
        #         return "Knight"
        #     elif figure in "bB":
        #         return "Bishop"
        #     elif figure in "rR":
        #         return "Rock"
        return "King"
