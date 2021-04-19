from chess.controller import Controller
from chess.figure import Figure
from chess.figures.Bishop import Bishop
from chess.figures.Queen import Queen
from chess.figures.Knight import Knight
from chess.figures.Rock import Rock
from chess.figures.King import King
from chess.figures.Pawn import Pawn
import copy

class Board:
    def __init__(self, height, width):
        # y
        self.height = height
        # x
        self.width = width

        self.check = False

        self.moved_figure = set()
        self.create_state()
        # self.current_figure = {'y': 6, 'x': 4}
        self.current_figure = self.state[6][4]
        # self.current_position = {'y': 6, 'x': 4}
        self.current_position = {'y': self.current_figure.y, 'x': self.current_figure.x}
        self.controller = Controller(self)

    def create_state(self):
        # self.state = [[], []]
        # заполняем доску пустыми ячейками
        self.state = [['0' for j in range(self.width)] for i in range(self.height)]

        # чёрные фигуры
        self.state[0][0] = Rock((0,0),'Black')
        self.state[0][7] = Rock((0, 7), 'Black')
        self.state[0][1] = Knight((0, 1), 'Black')
        self.state[0][6] = Knight((0, 6), 'Black')
        self.state[0][2] = Bishop((0, 2), 'Black')
        self.state[0][5] = Bishop((0, 5), 'Black')
        self.state[0][3] = Queen((0, 3), 'Black')
        self.state[0][4] = King((0, 4), 'Black')
        for j in range(self.width):
            self.state[1][j] = Pawn((1,j),'Black')

        # белые фигуры
        self.state[7][0] = Rock((7, 0), 'White')
        self.state[7][7] = Rock((7, 7), 'White')
        self.state[7][1] = Knight((7, 1), 'White')
        self.state[7][6] = Knight((7, 6), 'White')
        self.state[7][2] = Bishop((7, 2), 'White')
        self.state[7][5] = Bishop((7, 5), 'White')
        self.state[7][3] = Queen((7, 3), 'White')
        self.state[7][4] = King((7, 4), 'White')
        for j in range(self.width):
            self.state[6][j] = Pawn((6, j), 'White')


    # отобразить возможные ходы и выбор хода (position)
    def getFullState(self, player, moves=True, position=True):
        # показать текущие ходы, position = TRUE показать перемещение фигуры (при выборе хода)
        def getStateWithMoves():

            moves, kills = self.controller.figureMoves()
            # fullState = copy.deepcopy(self.state)
            fullState = [[str(el) for el in row] for row in self.state]
            for y, x in moves:
                fullState[y][x] = 'm'
            for y, x in kills:
                fullState[y][x] = 'k' + str(fullState[y][x])


            # текущая фигура
            if position:
                # print("cp")
                fullState[self.current_figure.y][self.current_figure.x] = 'm'
                fullState[self.current_position['y']][self.current_position['x']] = 'c' + str(self.state[self.current_figure.y][
                    self.current_figure.x])
            else:
                # print("cf")
                fullState[self.current_figure.y][self.current_figure.x] = 'c' + str(fullState[self.current_figure.y][
                    self.current_figure.x])

            # мои фигуры находящиеся под боем
            myFiguries = self.gelAllMyFiguries(player)
            for figure in myFiguries:
                if self.whoCanKilled(figure):
                    y, x = figure
                    # print("AIM"+str(figure))
                    fullState[y][x] = 'a' + str(fullState[y][x])

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

        if moves:
            return getStateWithMoves()
        return [[str(el) for el in row]for row in self.state]

    def whoCanKilled(self, aim):
        enemies = self.getAllEnemies(aim.player)
        # enemies = getAllEnemies(getPlayerByFigure(state[aim[0]][aim[1]]))

        killers = []
        for enemy in enemies:

            moves, kills = self.controller.figureMoves(enemy.getPosition(), safe=False)
            # if (enemy == (3,1)):
            #     print("KILLER")
            #     print(moves, kills)
            for move in moves:
                if move == aim:
                    killers.append(enemy)
            for kill in kills:

                if kill == aim:
                    killers.append(enemy)

        return killers

    # test ok
    def getAllEnemies(self,player):
        # if not player:
        #     player = currentPlayer
        enemies = []
        for y in range(self.height):
            for x in range(self.width):
                if self.isEnemy(self.state[y][x], player):
                    enemies.append(self.state[y][x])

        return enemies

    # test ok
    def gelAllMyFiguries(self, player):
        # return getAllEnemies(getMyEnemy())
        return self.getAllEnemies(player)

    def isFigure(self,ceil):
        return isinstance(ceil,Figure)
    # test ok
    def isEnemy(self, ceil, player):
        return self.isFigure(ceil) and player != ceil.player
        # return (player == 'White' and 'b' in str(ceil)) or (player == 'Black' and 'w' in str(ceil))

    def isMyFigure(self, ceil, player):
        return self.isFigure(ceil) and player == ceil.player
        # return (player == 'White' and 'w' in str(ceil)) or (player == 'Black' and 'b' in str(ceil))

    def getMyKing(self, player):
        # if not player:
        #     player = currentPlayer
        for y in range(self.height):
            for x in range(self.width):
                if type(self.state[y][x])== King and self.isMyFigure(self.state[y][x], player):
                    return self.state[y][x]

    def isEmptyCeil(self, ceil):
        return ceil == '0'

    def isFirstMove(self, y, x):
        return not ((y, x) in self.moved_figure)

    def getSize(self):
        return self.height, self.width

    def isCheck(self, player):
        king = self.getMyKing(player)
        self.check =self.whoCanKilled(king)