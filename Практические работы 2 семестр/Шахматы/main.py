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
    print()
    print("Правила игры".center(shutil.get_terminal_size().columns))
    print(
        'На поле, имеющем размер 4 на 5 клеток за один ход каждый игрок должен заполнить одну клетку своим символом. '
        'Игрок старается, чтобы его символы были как можно дальше друг от друга. В ходе игры ведется подсчет очков: '
        'за каждое соседство клеток с одинаковыми символами игроку, владельцу символа добавляется одно штрафное очко. '
        'Соседними считаются клетки, имеющие общую сторону или расположенные наискосок друг от друга. '
        'Выигрывает тот, у кого в конце игры меньше всего штрафных очков.')
    print()
    print("Управление".center(shutil.get_terminal_size().columns))
    print("Для выбора клетки вводить буквы: w,s,d,a и жмите Enter")
    print("Затем чтобы зафиксировать выбор нажмите Enter")
    print("Для выхода из игры нажмите Ctrl+C")
    print()
    print("Маркеры игроков".center(shutil.get_terminal_size().columns))
    tempStr = f'''
{Back.BLUE + ' ' * 10 + Back.RESET + ' '}{Fore.BLUE + '@' * 5 + ' ' * 5 + Fore.CYAN}
{Back.BLUE + ' ' * 10 + Back.RESET + ' '}{Fore.BLUE + ' ' * 5 + '@' * 5 + Fore.CYAN}
{Back.BLUE + ' ' * 10 + Back.RESET + ' '}{Fore.BLUE + '@' * 5 + ' ' * 5 + Fore.CYAN}
{Back.BLUE + ' ' * 10 + Back.RESET + ' '}{Fore.BLUE + ' ' * 5 + '@' * 5 + Fore.CYAN}'''
    print(tempStr)
    tempStr = f'''
{Back.GREEN + ' ' * 10 + Back.RESET + ' '}{Fore.GREEN + ' ' * 4 + '*' * 2 + ' ' * 4 + Fore.CYAN}
{Back.GREEN + ' ' * 10 + Back.RESET + ' '}{Fore.GREEN + ' ' * 3 + '*' * 4 + ' ' * 3 + Fore.CYAN}
{Back.GREEN + ' ' * 10 + Back.RESET + ' '}{Fore.GREEN + ' ' + '*' * 8 + ' ' + Fore.CYAN}
{Back.GREEN + ' ' * 10 + Back.RESET + ' '}{Fore.GREEN + '*' * 10 + Fore.CYAN}'''
    print(tempStr)
    print("Маркеры взятия и шаха".center(shutil.get_terminal_size().columns))
    tempStr = f'''
    {Back.RED + ' ' * 10 + Back.RESET + ' '}{Fore.RED + '+' * 6 + ' ' * 3 + '+' + Fore.CYAN}
    {Back.RED + ' ' * 10 + Back.RESET + ' '}{Fore.RED + '+' * 4 + ' ' * 4 + '+' * 2 + Fore.CYAN}
    {Back.RED + ' ' * 10 + Back.RESET + ' '}{Fore.RED + '+' * 2 + ' ' * 4 + '+' * 4 + Fore.CYAN}
    {Back.RED + ' ' * 10 + Back.RESET + ' '}{Fore.RED + '+' + ' ' * 3 + '+' * 6 + Fore.CYAN}'''
    print(tempStr)
    print()
    print("Что-бы запустить игру -нажмите Enter".center(shutil.get_terminal_size().columns))
    input()


defaultForeColor = Fore.CYAN
defaultBackColor = Back.BLACK
state = [[], []]
# выбранная фигура
current_figure = {'y': 6, 'x': 4}
# выбранный ход фигурой
current_position = {'y': 6, 'x': 4}
# фигуры сделавшие ход (y,x)
moved_figure = {(0, 0), (1, 2)}

currentPlayer = 'White'
# currentForeColor = Fore.BLUE
# currentBackColor = Back.BLUE
playersCount = {'White': '', 'Black': '', }

