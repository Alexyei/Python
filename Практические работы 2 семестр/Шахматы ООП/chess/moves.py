class FigureMoves:
    def __init__(self, state, figurePosition, safe):

        self.width = width
        self.height = height
        self.check = False
        self.current_figure = {'y': 7, 'x': 3}
        self.current_position = {'y': 7, 'x': 3}
        self.moved_figure = set()
        self.create_state()

    def create_state(self):
        self.state = [[], []]