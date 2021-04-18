class Board:
    def __init__(self, width, height):

        self.width = width
        self.height = height
        self.check = False
        self.current_figure = {'y': 7, 'x': 3}
        self.current_position = {'y': 7, 'x': 3}
        self.moved_figure = set()
        self.create_state()

    def create_state(self):
        self.state = [[], []]

    # отобразить возможные ходы и выбор хода (position)
    def getFullState(self, moves=True, position=True):
        # показать текущие ходы, position = TRUE показать перемещение фигуры (при выборе хода)
        def getStateWithMoves():

            moves, kills = figureMoves()
            fullState = copy.deepcopy(state)
            for y, x in moves:
                fullState[y][x] = 'm'
            for y, x in kills:
                fullState[y][x] = 'k' + fullState[y][x]


            # текущая фигура
            if position:
                # print("cp")
                fullState[current_figure['y']][current_figure['x']] = 'm'
                fullState[current_position['y']][current_position['x']] = 'c' + state[current_figure['y']][
                    current_figure['x']]
            else:
                # print("cf")
                fullState[current_figure['y']][current_figure['x']] = 'c' + fullState[current_figure['y']][
                    current_figure['x']]

            # мои фигуры находящиеся под боем
            myFiguries = gelAllMyFiguries()
            for figure in myFiguries:
                if whoCanKilled(figure):
                    y, x = figure
                    # print("AIM"+str(figure))
                    fullState[y][x] = 'a' + fullState[y][x]

            # return [['bR', 'bN', 'bB', 'bQ', 'sbK', 'bB', 'bN', 'kbR'],
            #         ['bP', 'kbP', 'bP', 'bP', 'cbP', 'bP', 'bP', 'bP'],
            #         ['0'] * 8, ['m'] * 8, ['0'] * 8, ['0'] * 8,
            #         ['wP', 'wP', 'wP', 'wP', 'kwP', 'wP', 'wP', 'wP'],
            #         ['wR', 'wN', 'kwB', 'wQ', 'swK', 'cwB', 'wN', 'wR']]
            # print("fig")
            # print(current_figure)
            # print("pos")
            # print(current_position)
            # print(fullState)
            return fullState

        if drawMoves:
            return getStateWithMoves()
        return state