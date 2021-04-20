import copy
from chess.figures.Bishop import Bishop
from chess.figures.Queen import Queen
from chess.figures.Knight import Knight
from chess.figures.Rock import Rock
from chess.figures.King import King
from chess.figures.Pawn import Pawn

class Controller:
    def __init__(self, board):
        self.board = board
        self.lastFigureMoved = None

    def figureMoves(self, figurePosition=None, safe=True):
        if figurePosition:
            y, x = figurePosition
        else:
            y, x = self.board.current_figure.y, self.board.current_figure.x

        current = self.board.state[y][x]
        moves = []
        kills = []
        player = current.player

        def getSafeMoves():
            safe_moves = []
            safe_kills = []
            myKing = self.board.getMyKing(player)
            if type(current) == King:
                for move in moves:
                    #         if inSafe(myKing, move):
                    safe_moves.append(move)
                #
                for kill in kills:
                    #         if inSafe(myKing, kill):
                    safe_kills.append(kill)
            else:
                # if not 'K' in current:
                # print("ELSE")
                for move in moves:
                    # if inSafe(myKing, guard=(y, x, move)):
                    if self.inSafe(myKing, guard=(current, move)):
                        safe_moves.append(move)

                for kill in kills:
                    # if inSafe(myKing, guard=(y, x, kill)):
                    if self.inSafe(myKing, guard=(current, kill)):
                        safe_kills.append(kill)

            return safe_moves, safe_kills

        def checkCeilForAction(y, x):
            if self.board.isEmptyCeil(self.board.state[y][x]):
                moves.append((y, x))
                return False
            else:
                if self.board.isEnemy(self.board.state[y][x], player):
                    kills.append((y, x))
                    # return True
            return True

        def getPawnAction():
            def getBlackPawnAction():
                # проверка возможности хода на одну клетку вперёд
                # нет проверки выходит, ли пешка за край доски, потому что она трансформируется в другую фигуру на крайней диагонали
                if self.board.isEmptyCeil(self.board.state[y + 1][x]):
                    moves.append((y + 1, x))
                # проверка возможности хода на две клетки вперёд
                if self.board.isFirstMove(y, x) and self.board.isEmptyCeil(
                        self.board.state[y + 1][x]) and self.board.isEmptyCeil(
                    self.board.state[y + 2][x]):
                    moves.append((y + 2, x))
                # проверка возможности съесть фигуру справа от пешки
                if x != self.board.width -1  and self.board.isEnemy(self.board.state[y + 1][x + 1], player):
                    kills.append((y + 1, x + 1))
                # проверка возможности съесть фигуру слева от пешки
                if x != 0 and self.board.isEnemy(self.board.state[y + 1][x - 1], player):
                    kills.append((y + 1, x - 1))
                # # проверка возможности взятия на проходе
                # if pawnJump and pawnJump[0] == y:
                #     # взятие на проходе справа
                #     if pawnJump[1] == x + 1:
                #         kills.append((y + 1, x + 1))
                #     # взятие на проходе слева
                #     elif pawnJump[1] == x - 1:
                #         kills.append((y + 1, x - 1))

                # проверка возможности взятия на проходе
                if type(self.lastFigureMoved) == Pawn and self.lastFigureMoved.jumped and y == self.lastFigureMoved.y:
                    # взятие на проходе справа
                    if self.lastFigureMoved.x == x + 1:
                        kills.append((y + 1, x + 1))
                    # взятие на проходе слева
                    elif self.lastFigureMoved.x == x - 1:
                        kills.append((y + 1, x - 1))



            def getWhitePawnAction():
                # проверка возможности хода на одну клетку вперёд
                if self.board.isEmptyCeil(self.board.state[y - 1][x]):
                    moves.append((y - 1, x))
                # проверка возможности хода на две клетки вперёд
                if self.board.isFirstMove(y, x) and self.board.isEmptyCeil(
                        self.board.state[y - 1][x]) and self.board.isEmptyCeil(
                    self.board.state[y - 2][x]):
                    moves.append((y - 2, x))
                # проверка возможности съесть фигуру справа от пешки
                if x != 7 and self.board.isEnemy(self.board.state[y - 1][x + 1], player):
                    kills.append((y - 1, x + 1))
                # проверка возможности съесть фигуру слева от пешки
                if x != 0 and self.board.isEnemy(self.board.state[y - 1][x - 1], player):
                    kills.append((y - 1, x - 1))
                # # проверка возможности взятия на проходе
                # if pawnJump and pawnJump[0] == y:
                #     # взятие на проходе справа
                #     if pawnJump[1] == x + 1:
                #         kills.append((y - 1, x + 1))
                #     # взятие на проходе слева
                #     elif pawnJump[1] == x - 1:
                #         kills.append((y - 1, x - 1))

                # проверка возможности взятия на проходе
                if type(self.lastFigureMoved) == Pawn and self.lastFigureMoved.jumped and y == self.lastFigureMoved.y:
                    # взятие на проходе справа
                    if self.lastFigureMoved.x == x + 1:
                        kills.append((y - 1, x + 1))
                    # взятие на проходе слева
                    elif self.lastFigureMoved.x == x - 1:
                        kills.append((y - 1, x - 1))

            if player == 'White':
                getWhitePawnAction()
            else:
                getBlackPawnAction()

        def getBishopAction():
            # проверка возможности хода вниз и вправо
            for i, j in zip(range(y + 1, self.board.height), range(x + 1, self.board.width)):
                if checkCeilForAction(i, j):
                    break
            # проверка возможности хода вверх и вправо
            for i, j in zip(range(y - 1, -1, -1), range(x + 1, self.board.width)):
                if checkCeilForAction(i, j):
                    break
            # проверка возможности хода вверх и влево
            for i, j in zip(range(y - 1, -1, -1), range(x - 1, -1, -1)):
                if checkCeilForAction(i, j):
                    break
            # проверка возможности хода вниз и влево
            for i, j in zip(range(y + 1, self.board.height), range(x - 1, -1, -1)):
                if checkCeilForAction(i, j):
                    break

        def getKnightAction():
            def knightMoves(y, x):
                return {(y + 2, x + 1), (y + 2, x - 1), (y - 2, x + 1), (y - 2, x - 1), (y + 1, x + 2), (y - 1, x + 2),
                        (y + 1, x - 2), (y - 1, x - 2)}

            moves = find_neighbors(y, x, 2).intersection(knightMoves(y, x))
            # print(find_neighbors(y, x,2))
            # print(moves)
            for move in moves:
                checkCeilForAction(*move)

        def getQueenAction():
            getRookAction()
            getBishopAction()

        def getRookAction():
            # проверка возможности хода вправо
            for j in range(x + 1, self.board.width):
                if checkCeilForAction(y, j):
                    break
            # проверка возможности хода влево
            for j in range(x - 1, -1, -1):
                if checkCeilForAction(y, j):
                    break
            # проверка возможности хода вниз
            for i in range(y + 1, self.board.height):
                if checkCeilForAction(i, x):
                    break
            # проверка возможности хода вверх
            for i in range(y - 1, -1, -1):
                if checkCeilForAction(i, x):
                    break

        def find_neighbors(i, j, dist=1):
            # range(max(0, i - 1):min(i + dist+1,8)
            result = set()
            for y in range(max(0, i - dist), min(i + dist + 1, self.board.height)):
                for x in range(max(0, j - dist), min(j + dist + 1, self.board.width)):
                    result.add((y, x))
            result.remove((i, j))
            return result
            # return [row[max(0, j - dist):j + dist] for row in m[max(0, i - 1):i + dist]]

        def getKingAction():
            def checkCastling():
                def checkLongCastling():
                    if self.board.isFirstMove(y, x) and self.board.isFirstMove(y, 0):
                        if self.board.isEmptyCeil(self.board.state[y][x - 1]) and self.board.isEmptyCeil(self.board.state[y][x - 2]) and self.board.isEmptyCeil(
                                self.board.state[y][x - 3]):
                            if safe:
                                # if (not self.inSafe((y, x), (y, x - 1))) or (not self.inSafe((y, x), (y, x - 2))):
                                if (not self.inSafe(current, (y, x - 1))) or (not self.inSafe(current, (y, x - 2))):
                                    return
                            # if inSafe((y, x), (y, x - 1)):
                            moves.append((y, x - 2))

                def checkShortCastling():
                    if self.board.isFirstMove(y, x) and self.board.isFirstMove(y, self.board.width-1):
                        if self.board.isEmptyCeil(self.board.state[y][x + 1]) and self.board.isEmptyCeil(self.board.state[y][x + 2]):
                            if safe:
                                # if not self.inSafe((y, x), (y, x + 1)):
                                if not self.inSafe(current, (y, x + 1)):
                                    return
                            moves.append((y, x + 2))

                checkLongCastling()
                checkShortCastling()

            neighbors = find_neighbors(y, x)

            for move in neighbors:
                if safe:
                    # if not self.inSafe((y, x), move):

                    if not self.inSafe(current, move):
                        continue
                checkCeilForAction(*move)

            # рокировку нельзя делать под шахом
            if not self.board.check:
                checkCastling()

        # проверка возможности ходов для пешки
        # if 'P' in current:
        if type(current) == Pawn:
            getPawnAction()
        # проверка возможности ходов для слона
        # elif 'B' in current:
        elif type(current) == Bishop:
            getBishopAction()
        # проверка возможности ходов для коня
        # elif 'N' in current:
        elif type(current) == Knight:
            getKnightAction()
        # проверка возможности ходов для ферзя
        # elif 'Q' in current:
        elif type(current) == Queen:
            getQueenAction()
        # проверка возможности ходов для ладьи
        # elif 'R' in current:
        elif type(current) == Rock:
            getRookAction()
        # проверка возможности ходов для короля
        # elif 'K' in current:
        elif type(current) == King:
            getKingAction()
            # if current.player == 'Black':
            #     print(moves)
            #     print(kills)

        if safe:
            return getSafeMoves()
        return moves, kills

    # aim == Figure , move ,
    def inSafe(self, aim, move=None, guard=None):
        saved_state = copy.deepcopy(self.board.state)
        save_position = aim.getPosition()
        save_guard_position = None
        if move:
            # figure = self.board.state[aim[0]][aim[1]]
            figure = aim
            self.board.state[aim.y][aim.x] = '0'
            self.board.state[move[0]][move[1]] = figure
            figure.y = move[0]
            figure.x = move[1]
        if guard:
            # global save_guard_position
            guard_figure, guard_move = guard
            self.board.state[guard_move[0]][guard_move[1]] = guard_figure
            self.board.state[guard_figure.y][guard_figure.x] = '0'
            save_guard_position = guard_figure.getPosition()
        if move:
            result = not self.board.whoCanKilled(self.board.state[move[0]][move[1]])
            aim.y = save_position[0]
            aim.x = save_position[1]
        else:
            if guard:
                guard_figure, guard_move = guard
                guard_figure.y = save_guard_position[0]
                guard_figure.x = save_guard_position[1]
            result = not self.board.whoCanKilled(aim)
        self.board.state = saved_state
        # if move:
        #     state[aim[0]][aim[1]] = figure
        #     state[move[0]][move[1]] = new_position

        return result

    def move(self, figure, position, killed=None):
        figureClasses = {'Queen': Queen, 'Knight': Knight, 'Bishop': Bishop, 'Rock': Rock}
        y,x = position
        if self.board.isFigure(self.board.state[y][x]):
            if not killed:
                killed = []
            killed.append(self.board.state[y][x])

        lastPosition = figure.getPosition()
        result = figure.move(position, self.lastFigureMoved, (self.board.getSize()))

        self.board.moved_figure.add(position)
        self.board.moved_figure.add(figure.getPosition())
        self.lastFigureMoved = figure
        self.board.state[lastPosition[0]][lastPosition[1]] = '0'
        self.board.state[figure.y][figure.x] = figure

        # print(result)
        if result["status"] == 'move':
            figure = self.board.state[result["data"]["figure"][0]][result["data"]["figure"][1]]
            position = result["data"]["position"]
            self.move(figure, position, killed)
        elif result["status"] == 'transform':
            self.board.state[figure.y][figure.x] = figureClasses[result["data"]](figure.getPosition(),figure.player)
        elif result["status"] == 'kill':
            if not killed:
                killed = []
            killed.append(self.board.state[result["data"][0]][result["data"][1]])
            self.board.state[result["data"][0]][result["data"][1]] = '0'

        # print("KILLED"+str(killed))
        return killed

    def canMove(self, figurePosition=None):
        # moves, kills = figureMovesWithCheck(figurePosition)
        moves, kills = self.figureMoves(figurePosition)
        # print(moves, kills)
        return moves or kills


