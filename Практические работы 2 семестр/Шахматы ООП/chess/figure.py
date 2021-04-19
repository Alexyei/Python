class Figure:
    def __init__(self, position, player, name):
        # self._init()
        y, x = position
        self.y = y
        self.x = x
        self.player = player
        self.name = name

    def getPosition(self):
        return self.y, self.x

    def move(self, position, lastMovedFigure = None):
        y, x = position
        self.y = y
        self.x = x
        return {"status": 'success'}

    def __str__(self):
        return self.player[0].lover()+self.name