# шах
check = False
# пешка сделал ход на две клетки вперёд, возможно взятие на проходе
pawnJump = False


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
             ['wR', 'wN', 'wB', 'wQ', 'wKs', 'wB', 'wN', 'wR']]

    # print(' '.join(state[0][:]))
    current_figure = {'y': 0, 'x': 0}
    current_position = {'y': 0, 'x': 0}
    moved_figure = {}
    currentPlayer = 'White'
    # currentForeColor = Fore.GREEN
    # currentBackColor = Back.GREEN
    playersCount = {'White': '', 'Black': '', }
    check = False


def gameover():
    myFiguries = gelAllMyFiguries()
    for figure in myFiguries:
        moves, kills = figureMovesWithCheck(figure)
        if moves or kills:
            return False
    return True


def isEnemy(ceil, player=currentPlayer):
    return (player == 'White' and 'b' in ceil) or (player == 'Black' and 'w' in ceil)


def isEmptyCeil(ceil):
    return ceil == '0'


def isFirstMove(y, x):
    return not ((y, x) in moved_figure)


def isMyFigure(ceil, player=currentPlayer):
    return (player == 'White' and 'w' in ceil) or (player == 'Black' and 'b' in ceil)


def getMyEnemy():
    if currentPlayer == 'White':
        return 'Black'
    else:
        return 'White'


def myKingPosition(player=currentPlayer):
    for y in range(8):
        for x in range(8):
            if 'K' in state[y][x] and isMyFigure(state[y][x], player):
                return y, x


def getAllEnemies(player=currentPlayer):
    enemies = []
    for y in range(8):
        for x in range(8):
            if isEnemy(state[y][x], player):
                enemies.append((y, x))

    return enemies


def gelAllMyFiguries():
    return getAllEnemies(getMyEnemy())


def whoCanKilled(aim):
    enemies = getAllEnemies(getPlayerByFigure(state[aim[0]][aim[1]]))
    killers = []
    for enemy in enemies:
        moves, kills = figureMoves(enemy)
        for move in moves:
            if move == aim:
                killers.append(enemy)
        for kill in kills:
            if kill == aim:
                killers.append(enemy)

    return killers


def inSafe(aim, move=None, guard=None):
    global state
    saved_state = copy.deepcopy(state)
    if move:
        figure = state[aim[0]][aim[1]]
        state[aim[0]][aim[1]] = '0'
        state[move[0]][move[1]] = figure

    if guard:
        if currentPlayer == 'White':
            queen = 'wQ'
        else:
            queen = 'bQ'
        state[guard[0]][guard[1]] = queen

    result = not whoCanKilled(aim)
    state = saved_state
    # if move:
    #     state[aim[0]][aim[1]] = figure
    #     state[move[0]][move[1]] = new_position

    return result


def getPlayerByFigure(figure):
    if 'w' in figure:
        return 'White'
    return 'Black'


# допустимые ходы, когда королю объявлен шах
def figureMovesWithCheck(figurePosition=None):
    if not check:
        return figureMoves(figurePosition)

    if figurePosition:
        y, x = figurePosition
    else:
        y, x = current_figure['y'], current_figure['x']

    current = state[y][x]
    moves = []
    kills = []
    player = getPlayerByFigure(current)

    temp_moves, temp_kills = figureMoves(figurePosition)
    myKing = myKingPosition(player)

    if 'K' in current:
        for move in temp_moves:
            if inSafe(myKing, move):
                moves.append(move)

        for kill in temp_kills:
            if inSafe(myKing, kill):
                kills.append(kill)
    else:
        for move in temp_moves:
            if inSafe(myKing, guard=move):
                moves.append(move)

        for kill in temp_kills:
            if inSafe(myKing, guard=kill):
                kills.append(kill)

    return moves, kills


