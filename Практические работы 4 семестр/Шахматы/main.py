import shutil
import os
import copy
from colorama import Fore
from colorama import Back


# table = f'''
# ╔══════════════╦══════════════╦══════════════╦══════════════╦══════════════╦══════════════╦══════════════╦══════════════╦══════════════╗
# ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║
# ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║
# ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║
# ║    @@  @@    ║    @@  @@    ║    @@  @@    ║    @@  @@    ║    @@  @@    ║    @@  @@    ║    @@  @@    ║    @@  @@    ║    @@  @@    ║
# ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║
# ╠══════════════╬══════════════╬══════════════╬══════════════╬══════════════╬══════════════╬══════════════╬══════════════╬══════════════╣
# ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║
# ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║
# ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║
# ║    @@  @@    ║    @@  @@    ║    @@  @@    ║    @@  @@    ║    @@  @@    ║    @@  @@    ║    @@  @@    ║    @@  @@    ║    @@  @@    ║
# ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║
# ╠══════════════╬══════════════╬══════════════╬══════════════╬══════════════╬══════════════╬══════════════╬══════════════╬══════════════╣
# ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║
# ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║
# ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║
# ║    @@  @@    ║    @@  @@    ║    @@  @@    ║    @@  @@    ║    @@  @@    ║    @@  @@    ║    @@  @@    ║    @@  @@    ║    @@  @@    ║
# ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║
# ╠══════════════╬══════════════╬══════════════╬══════════════╬══════════════╬══════════════╬══════════════╬══════════════╬══════════════╣
# ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║
# ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║
# ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║    @@@@@@    ║
# ║    @@  @@    ║    @@  @@    ║    @@  @@    ║    @@  @@    ║    @@  @@    ║    @@  @@    ║    @@  @@    ║    @@  @@    ║    @@  @@    ║
# ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║    @@   @@   ║
# ╠══════════════╬══════════════╬══════════════╬══════════════╬══════════════╬══════════════╬══════════════╬══════════════╬══════════════╣

# ║          ║          ║          ║          ║          ║
# ║          ║          ║          ║          ║          ║
# ║          ║          ║          ║          ║          ║
# ║          ║          ║          ║          ║          ║
# ╚══════════╩══════════╩══════════╩══════════╩══════════╝
# '''

#    A    B    C    D    E    F    G    H
# ╔════╦════╦════╦════╦════╦════╦════╦════╗
# ║ bR ║ bN ║ bB ║ bQ ║ bK ║ bB ║ bN ║ bR ║ 8
# ╠════╬════╬════╬════╬════╬════╬════╬════╣
# ║ bP ║ bP ║ bP ║ bP ║ bP ║ bP ║ bP ║ bP ║ 7
# ╠════╬════╬════╬════╬════╬════╬════╬════╣
# ║    ║    ║    ║    ║    ║    ║    ║    ║ 6
# ╠════╬════╬════╬════╬════╬════╬════╬════╣
# ║    ║    ║    ║    ║    ║    ║    ║    ║ 5
# ╠════╬════╬════╬════╬════╬════╬════╬════╣
# ║    ║    ║    ║    ║    ║    ║    ║    ║ 4
# ╠════╬════╬════╬════╬════╬════╬════╬════╣
# ║    ║    ║    ║    ║    ║    ║    ║    ║ 3
# ╠════╬════╬════╬════╬════╬════╬════╬════╣
# ║ wP ║ wP ║ wP ║ wP ║ wP ║ wP ║ wP ║ wP ║ 2
# ╠════╬════╬════╬════╬════╬════╬════╬════╣
# ║ wR ║ wN ║ wB ║ wQ ║ wK ║ wB ║ wN ║ wR ║ 1
# ╚════╩════╩════╩════╩════╩════╩════╩════╝
# White: ppBN, Black QNN

def showRules():
    os.system("cls")
    print("Шахматы".center(shutil.get_terminal_size().columns))
    print()
    print("Правила игры".center(shutil.get_terminal_size().columns))
    print(
        'Соперники ходят по очереди. Игрок может выбрать фигуру для которой есть хотя бы один ход.\n'+
        'Победителем является тот кто поставит мат противнику.\n'+
        'Также возможно ничья (пат), когда мат противнику не поставлен, но у него не осталось ходов.')
    print()
    print("Управление".center(shutil.get_terminal_size().columns))
    print("Для выбора фигуры введите одну из буквы: w,s,d,a и нажмите Enter")
    print("Затем чтобы зафиксировать выбор нажмите Enter")
    print("Для выбора хода фигуры введите одну из буквы: w,s,d,a и нажмите Enter")
    print("Затем чтобы зафиксировать выбор нажмите Enter")
    print("Для выхода из игры нажмите Ctrl+C")
    print()
    print("Что-бы запустить игру -нажмите Enter".center(shutil.get_terminal_size().columns))
    input()


