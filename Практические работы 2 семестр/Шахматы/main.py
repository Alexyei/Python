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
state = [[]]
# выбранная фигура
current_figure = {'x': 4, 'y': 6}
# выбранный ход фигурой
current_position = {'x': 4, 'y': 6}
currentPlayer = 'White'
# currentForeColor = Fore.BLUE
# currentBackColor = Back.BLUE
playersCount = {'White': '', 'Black': '', }


def init():
    global state
    global marker
    global currentPlayer
    global current_figure
    global current_position
    # global currentForeColor
    # global currentBackColor
    global playersCount

    state = [['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
             ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
             ['0'] * 8, ['0'] * 8, ['0'] * 8, ['0'] * 8,
             ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
             ['wR', 'wN', 'wB', 'wQ', 'wKs', 'wB', 'wN', 'wR']]

    # print(' '.join(state[0][:]))
    current_figure = {'x': 0, 'y': 0}
    current_position = {'x': 0, 'y': 0}
    currentPlayer = 'White'
    # currentForeColor = Fore.GREEN
    # currentBackColor = Back.GREEN
    playersCount = {'White': '', 'Black': '', }


def gameover():
    def mat():
        return False

    def pat():
        return False

    return mat() or pat()


# отобразить возможные ходы и выбор хода (position)
def fullState(drawMoves=True, position=False):
    # if not (drawMoves or moveMode):

    # показать текущие ходы, position = TRUE показать перемещение фигуры (при выборе хода)
    def viewMoves(position=True):
        return [['bR', 'bN', 'bB', 'bQ', 'sbK', 'bB', 'bN', 'kbR'],
                ['bP', 'kbP', 'bP', 'bP', 'cbP', 'bP', 'bP', 'bP'],
                ['0'] * 8, ['m'] * 8, ['0'] * 8, ['0'] * 8,
                ['wP', 'wP', 'wP', 'wP', 'kwP', 'wP', 'wP', 'wP'],
                ['wR', 'wN', 'kwB', 'wQ', 'swK', 'cwB', 'wN', 'wR']]

    if drawMoves:
        return viewMoves(position)
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
        # возможный ход
        elif cell == 'm':
            return currentBackColor + '    ' + Back.RESET
        # шах
        elif cell.startswith('s'):
            return Back.MAGENTA + ' ' + Fore.BLACK + cell[1:] + defaultForeColor + ' ' + Back.RESET
        # фигуры под боем
        elif cell.startswith('k'):

            return Back.RED + ' ' + Fore.BLACK + cell[1:] + defaultForeColor + ' ' + Back.RESET
        # текущая фигура
        elif cell.startswith('c'):
            return currentBackColor + ' ' + Fore.BLACK + cell[1:] + defaultForeColor + ' ' + Back.RESET
        # обычные фигуры
        else:
            return ' ' + currentForeColor + cell + defaultForeColor + ' '

    temp_state = fullState(drawMoves=True, position=False)
    tableContent = [[getCellStyle(temp_state[i][j]) for j in range(8)] for i in range(8)]

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


def myFigure(ceil):
    return (currentPlayer == 'White' and 'w' in ceil) or (currentPlayer == 'Black' and 'b' in ceil)

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
                if myFigure(state[current_figure['y']][j]):
                    current_figure['x'] = j
                    break
            else:
                for i in range(current_figure['y'] + 1, 8):
                    for j in range(8):
                        if myFigure(state[i][j]):
                            current_figure['y'] = i
                            current_figure['x'] = j
                            break
                    else:
                        continue
                    break
        elif command == "s":
            # if marker['x'] != 3 and state[marker['x'] + 1][marker['y']] == 's':
            #     marker['x'] += 1
            for i in range(current_figure['y'] + 1, 8):
                if myFigure(state[i][marker['x']]):
                    current_figure['y'] = i
                    break
            else:
                for j in range(current_figure['x'] + 1, 8):
                    for i in range(8):
                        if myFigure(state[i][j]):
                            current_figure['y'] = i
                            current_figure['x'] = j
                            break
                    else:
                        continue
                    break
        elif command == "a":
            # if marker['y'] != 0 and state[marker['x']][marker['y'] - 1] == 's':
            #     marker['y'] -= 1
            for j in range(current_figure['x'] - 1, -1, -1):
                if myFigure(state[current_figure['y']][j]):
                    current_figure['x'] = j
                    break
            else:
                for i in range(current_figure['y'] - 1, -1, -1):
                    for j in range(8, -1, -1):
                        if myFigure(state[i][j]):
                            current_figure['y'] = i
                            current_figure['x'] = j
                            break
                    else:
                        continue
                    break
        elif command == "w":
            # if marker['x'] != 0 and state[marker['x'] - 1][marker['y']] == 's':
            #     marker['x'] -= 1
            for i in range(current_figure['y'] - 1, -1, -1):
                if myFigure(state[i][current_figure['x']]):
                    current_figure['y'] = i
                    break
            else:
                for j in range(current_figure['x'] - 1, -1, -1):
                    for i in range(7, -1, -1):
                        if myFigure(state[i][j]):
                            current_figure['y'] = i
                            current_figure['x'] = j
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

def move():
    def nextPlayer():
        global currentPlayer
        currentPlayer = str(int(currentPlayer) % 3 + 1)

    def newMarker():
        for i in range(4):
            for j in range(5):
                if state[i][j] == 's':
                    marker['x'] = i
                    marker['y'] = j
                    return

    state = fullState(True, True)

    while True:
        command = input()
        if command == "d":
            # if marker['y'] != 4 and state[marker['x']][marker['y'] + 1] == 's':
            #     marker['y'] += 1
            # if marker['x'] != 4:
            for j in range(marker['y'] + 1, 5):
                if state[marker['x']][j] == 'm':
                    marker['y'] = j
                    break
            else:
                for i in range(marker['x'] + 1, 4):
                    for j in range(5):
                        if state[i][j] == 's':
                            marker['x'] = i
                            marker['y'] = j
                            break
                    else:
                        continue
                    break
        elif command == "s":
            # if marker['x'] != 3 and state[marker['x'] + 1][marker['y']] == 's':
            #     marker['x'] += 1
            for i in range(marker['x'] + 1, 4):
                if state[i][marker['y']] == 's':
                    marker['x'] = i
                    break
            else:
                for j in range(marker['y'] + 1, 5):
                    for i in range(4):
                        if state[i][j] == 's':
                            marker['x'] = i
                            marker['y'] = j
                            break
                    else:
                        continue
                    break
        elif command == "a":
            # if marker['y'] != 0 and state[marker['x']][marker['y'] - 1] == 's':
            #     marker['y'] -= 1
            for j in range(marker['y'] - 1, -1, -1):
                if state[marker['x']][j] == 's':
                    marker['y'] = j
                    break
            else:
                for i in range(marker['x'] - 1, -1, -1):
                    for j in range(4, -1, -1):
                        if state[i][j] == 's':
                            marker['x'] = i
                            marker['y'] = j
                            break
                    else:
                        continue
                    break
        elif command == "w":
            # if marker['x'] != 0 and state[marker['x'] - 1][marker['y']] == 's':
            #     marker['x'] -= 1
            for i in range(marker['x'] - 1, -1, -1):
                if state[i][marker['y']] == 's':
                    marker['x'] = i
                    break
            else:
                for j in range(marker['y'] - 1, -1, -1):
                    for i in range(3, -1, -1):
                        if state[i][j] == 's':
                            marker['x'] = i
                            marker['y'] = j
                            break
                    else:
                        continue
                    break
        elif command == '':
            state[marker['x']][marker['y']] = currentPlayer
            changePlayerCount()
            break
        draw(getTableContent())
        showPlayerCount()
    nextPlayer()
    newMarker()

def game():
    try:
        # showRules()
        while True:
            init()

            # while not gameover():
            draw(getTableContent())
            showPlayerCount()
            # move()
            # state[marker['x']][marker['y']] = currentPlayer
            # changePlayerCount()
            # draw(getTableContent(False))
            # showPlayerCount()
            # showWinner()
            input()
    except KeyboardInterrupt:
        exit(0)


if __name__ == '__main__':
    game()