# figurePosition y,x
def figureMoves(figurePosition=None):
    if figurePosition:
        y, x = figurePosition
    else:
        y, x = current_figure['y'], current_figure['x']

    current = state[y][x]
    moves = []
    kills = []
    player = getPlayerByFigure(current)

    def checkCeilForAction(y, x):
        if isEmptyCeil(state[y][x]):
            moves.append((y, x))
            return True
        else:
            if isEnemy(state[y][x], player):
                kills.append((y, x))
            return False

    def getPawnAction():
        def getBlackPawnAction():
            # проверка возможности хода на одну клетку вперёд
            # нет проверки выходит, ли пешка за край доски, потому что она трансформируется в другую фигуру на крайней диагонали
            if isEmptyCeil(state[y + 1][x]):
                moves.append((y + 1, x))
            # проверка возможности хода на две клетки вперёд
            if isFirstMove(y, x) and isEmptyCeil(
                    state[y + 2][x]):
                moves.append((y + 2, x))
            # проверка возможности съесть фигуру справа от пешки
            if x != 7 and isEnemy(state[y + 1][x + 1], player):
                kills.append((y + 1, x + 1))
            # проверка возможности съесть фигуру слева от пешки
            if x != 0 and isEnemy(state[y + 1][x - 1], player):
                kills.append((y + 1, x + 1))
            # проверка возможности взятия на проходе
            if pawnJump and pawnJump['y'] == y:
                # взятие на проходе справа
                if pawnJump['x'] == x + 1:
                    kills.append((y + 1, x + 1))
                # взятие на проходе слева
                elif pawnJump['x'] == x - 1:
                    kills.append((y + 1, x - 1))

        def getWhitePawnAction():
            # проверка возможности хода на одну клетку вперёд
            if isEmptyCeil(state[y - 1][x]):
                moves.append((y - 1, x))
            # проверка возможности хода на две клетки вперёд
            if isFirstMove(y, x) and isEmptyCeil(
                    state[y - 2][x]):
                moves.append((y - 2, x))
            # проверка возможности съесть фигуру справа от пешки
            if x != 7 and isEnemy(state[y - 1][x + 1], player):
                kills.append((y - 1, x + 1))
            # проверка возможности съесть фигуру слева от пешки
            if x != 0 and isEnemy(state[y - 1][x - 1], player):
                kills.append((y - 1, x + 1))
            # проверка возможности взятия на проходе
            if pawnJump and pawnJump['y'] == y:
                # взятие на проходе справа
                if pawnJump['x'] == x + 1:
                    kills.append((y - 1, x + 1))
                # взятие на проходе слева
                elif pawnJump['x'] == x - 1:
                    kills.append((y - 1, x - 1))

        if currentPlayer == 'White':
            return getWhitePawnAction()
        else:
            return getBlackPawnAction()

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
            if checkCeilForAction(j, j):
                break
        # проверка возможности хода вниз и влево
        for i, j in zip(range(y + 1, 8), range(x - 1, -1, -1)):
            if checkCeilForAction(j, j):
                break

    def getKnightAction():
        def knightMoves(y, x):
            return {(y + 2, x + 1), (y + 2, x - 1), (y - 2, x + 1), (y - 2, x - 1), (y + 1, x + 2), (y - 1, x + 2),
                    (y + 1, x - 2), (y - 1, x - 2)}

        moves = find_neighbors(y, x,2).intersection(knightMoves(y,x))
        for move in moves:
            checkCeilForAction(move)

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
        # проверка возможности хода ыниз
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
        for y in range(max(0, i - 1), min(i + dist + 1, 8)):
            for x in range(max(0, j - dist), min(j + dist + 1, 8)):
                result.add((y, x))
        result.remove((i, j))
        return result
        # return [row[max(0, j - dist):j + dist] for row in m[max(0, i - 1):i + dist]]

    def getKingAction():
        def checkCastling():
            def checkLongCastling():
                if isFirstMove(y, x) and isFirstMove(y, 0):
                    if isEmptyCeil((y, x - 1)) and isEmptyCeil((y, x - 2)) and isEmptyCeil((y, x - 3)):
                        if inSafe((y, x), (y, x - 1)):
                            moves.append((y, x - 2))
            def checkShortCastling():
                if isFirstMove(y, x) and isFirstMove(y, 7):
                    if isEmptyCeil((y,x+1)) and isEmptyCeil((y,x+2)):
                        if inSafe((y,x),(y,x+1)):
                            moves.append((y, x+2))

            checkLongCastling()
            checkShortCastling()

        neighbors = find_neighbors(y, x)
        for move in neighbors:
            if inSafe((y, x), move):
                checkCeilForAction(y, move)

        # рокировку нельзя делать под шахом
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

    return moves, kills