defaultForeColor = Fore.CYAN
defaultBackColor = Back.BLACK
state = [[], []]
# выбранная фигура
current_figure = {'y': 7, 'x': 3}
# выбранный ход фигурой
current_position = {'y': 7, 'x': 3}
# фигуры сделавшие ход (y,x)
moved_figure = {(0, 0), (1, 2)}

currentPlayer = 'Black'
# currentForeColor = Fore.BLUE
# currentBackColor = Back.BLUE
playersCount = {'White': '', 'Black': '', }

# шах
check = False
# пешка сделал ход на две клетки вперёд, возможно взятие на проходе
pawnJump = False

# +
def init():
    global state
    global marker
    global currentPlayer
    global current_figure
    global current_position
    # global currentForeColor
    # global currentBackColor
    global moved_figure
    global playersCount
    global check

    state = [['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
             ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
             ['0'] * 8, ['0'] * 8, ['0'] * 8, ['0'] * 8,
             ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
             ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']]

    # # пат тест
    # state = [['0', '0', 'wQ', '0', '0', 'bB', 'bN', 'bR'],
    #          ['0', '0', '0', '0', 'bP', '0', 'bP', 'bQ'],
    #          ['0','0','0','0','0','bP','bK','bR'],
    #          ['0', '0', '0', '0', '0', '0', '0', 'bP'],
    #          ['0', '0', '0', '0', '0', '0', '0', 'wP'],
    #         ['0','0','0','0','wP','0','0','0'],
    #          ['wP', 'wP', 'wP', 'wP', '0', 'wP', 'wP', '0'],
    #          ['wR', 'wN', 'wB', '0', 'wK', 'wB', 'wN', 'wR']]
    # # тест рокировки
    # state = [['bR', '0', '0', '0', 'bK', '0', '0', 'bR'],
    #          ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
    #          ['0'] * 8, ['0'] * 8, ['0'] * 8, ['0'] * 8,
    #          ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
    #          ['wR', '0', '0', '0', 'wK', '0', '0', 'wR']]
    #
    # # тест рокировки перескок через биток поле
    # state = [['bR', '0', '0', '0', 'bK', '0', '0', 'bR'],
    #          ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
    #          ['bQ','0','0','0','0','0','0','0'],
    #          ['0'] * 8, ['0'] * 8, ['0'] * 8,
    #          ['wP', 'wP', 'wP', 'wP', '0', 'wP', 'wP', 'wP'],
    #          ['wR', '0', '0', '0', 'wK', '0', '0', 'wR']]
    #
    # # тест рокировки шах
    # state = [['bR', '0', '0', '0', 'bK', '0', '0', 'bR'],
    #          ['bP', 'bP', 'bP', 'bP', '0', 'bP', 'bP', 'bP'],
    #          ['bP', '0', '0', '0', 'bQ', '0', '0', '0'],
    #          ['0'] * 8, ['0'] * 8, ['0'] * 8,
    #          ['wP', 'wP', 'wP', 'wP', '0', 'wP', 'wP', 'wP'],
    #          ['wR', '0', '0', '0', 'wK', '0', 'wN', 'wR']]

    # print(' '.join(state[0][:]))
    current_figure = {'y': 6, 'x': 4}
    current_position = {'y': 6, 'x': 4}
    moved_figure = set()
    currentPlayer = 'White'
    # currentForeColor = Fore.GREEN
    # currentBackColor = Back.GREEN
    playersCount = {'White': '', 'Black': '', }
    check = False

# +
# test ok
def gameover():
    myFiguries = gelAllMyFiguries()
    for figure in myFiguries:
        # moves, kills = figureMovesWithCheck(figure)
        moves, kills = figureMoves(figure)
        if moves or kills:
            return False
    # print("GAMEOVER!")
    return True

# +
# test ok
def isEnemy(ceil, player=False):
    if not player:
        player = currentPlayer
    return (player == 'White' and 'b' in ceil) or (player == 'Black' and 'w' in ceil)

# +
# test ok
def isEmptyCeil(ceil):
    return ceil == '0'

# +
# test ok
def isFirstMove(y, x):
    return not ((y, x) in moved_figure)

# +
def isMyFigure(ceil, player=False):
    # print(player)
    # if (ceil == 'wN'):
    #     print(player)
    #     print(currentPlayer)
    if not player:
        player = currentPlayer
    return (player == 'White' and 'w' in ceil) or (player == 'Black' and 'b' in ceil)

# +
def getMyEnemy():
    if currentPlayer == 'White':
        return 'Black'
    else:
        return 'White'

# +
def myKingPosition(player=False):
    if not player:
        player = currentPlayer
    for y in range(8):
        for x in range(8):
            if 'K' in state[y][x] and isMyFigure(state[y][x], player):
                return y, x

# +
# test ok
def getAllEnemies(player=False):
    if not player:
        player = currentPlayer
    enemies = []
    for y in range(8):
        for x in range(8):
            if isEnemy(state[y][x], player):
                enemies.append((y, x))

    return enemies

# +
# test ok
def gelAllMyFiguries():
    return getAllEnemies(getMyEnemy())

# +
def whoCanKilled(aim):
    enemies = getAllEnemies(getPlayerByFigure(state[aim[0]][aim[1]]))
    # if (aim == (4,0)):
    #     print("ENEMY")
    #     print(enemies)
    killers = []
    for enemy in enemies:

        moves, kills = figureMoves(enemy, safe=False)
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

# +
def inSafe(aim, move=None, guard=None):
    global state
    saved_state = copy.deepcopy(state)
    if move:
        figure = state[aim[0]][aim[1]]
        state[aim[0]][aim[1]] = '0'
        state[move[0]][move[1]] = figure
    if guard:
        y, x, guard_move = guard
        # print(guard)
        # if currentPlayer == 'White':
        #     queen = 'wQ'
        # else:
        #     queen = 'bQ'
        state[guard_move[0]][guard_move[1]] = state[y][x]
        state[y][x] = '0'
    if move:
        result = not whoCanKilled(move)
    else:
        result = not whoCanKilled(aim)
    state = saved_state
    # if move:
    #     state[aim[0]][aim[1]] = figure
    #     state[move[0]][move[1]] = new_position

    return result

# +
# test ok
def getPlayerByFigure(figure):
    if 'w' in figure:
        return 'White'
    return 'Black'


# допустимые ходы, когда королю объявлен шах
# def figureMovesWithCheck(figurePosition=None):
# if not check:
#     return figureMoves(figurePosition)
# return figureMoves(figurePosition)

# if figurePosition:
#     y, x = figurePosition
# else:
#     y, x = current_figure['y'], current_figure['x']
#
# current = state[y][x]
# moves = []
# kills = []
# player = getPlayerByFigure(current)
#
# temp_moves, temp_kills = figureMoves(figurePosition)
# myKing = myKingPosition(player)

# if 'K' in current:
#     for move in temp_moves:
# #         if inSafe(myKing, move):
#         moves.append(move)
# #
#     for kill in temp_kills:
# #         if inSafe(myKing, kill):
#         kills.append(kill)
# else:
# # if not 'K' in current:
#     print("ELSE")
#     for move in temp_moves:
#         if inSafe(myKing, guard=(y, x , move)):
#             moves.append(move)
#
#     for kill in temp_kills:
#         if inSafe(myKing, guard=(y, x ,kill)):
#             kills.append(kill)

# return temp_moves, temp_kills


# figurePosition y,x
# +
def figureMoves(figurePosition=None, safe=True):
    if figurePosition:
        y, x = figurePosition
    else:
        y, x = current_figure['y'], current_figure['x']

    current = state[y][x]
    moves = []
    kills = []
    player = getPlayerByFigure(current)

    def getSafeMoves():
        safe_moves = []
        safe_kills = []
        myKing = myKingPosition(player)
        if 'K' in current:
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
                if inSafe(myKing, guard=(y, x, move)):
                    safe_moves.append(move)

            for kill in kills:
                if inSafe(myKing, guard=(y, x, kill)):
                    safe_kills.append(kill)

        return safe_moves, safe_kills

    def checkCeilForAction(y, x):
        if isEmptyCeil(state[y][x]):
            moves.append((y, x))
            return False
        else:
            if isEnemy(state[y][x], player):
                kills.append((y, x))
                # return True
        return True

    def getPawnAction():
        def getBlackPawnAction():
            # проверка возможности хода на одну клетку вперёд
            # нет проверки выходит, ли пешка за край доски, потому что она трансформируется в другую фигуру на крайней диагонали
            if isEmptyCeil(state[y + 1][x]):
                moves.append((y + 1, x))
            # проверка возможности хода на две клетки вперёд
            if isFirstMove(y, x) and isEmptyCeil(
                    state[y + 1][x]) and isEmptyCeil(
                state[y + 2][x]):
                moves.append((y + 2, x))
            # проверка возможности съесть фигуру справа от пешки
            if x != 7 and isEnemy(state[y + 1][x + 1], player):
                kills.append((y + 1, x + 1))
            # проверка возможности съесть фигуру слева от пешки
            if x != 0 and isEnemy(state[y + 1][x - 1], player):
                kills.append((y + 1, x - 1))
            # проверка возможности взятия на проходе
            if pawnJump and pawnJump[0] == y:
                # взятие на проходе справа
                if pawnJump[1] == x + 1:
                    kills.append((y + 1, x + 1))
                # взятие на проходе слева
                elif pawnJump[1] == x - 1:
                    kills.append((y + 1, x - 1))

        def getWhitePawnAction():
            # проверка возможности хода на одну клетку вперёд
            if isEmptyCeil(state[y - 1][x]):
                moves.append((y - 1, x))
            # проверка возможности хода на две клетки вперёд
            if isFirstMove(y, x) and isEmptyCeil(
                    state[y - 1][x]) and isEmptyCeil(
                state[y - 2][x]):
                moves.append((y - 2, x))
            # проверка возможности съесть фигуру справа от пешки
            if x != 7 and isEnemy(state[y - 1][x + 1], player):
                kills.append((y - 1, x + 1))
            # проверка возможности съесть фигуру слева от пешки
            if x != 0 and isEnemy(state[y - 1][x - 1], player):
                kills.append((y - 1, x - 1))
            # проверка возможности взятия на проходе
            if pawnJump and pawnJump[0] == y:
                # взятие на проходе справа
                if pawnJump[1] == x + 1:
                    kills.append((y - 1, x + 1))
                # взятие на проходе слева
                elif pawnJump[1] == x - 1:
                    kills.append((y - 1, x - 1))

        if player == 'White':
            getWhitePawnAction()
        else:
            getBlackPawnAction()

    def getBishopAction():
        # проверка возможности хода вниз и вправо
        for i, j in zip(range(y + 1, 8), range(x + 1, 8)):
            if checkCeilForAction(i, j):
                break
        # проверка возможности хода вверх и вправо
        for i, j in zip(range(y - 1, -1, -1), range(x + 1, 8)):
            if checkCeilForAction(i, j):
                break
        # проверка возможности хода вверх и влево
        for i, j in zip(range(y - 1, -1, -1), range(x - 1, -1, -1)):
            if checkCeilForAction(i, j):
                break
        # проверка возможности хода вниз и влево
        for i, j in zip(range(y + 1, 8), range(x - 1, -1, -1)):
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
        for j in range(x + 1, 8):
            if checkCeilForAction(y, j):
                break
        # проверка возможности хода влево
        for j in range(x - 1, -1, -1):
            if checkCeilForAction(y, j):
                break
        # проверка возможности хода вниз
        for i in range(y + 1, 8):
            if checkCeilForAction(i, x):
                break
        # проверка возможности хода вверх
        for i in range(y - 1, -1, -1):
            if checkCeilForAction(i, x):
                break

    def find_neighbors(i, j, dist=1):
        # range(max(0, i - 1):min(i + dist+1,8)
        result = set()
        for y in range(max(0, i - dist), min(i + dist + 1, 8)):
            for x in range(max(0, j - dist), min(j + dist + 1, 8)):
                result.add((y, x))
        result.remove((i, j))
        return result
        # return [row[max(0, j - dist):j + dist] for row in m[max(0, i - 1):i + dist]]

    def getKingAction():
        def checkCastling():
            def checkLongCastling():
                if isFirstMove(y, x) and isFirstMove(y, 0):
                    if isEmptyCeil(state[y][x - 1]) and isEmptyCeil(state[y][x - 2]) and isEmptyCeil(state[y][x - 3]):
                        if safe:
                            if (not inSafe((y, x), (y, x - 1))) or (not inSafe((y, x), (y, x - 2))):
                                return
                        # if inSafe((y, x), (y, x - 1)):
                        moves.append((y, x - 2))

            def checkShortCastling():
                # print("check short")
                if isFirstMove(y, x) and isFirstMove(y, 7):
                    # print("1 short")
                    # print(state[y][x+1])
                    # print(state[y][x + 2])
                    # print(isEmptyCeil((y,x+1)))
                    # print(isEmptyCeil((y, x + 2)))
                    if isEmptyCeil(state[y][x + 1]) and isEmptyCeil(state[y][x + 2]):
                        # print("2 short")
                        # if inSafe((y,x),(y,x+1)):
                        if safe:
                            if not inSafe((y, x), (y, x + 1)):
                                return
                        moves.append((y, x + 2))

            checkLongCastling()
            checkShortCastling()

        neighbors = find_neighbors(y, x)
        for move in neighbors:
            if safe:
                if not inSafe((y, x), move):
                    continue
            checkCeilForAction(*move)

        # рокировку нельзя делать под шахом
        #  and (player == currentPlayer)
        if not check:
            checkCastling()
        # if x != 7 and inSafe((y,x),(y,x+1)):
        #     checkCeilForAction(y,x+1)
        # if x != 0 and inSafe((y,x),(y,x-1)):
        #     checkCeilForAction(y,x-1)

    # проверка возможности ходов для пешки
    if 'P' in current:
        getPawnAction()
    # проверка возможности ходов для слона
    elif 'B' in current:
        getBishopAction()
    # проверка возможности ходов для коня
    elif 'N' in current:
        getKnightAction()
    # проверка возможности ходов для ферзя
    elif 'Q' in current:
        getQueenAction()
    # проверка возможности ходов для ладьи
    elif 'R' in current:
        getRookAction()
    # проверка возможности ходов для короля
    elif 'K' in current:
        getKingAction()

    if safe:
        return getSafeMoves()
    return moves, kills

# +
# отобразить возможные ходы и выбор хода (position)
def getFullState(drawMoves=True, position=True):
    # if not (drawMoves or moveMode):

    # показать текущие ходы, position = TRUE показать перемещение фигуры (при выборе хода)
    def getStateWithMoves():
        # moves, kills = figureMovesWithCheck()
        moves, kills = figureMoves()
        fullState = copy.deepcopy(state)
        for y, x in moves:
            fullState[y][x] = 'm'
        for y, x in kills:
            fullState[y][x] = 'k' + fullState[y][x]
        # if check:
        #     y, x = myKingPosition()
        #     fullState[y][x] = 's'+ fullState[y][x]

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

# +
def getTableContent(drawMoves=True, position=True):
    def getCellStyle(cell):
        def getCurrentColor():
            if 'w' in cell:
                return Fore.BLUE, Back.BLUE
            elif 'b' in cell:
                return Fore.GREEN, Back.GREEN
            elif currentPlayer == 'White':
                return Fore.BLUE, Back.BLUE
            else:
                return Fore.GREEN, Back.GREEN

        currentForeColor, currentBackColor = getCurrentColor()

        # пустая клетка
        if cell == '0':
            return '    '
        # взятие на проходе
        elif cell == 'k0':
            return Back.RED + '    ' + Back.RESET
        # возможный ход
        elif 'm' in cell:
            return currentBackColor + '    ' + Back.RESET
        # фигуры под боем
        # 1:3 cswK acwN
        elif cell.startswith('k'):
            return Back.RED + ' ' + Fore.BLACK + cell[-2:] + defaultForeColor + ' ' + Back.RESET
        # текущая фигура
        elif cell.startswith('c'):
            # print(cell[-2:])
            return currentBackColor + ' ' + Fore.BLACK + cell[-2:] + defaultForeColor + ' ' + Back.RESET
        # шах
        elif cell.startswith('a') and 'K' in cell:
            return Back.MAGENTA + ' ' + Fore.BLACK + cell[-2:] + defaultForeColor + ' ' + Back.RESET
        # aim фигуру которую может съесть противник на следующем ходу
        elif cell.startswith('a'):
            return ' ' + Fore.RED + cell[-2:] + defaultForeColor + ' '
        # обычные фигуры
        else:
            return ' ' + currentForeColor + cell + defaultForeColor + ' '

    fullState = getFullState(drawMoves, position)
    # print("FULLSTATE")
    # print(fullState)
    tableContent = [[getCellStyle(fullState[i][j]) for j in range(8)] for i in range(8)]

    return tableContent

# +
def draw(tableContent):
    # print(tableContent)
    def getRow(row):
        result = "\n\t║"
        for j in range(8):
            # for j in range(5):
            # print(tableContent[index][j][i])
            result += tableContent[row][j] + "║"
        return result

    # print('-1')
    table = f'''{defaultForeColor}
\t   A    B    C    D    E    F    G    H
\t╔════╦════╦════╦════╦════╦════╦════╦════╗'''
    for i in range(8):
        # print(i)
        table += getRow(i) + ' ' + str(8 - i)
        if i < 7:
            table += '\n\t╠════╬════╬════╬════╬════╬════╬════╬════╣'
        else:
            table += f'''\n\t╚════╩════╩════╩════╩════╩════╩════╩════╝{Fore.WHITE}'''

    # {getRow(0)}
    # \t╠══════════╬══════════╬══════════╬══════════╬══════════╣{getRow(1)}
    # \t╠══════════╬══════════╬══════════╬══════════╬══════════╣{getRow(2)}
    # \t╠══════════╬══════════╬══════════╬══════════╬══════════╣{getRow(3)}
    # \t╚══════════╩══════════╩══════════╩══════════╩══════════╝{Fore.WHITE}'''

    os.system("cls")
    # print('1')
    print(table)

# +
# test ok
def showPlayerCount():
    print(f"\t{Fore.BLUE}White: {playersCount['White']}\n\t{Fore.GREEN}Black: {playersCount['Black']}{Fore.RESET}")

# +
def canMove(figurePosition=None):
    # moves, kills = figureMovesWithCheck(figurePosition)
    moves, kills = figureMoves(figurePosition)
    # print(moves, kills)
    return moves or kills

# +
# выбор своей фигуры для хода
# возможно следует добавить метод canMove() для проверки есть ли у фигуры ходы if myFigure(state[i][j]) and canMove(state[i][j])
def selectFigure():
    # print("select f")
    # print(currentPlayer)
    while True:
        # print(currentPlayer)
        # print(state)
        command = input()
        if command == "d":
            # print("d"+currentPlayer)
            for j in range(current_figure['x'] + 1, 8):
                if isMyFigure(state[current_figure['y']][j]):
                    current_figure['x'] = j
                    if canMove():
                        # print("selected"+str(i)+" "+str(j))
                        break
            else:
                # for i in range(8):
                for i in range(current_figure['y'] + 1, 8):
                    for j in range(8):

                        if isMyFigure(state[i][j]):
                            current_figure['y'] = i
                            current_figure['x'] = j
                            if canMove():
                                # print("selected" + str(i) + " " + str(j))
                                break
                    else:
                        continue
                    break
                else:
                    for i in range(0, current_figure['y'] + 1):
                        for j in range(8):

                            if isMyFigure(state[i][j]):
                                current_figure['y'] = i
                                current_figure['x'] = j
                                if canMove():
                                    # print("selected" + str(i) + " " + str(j))
                                    break
                        else:
                            continue
                        break
        elif command == "s":
            for i in range(current_figure['y'] + 1, 8):
                if isMyFigure(state[i][current_figure['x']]):
                    current_figure['y'] = i
                    if canMove():
                        break
            else:
                for j in range(current_figure['x'] + 1, 8):
                    # for j in range(8):
                    for i in range(8):
                        if isMyFigure(state[i][j]):
                            current_figure['y'] = i
                            current_figure['x'] = j
                            if canMove():
                                break
                    else:
                        continue
                    break
                else:
                    for j in range(0, current_figure['x'] + 1):
                        # for j in range(8):
                        for i in range(8):
                            if isMyFigure(state[i][j]):
                                current_figure['y'] = i
                                current_figure['x'] = j
                                if canMove():
                                    break
                        else:
                            continue
                        break
        elif command == "a":
            for j in range(current_figure['x'] - 1, -1, -1):
                if isMyFigure(state[current_figure['y']][j]):
                    current_figure['x'] = j
                    if canMove():
                        break
            else:
                # for i in range(7, -1, -1):
                for i in range(current_figure['y'] - 1, -1, -1):
                    for j in range(7, -1, -1):
                        # print(str(i) + str(j))
                        if isMyFigure(state[i][j]):
                            # print("TTT"+state[i][j])
                            current_figure['y'] = i
                            current_figure['x'] = j
                            if canMove():
                                break
                    else:
                        continue
                    break
                else:
                    for i in range(7, current_figure['y'] - 1, -1):
                        # print("AAAA")
                        for j in range(7, -1, -1):
                            if isMyFigure(state[i][j]):
                                current_figure['y'] = i
                                current_figure['x'] = j
                                if canMove():
                                    # print("selected" + str(i) + " " + str(j))
                                    break
                        else:
                            continue
                        break
        elif command == "w":

            for i in range(current_figure['y'] - 1, -1, -1):
                if isMyFigure(state[i][current_figure['x']]):
                    current_figure['y'] = i
                    if canMove():
                        break
            else:
                for j in range(current_figure['x'] - 1, -1, -1):
                    # for j in range(7, -1, -1):
                    for i in range(7, -1, -1):
                        if isMyFigure(state[i][j]):
                            current_figure['y'] = i
                            current_figure['x'] = j
                            if canMove():
                                break
                    else:
                        continue
                    break
                else:
                    for j in range(7, current_figure['x'] - 1, -1):
                        # for j in range(7, -1, -1):
                        for i in range(7, -1, -1):
                            if isMyFigure(state[i][j]):
                                current_figure['y'] = i
                                current_figure['x'] = j
                                if canMove():
                                    break
                        else:
                            continue
                        break
        elif command == '':
            # state[marker['x']][marker['y']] = currentPlayer
            # changePlayerCount()
            break
        draw(getTableContent(position=False))
        showPlayerCount()

# +
def isMyFigureArea(ceil):
    # print(ceil)
    return ('m' in ceil) or ('k' in ceil)

# +
def moveFigure():
    # print("move f")
    def nextPlayer():
        global currentPlayer
        if currentPlayer == 'White':
            currentPlayer = 'Black'
        else:
            currentPlayer = 'White'
        # print("new Current player:"+currentPlayer)

    def newMarker():
        for i in range(8):
            for j in range(8):
                if isMyFigure(state[i][j]):
                    current_figure['y'] = current_position['y'] = i
                    current_figure['x'] = current_position['x'] = j
                    if canMove():
                        return

    # синхронизация (так как в select figure меняется только current_figure)
    current_position['y'] = current_figure['y']
    current_position['x'] = current_figure['x']

    while True:
        state = getFullState(True, True)
        # print(state)
        command = input()
        if command == "d":
            for j in range(current_position['x'] + 1, 8):
                if isMyFigureArea(state[current_position['y']][j]):
                    current_position['x'] = j
                    break
            else:
                for i in range(current_position['y'] + 1, 8):
                    # for i in range(8):
                    for j in range(8):
                        if isMyFigureArea(state[i][j]):
                            current_position['y'] = i
                            current_position['x'] = j
                            break
                    else:
                        continue
                    break
                else:
                    for i in range(0, current_figure['y'] + 1):
                        for j in range(8):
                            if isMyFigureArea(state[i][j]):
                                current_position['y'] = i
                                current_position['x'] = j
                                break
                        else:
                            continue
                        break
        elif command == "s":
            # print(state)
            for i in range(current_position['y'] + 1, 8):
                # print("fl do it" + str(i))
                if isMyFigureArea(state[i][current_position['x']]):
                    # print("do it"+str(i))
                    current_position['y'] = i
                    break
            else:
                for j in range(current_position['x'] + 1, 8):
                    # for j in range(8):
                    for i in range(8):
                        if isMyFigureArea(state[i][j]):
                            current_position['y'] = i
                            current_position['x'] = j
                            break
                    else:
                        continue
                    break
                else:
                    for j in range(0, current_figure['x'] + 1):
                        for i in range(8):
                            if isMyFigureArea(state[i][j]):
                                current_position['y'] = i
                                current_position['x'] = j
                                break
                        else:
                            continue
                        break

        elif command == "a":
            for j in range(current_position['x'] - 1, -1, -1):
                if isMyFigureArea(state[current_position['y']][j]):
                    current_position['x'] = j
                    break
            else:
                for i in range(current_position['y'] - 1, -1, -1):
                    # for i in range(7, -1, -1):
                    for j in range(7, -1, -1):
                        if isMyFigureArea(state[i][j]):
                            current_position['y'] = i
                            current_position['x'] = j
                            break
                    else:
                        continue
                    break
                else:
                    for i in range(7, current_figure['y'] - 1, -1):
                        for j in range(7, -1, -1):
                            if isMyFigureArea(state[i][j]):
                                current_position['y'] = i
                                current_position['x'] = j
                                break
                        else:
                            continue
                        break
        elif command == "w":
            for i in range(current_position['y'] - 1, -1, -1):
                if isMyFigureArea(state[i][current_position['x']]):
                    current_position['y'] = i
                    break
            else:
                for j in range(current_position['x'] - 1, -1, -1):
                    # for j in range(7, -1, -1):
                    for i in range(7, -1, -1):
                        if isMyFigureArea(state[i][j]):
                            current_position['y'] = i
                            current_position['x'] = j
                            break
                    else:
                        continue
                    break
                else:
                    for j in range(7, current_figure['x'] - 1, -1):
                        for i in range(7, -1, -1):
                            if isMyFigureArea(state[i][j]):
                                current_position['y'] = i
                                current_position['x'] = j
                                break
                        else:
                            continue
                        break
        elif command == '':
            if current_figure == current_position:
                # print("ret f")
                return True

            move()

            break
        elif command == 'q':
            return True
        draw(getTableContent())
        showPlayerCount()
    nextPlayer()
    newMarker()
    return True

# +
def transformPawn():
    while True:
        print("Замена пешки, выберите одну из фигур: q,r,n,b")
        figure = input()
        if figure in "qQrRnNbB":
            if currentPlayer == 'White':
                return 'w' + figure.upper()
            else:
                return 'b' + figure.upper()

# +
# рокировка (передвигаем ладью), король движется в методе move
def castling(short=True):
    if currentPlayer == 'White':
        # короткая рокировка
        if short:
            state[7][5] = state[7][7]
            state[7][7] = '0'
        # длиная
        else:
            state[7][3] = state[7][0]
            state[7][0] = '0'
    else:
        # короткая рокировка
        if short:
            state[0][5] = state[0][7]
            state[0][7] = '0'
        # длиная
        else:
            state[0][3] = state[0][0]
            state[0][0] = '0'

# +
def isCheck():
    king = myKingPosition(getMyEnemy())
    return whoCanKilled(king)

# +
# приватный метод
def move():
    global check
    global pawnJump

    def isPawnJump():
        # если пешка
        if 'P' in figure:
            if (current_position['y'] - current_figure['y'] == 2) or (current_figure['y'] - current_position['y'] == 2):
                # print("PAWN JUMP!")
                return (current_position['y'], current_position['x'])
        return False

    # произошло ли взятие на проходе
    def checkPawnCapturing():
        nonlocal current
        if pawnJump and ('P' in figure):
            if 'b' in figure:
                if pawnJump[1] == current_position['x'] and pawnJump[0] + 1 == current_position['y']:
                    state[current_position['y'] - 1][current_position['x']] = '0'
                    current = 'wP'
            else:
                if pawnJump[1] == current_position['x'] and pawnJump[0] - 1 == current_position['y']:
                    state[current_position['y'] + 1][current_position['x']] = '0'
                    current = 'bP'

    # новая позиция фигуры
    current = state[current_position['y']][current_position['x']]
    # прошлая позиция
    figure = state[current_figure['y']][current_figure['x']]

    # отмечаем, что фигура сделала ход, это нужно для рокировки, или хода на две клетки вперёд у пешки, взятие на проходе
    # moved_figure.add((current_figure['y'], current_figure['x']))
    moved_figure.add((current_position['y'], current_position['x']))

    # print("moved figure")
    # print(moved_figure)

    checkPawnCapturing()
    print(current)
    # фигура бьёт другую
    if 'w' in current or 'b' in current:
        # print("WTF")
        # взятие на проходе
        # if current == '0':
        #
        #     if 'b' in current:
        #         playersCount[currentPlayer] += state[current_position['y'] + 1][current_position['x']]
        #         state[current_position['y'] + 1][current_position['x']] = '0'
        #     else:
        #         playersCount[currentPlayer] += state[current_position['y'] - 1][current_position['x']]
        #         state[current_position['y'] - 1][current_position['x']] = '0'
        # # другие случаи
        # else:
        # print("KILLED"+current+"!")
        playersCount[currentPlayer] += current[-1]

    # пешка дошла до края доски
    if 'P' in figure:
        if (currentPlayer == 'White' and current_position['y'] == 0) or (
                currentPlayer == 'Black' and current_position['y'] == 7):
            figure = transformPawn()

    # обработка рокировки
    if 'K' in figure:
        if current_position['x'] - current_figure['x'] == 2:
            castling()
        elif current_figure['x'] - current_position['x'] == 2:
            castling(False)

    state[current_position['y']][current_position['x']] = figure
    state[current_figure['y']][current_figure['x']] = '0'

    # проверить сделала ли пешка ход на два шага вперёд, необходимо для проверки возможности взятия на проходе
    pawnJump = isPawnJump()

    # проверить привёл ли ход к шаху
    check = isCheck()

# +
def showWinner():
    # мат
    if check:
        if currentPlayer == 'White':
            print("Black win!")
        else:
            print("White win!")
    # пат
    else:
        print('draw')

# +
def game():
    try:
        showRules()
        while True:
            init()

            while not gameover():
                draw(getTableContent(position=False))
                showPlayerCount()
                selectFigure()
                # while not moveFigure():
                #     pass
                moveFigure()
                # print(state)

            # move()
            # state[marker['x']][marker['y']] = currentPlayer
            # changePlayerCount()
            draw(getTableContent(False))
            showPlayerCount()
            showWinner()
            input()
    except KeyboardInterrupt:
        exit(0)


if __name__ == '__main__':
    game()
    # if {'y': 0, 'x': 0}:
    #     print(True)