# def figureMoves():
#     current = state[current_figure['y']][current_figure['x']]
#     moves = []
#     kills = []
#
#     def checkCeilForAction(y, x):
#         if isEmptyCeil(state[y][x]):
#             moves.append((y, x))
#             return True
#         else:
#             if isEnemy(state[y][x]):
#                 kills.append((y, x))
#             return False
#
#     def getPawnAction():
#         def getBlackPawnAction():
#             pass
#
#         def getWhitePawnAction():
#             # проверка возможности хода на одну клетку вперёд
#             if isEmptyCeil(state[current_figure['y'] + 1][current_figure['x']]):
#                 moves.append((current_figure['y'] + 1, current_figure['x']))
#             # проверка возможности хода на две клетки вперёд
#             if isFirstMove(current_figure['y'], current_figure['x']) and isEmptyCeil(
#                     state[current_figure['y'] + 2][current_figure['x']]):
#                 moves.append((current_figure['y'] + 2, current_figure['x']))
#             # проверка возможности съесть фигуру справа от пешки
#             if current_figure['x'] != 7 and isEnemy(state[current_figure['y'] + 1][current_figure['x'] + 1]):
#                 kills.append((current_figure['y'] + 1, current_figure['x'] + 1))
#             # проверка возможности съесть фигуру слева от пешки
#             if current_figure['x'] != 0 and isEnemy(state[current_figure['y'] + 1][current_figure['x'] - 1]):
#                 kills.append((current_figure['y'] + 1, current_figure['x'] + 1))
#             # проверка возможности взятия на проходе
#             if pawnJump and pawnJump['y'] == current_figure['y']:
#                 # взятие на проходе справа
#                 if pawnJump['x'] == current_figure['x'] + 1:
#                     kills.append((current_figure['y'] + 1, current_figure['x'] + 1))
#                 # взятие на проходе слева
#                 elif pawnJump['x'] == current_figure['x'] - 1:
#                     kills.append((current_figure['y'] + 1, current_figure['x'] - 1))
#
#         if currentPlayer == 'White':
#             return getWhitePawnAction()
#         else:
#             return getBlackPawnAction()
#
#     def getRookAction():
#         # проверка возможности хода вправо
#         for j in range(current_figure['x'] + 1, 8):
#             # if isEmptyCeil(state[current_figure['y']][j]):
#             #     moves.append((current_figure['y'],j))
#             # else:
#             #    if isEnemy(state[current_figure['y']][j]):
#             #        kills.append((current_figure['y'], j))
#             #    break
#             if checkCeilForAction(current_figure['y'], j):
#                 break
#         # проверка возможности хода влево
#         for j in range(current_figure['x'] - 1, -1, -1):
#             if checkCeilForAction(current_figure['y'], j):
#                 break
#         # проверка возможности хода ыниз
#         for i in range(current_figure['y'] + 1, 8):
#             if checkCeilForAction(i, current_figure['x']):
#                 break
#         # проверка возможности хода вверх
#         for i in range(current_figure['y'] - 1, -1, -1):
#             if checkCeilForAction(i, current_figure['x']):
#                 break
#
#     # проверка возможныъ ходов для пешки
#     if 'P' in current:
#         getPawnAction()
#     # проверка возможныъ ходов для ладьи
#     elif 'R' in current:
#         # # проверка возможности хода вправо
#         # for j in range(current_figure['x']+1,8):
#         #     # if isEmptyCeil(state[current_figure['y']][j]):
#         #     #     moves.append((current_figure['y'],j))
#         #     # else:
#         #     #    if isEnemy(state[current_figure['y']][j]):
#         #     #        kills.append((current_figure['y'], j))
#         #     #    break
#         #     if checkCeilForAction(current_figure['y'],j):
#         #         break
#         # # проверка возможности хода влево
#         # for j in range(current_figure['x'] - 1, -1, -1):
#         #     if checkCeilForAction(current_figure['y'],j):
#         #         break
#         # # проверка возможности хода ыниз
#         # for i in range(current_figure['y'] + 1, 8):
#         #     if checkCeilForAction(i,current_figure['x']):
#         #         break
#         # # проверка возможности хода вверх
#         # for i in range(current_figure['y'] - 1, -1, -1):
#         #     if checkCeilForAction(i,current_figure['x']):
#         #         break
#         getRookAction()
#
#     return moves, kills


# отобразить возможные ходы и выбор хода (position)
def getFullState(drawMoves=True, position=False):
    # if not (drawMoves or moveMode):

    # показать текущие ходы, position = TRUE показать перемещение фигуры (при выборе хода)
    def getStateWithMoves():
        moves, kills = figureMovesWithCheck()
        fullState = copy.deepcopy(state)
        for y, x in moves:
            fullState[y][x] = 'm'
        for y, x in kills:
            fullState[y][x] = 'k' + fullState[y][x]
        # if check:
        #     y, x = myKingPosition()
        #     fullState[y][x] = 's'+ fullState[y][x]
        # текущая фигура
        fullState[current_position['y']][current_position['x']] = 'c' + fullState[current_position['y']][
            current_position['x']]

        # мои фигуры находящиеся под боем
        myFiguries = gelAllMyFiguries()
        for figure in myFiguries:
            if whoCanKilled(figure):
                y, x = figure
                fullState[y][x] = 'a' + fullState[y][x]

        # return [['bR', 'bN', 'bB', 'bQ', 'sbK', 'bB', 'bN', 'kbR'],
        #         ['bP', 'kbP', 'bP', 'bP', 'cbP', 'bP', 'bP', 'bP'],
        #         ['0'] * 8, ['m'] * 8, ['0'] * 8, ['0'] * 8,
        #         ['wP', 'wP', 'wP', 'wP', 'kwP', 'wP', 'wP', 'wP'],
        #         ['wR', 'wN', 'kwB', 'wQ', 'swK', 'cwB', 'wN', 'wR']]
        return fullState

    if drawMoves:
        return getStateWithMoves()
    return state


def getTableContent(drawMoves=True, position=False):
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
        elif cell == 'm':
            return currentBackColor + '    ' + Back.RESET
        # фигуры под боем
        # 1:3 cswK acwN
        elif cell.startswith('k'):
            return Back.RED + ' ' + Fore.BLACK + cell[-2:] + defaultForeColor + ' ' + Back.RESET
        # текущая фигура
        elif cell.startswith('c'):
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

    fullState = getFullState(drawMoves=True, position=False)
    tableContent = [[getCellStyle(fullState[i][j]) for j in range(8)] for i in range(8)]

    # cellTypes = {0: '    ',
    #              'm': currentBackColor+'    '+defaultBackColor,
    #              'bP': ' '+currentForeColor+'bP'+defaultForeColor+' ',
    #             'swK': Back.YELLOW+' '+currentForeColor+'wK'+defaultForeColor+' '+defaultBackColor,
    #              'kbP':  Back.RED+' '+Fore.black+'wK'+defaultForeColor+' '+defaultBackColor,
    #              '3': [[Fore.GREEN + ' ' * 4 + '*' * 2 + ' ' * 4 + Fore.CYAN],
    #                    [Fore.GREEN + ' ' * 3 + '*' * 4 + ' ' * 3 + Fore.CYAN],
    #                    [Fore.GREEN + ' ' + '*' * 8 + ' ' + Fore.CYAN], [Fore.GREEN + '*' * 10 + Fore.CYAN]],
    #              }

    # print(len(state))
    # print(len(state[0]))
    # print(tableContent)
    # for i in range(8):
    #     for j in range(8):
    #         tableContent[i][j] = copy.deepcopy(cellTypes[state[i][j]])

    # tableContent[marker['x']][marker['y']] = cellTypes[currentPlayer]

    # if drawMarker:
    #     def getBackColor():
    #         if currentPlayer == '1':
    #             return Back.RED
    #         elif currentPlayer == '2':
    #             return Back.BLUE
    #         else:
    #             return Back.GREEN
    #
    #     backColor = getBackColor()
    #
    #     for i in range(4):
    #         tableContent[marker['x']][marker['y']][i][0] = backColor + tableContent[marker['x']][marker['y']][i][
    #             0] + Back.RESET

    return tableContent


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


def showPlayerCount():
    print(f"\t{Fore.BLUE}White: {playersCount['White']}\n\t{Fore.GREEN}Black: {playersCount['Black']}{Fore.RESET}")


#
# def canMove():
#     moves, kills = figureMoves()
#     return moves or kills

def canMove(figurePosition=None):
    moves, kills = figureMoves(figurePosition)
    return moves or kills


# выбор своей фигуры для хода
# возможно следует добавить метод canMove() для проверки есть ли у фигуры ходы if myFigure(state[i][j]) and canMove(state[i][j])
def selectFigure():
    while True:
        command = input()
        if command == "d":
            # if marker['y'] != 4 and state[marker['x']][marker['y'] + 1] == 's':
            #     marker['y'] += 1
            # if marker['x'] != 4:
            for j in range(current_figure['x'] + 1, 8):
                if isMyFigure(state[current_figure['y']][j]):
                    current_figure['x'] = j
                    if canMove():
                        break
            else:
                for i in range(current_figure['y'] + 1, 8):
                    for j in range(8):
                        if isMyFigure(state[i][j]):
                            current_figure['y'] = i
                            current_figure['x'] = j
                            if canMove():
                                break
                    else:
                        continue
                    break
        elif command == "s":
            # if marker['x'] != 3 and state[marker['x'] + 1][marker['y']] == 's':
            #     marker['x'] += 1
            for i in range(current_figure['y'] + 1, 8):
                if isMyFigure(state[i][current_figure['x']]):
                    current_figure['y'] = i
                    if canMove():
                        break
            else:
                for j in range(current_figure['x'] + 1, 8):
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
            # if marker['y'] != 0 and state[marker['x']][marker['y'] - 1] == 's':
            #     marker['y'] -= 1
            for j in range(current_figure['x'] - 1, -1, -1):
                if isMyFigure(state[current_figure['y']][j]):
                    current_figure['x'] = j
                    if canMove():
                        break
            else:
                for i in range(current_figure['y'] - 1, -1, -1):
                    for j in range(8, -1, -1):
                        if isMyFigure(state[i][j]):
                            current_figure['y'] = i
                            current_figure['x'] = j
                            if canMove():
                                break
                    else:
                        continue
                    break
        elif command == "w":
            # if marker['x'] != 0 and state[marker['x'] - 1][marker['y']] == 's':
            #     marker['x'] -= 1
            for i in range(current_figure['y'] - 1, -1, -1):
                if isMyFigure(state[i][current_figure['x']]):
                    current_figure['y'] = i
                    if canMove():
                        break
            else:
                for j in range(current_figure['x'] - 1, -1, -1):
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
        draw(getTableContent())
        showPlayerCount()


def isMyFigureArea(ceil):
    return ceil == 'w' or 'k' in ceil


def moveFigure():
    def nextPlayer():
        global currentPlayer
        if currentPlayer == 'White':
            currentPlayer = 'Black'
        else:
            currentPlayer = 'White'

    def newMarker():
        for i in range(8):
            for j in range(8):
                if isMyFigure(state[i][j]):
                    current_figure['y'] = current_position['y'] = i
                    current_figure['x'] = current_position['x'] = j
                    return

    state = getFullState(True, True)

    while True:
        command = input()
        if command == "d":
            # if marker['y'] != 4 and state[marker['x']][marker['y'] + 1] == 's':
            #     marker['y'] += 1
            # if marker['x'] != 4:
            for j in range(current_position['x'] + 1, 8):
                if isMyFigureArea(state[current_position['y']][j]):
                    current_position['x'] = j
                    break
            else:
                for i in range(current_position['y'] + 1, 8):
                    for j in range(8):
                        if isMyFigureArea(state[i][j]):
                            current_position['y'] = i
                            current_position['x'] = j
                            break
                    else:
                        continue
                    break
        elif command == "s":
            # if marker['x'] != 3 and state[marker['x'] + 1][marker['y']] == 's':
            #     marker['x'] += 1
            for i in range(current_position['y'] + 1, 8):
                if isMyFigureArea(state[i][current_position['x']]):
                    current_position['y'] = i
                    break
            else:
                for j in range(current_position['x'] + 1, 8):
                    for i in range(8):
                        if isMyFigureArea(state[i][j]):
                            current_position['y'] = i
                            current_position['x'] = j
                            break
                    else:
                        continue
                    break
        elif command == "a":
            # if marker['y'] != 0 and state[marker['x']][marker['y'] - 1] == 's':
            #     marker['y'] -= 1
            for j in range(current_position['x'] - 1, -1, -1):
                if isMyFigureArea(state[current_position['y']][j]):
                    current_position['x'] = j
                    break
            else:
                for i in range(current_position['y'] - 1, -1, -1):
                    for j in range(8, -1, -1):
                        if isMyFigureArea(state[i][j]):
                            current_position['y'] = i
                            current_position['x'] = j
                            break
                    else:
                        continue
                    break
        elif command == "w":
            # if marker['x'] != 0 and state[marker['x'] - 1][marker['y']] == 's':
            #     marker['x'] -= 1
            for i in range(current_position['y'] - 1, -1, -1):
                if isMyFigureArea(state[i][current_position['x']]):
                    current_position['y'] = i
                    break
            else:
                for j in range(current_position['x'] - 1, -1, -1):
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
                return False

            move()

            break
        elif command == 'q':
            return False
        draw(getTableContent())
        showPlayerCount()
    nextPlayer()
    newMarker()
    return True


def transformPawn():
    if currentPlayer == 'White':
        return 'wQ'
    else:
        return 'bQ'


# def IsCheck():
#     return False


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


def isCheck():
    king = myKingPosition(getMyEnemy())
    return whoCanKilled(king)


# приватный метод
def move():
    global check
    global pawnJump

    def isPawnJump():
        # если пешка
        if 'P' in figure:
            if (current_position['y'] - current_figure['y'] == 2) or (current_figure['y'] - current_position['y'] == 2):
                return (current_position['y'], current_position['x'])
        return False

    # новая позиция фигуры
    current = state[current_position['y']][current_position['x']]
    # прошлая позиция
    figure = state[current_figure['y']][current_figure['x']]

    # отмечаем, что фигура сделала ход, это нужно для рокировки, или хода на две клетки вперёд у пешки, взятие на проходе
    moved_figure.add((current_figure['y'], current_figure['x']))

    # проверить сделала ли пешка ход на два шага вперёд, необходимо для проверки возможности взятия на проходе
    pawnJump = isPawnJump()

    # фигура бьёт другую
    if 'k' in current:
        # взятие на проходе
        if current == 'k':
            playersCount[currentPlayer] += state[current_position['y'] + 1][current_position['x']]
            state[current_position['y'] + 1][current_position['x']] = '0'
        # другие случаи
        else:
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

    # проверить привёл ли ход к шаху
    check = isCheck()


def showWinner():
    # мат
    if check:
        print(currentPlayer + " win!")
    # пат
    else:
        print('draw')


def game():
    try:
        # showRules()
        while True:
            init()

            while not gameover():
                draw(getTableContent())
                showPlayerCount()
                selectFigure()
                while not moveFigure():
                    pass

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
    # game()
    if {'y': 0, 'x': 0}:
        print(True)
