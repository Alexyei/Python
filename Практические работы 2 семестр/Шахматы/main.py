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


state = [[]]
current_figure = {'x': 0, 'y': 0}
currentPlayer = 'White'
playersCount = {'White': '', 'Black': '', }


def init():
    global state
    global marker
    global currentPlayer
    global playersCount

    state = [['bR','bN','bB','bQ','bK','bB','bN','bR'],
             ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
             [0] * 8, [0] * 8, [0] * 8, [0] * 8,
             ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
             ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']]

    # print(' '.join(state[0][:]))
    current_figure = {'x': 0, 'y': 0}
    currentPlayer = 'White'
    playersCount = {'White': '', 'Black': '', }


def gameover():
    def mat():
        return False
    def pat():
        return False
    return mat() or pat()


def getTableContent(drawMarker=True):
    temp_state = fullState(state, current_figure)
    tableContent = [[[] for j in range(8)] for i in range(8)]
    cellTypes = {'s': [['          '] for j in range(4)],
                 '1': [[Fore.RED + '+' * 6 + ' ' * 3 + '+' + Fore.CYAN],
                       [Fore.RED + '+' * 4 + ' ' * 4 + '+' * 2 + Fore.CYAN],
                       [Fore.RED + '+' * 2 + ' ' * 4 + '+' * 4 + Fore.CYAN],
                       [Fore.RED + '+' + ' ' * 3 + '+' * 6 + Fore.CYAN]],
                 '2': [[Fore.BLUE + '@' * 5 + ' ' * 5 + Fore.CYAN],
                       [Fore.BLUE + ' ' * 5 + '@' * 5 + Fore.CYAN],
                       [Fore.BLUE + '@' * 5 + ' ' * 5 + Fore.CYAN],
                       [Fore.BLUE + ' ' * 5 + '@' * 5 + Fore.CYAN]],
                 '3': [[Fore.GREEN + ' ' * 4 + '*' * 2 + ' ' * 4 + Fore.CYAN],
                       [Fore.GREEN + ' ' * 3 + '*' * 4 + ' ' * 3 + Fore.CYAN],
                       [Fore.GREEN + ' ' + '*' * 8 + ' ' + Fore.CYAN], [Fore.GREEN + '*' * 10 + Fore.CYAN]],
                 }

    # print(len(state))
    # print(len(state[0]))
    # print(tableContent)
    for i in range(8):
        for j in range(8):
            tableContent[i][j] = copy.deepcopy(cellTypes[state[i][j]])

    # tableContent[marker['x']][marker['y']] = cellTypes[currentPlayer]

    if drawMarker:
        def getBackColor():
            if currentPlayer == '1':
                return Back.RED
            elif currentPlayer == '2':
                return Back.BLUE
            else:
                return Back.GREEN

        backColor = getBackColor()

        for i in range(4):
            tableContent[marker['x']][marker['y']][i][0] = backColor + tableContent[marker['x']][marker['y']][i][
                0] + Back.RESET

    return tableContent


def draw(tableContent):
    # print(tableContent)

    def getRow(index):
        result = ""
        for i in range(4):
            result += "\n\t║"
            for j in range(5):
                # print(tableContent[index][j][i])
                result += tableContent[index][j][i][0] + "║"
        return result

    table = f'''{Fore.CYAN}
\t╔══════════╦══════════╦══════════╦══════════╦══════════╗{getRow(0)}
\t╠══════════╬══════════╬══════════╬══════════╬══════════╣{getRow(1)}
\t╠══════════╬══════════╬══════════╬══════════╬══════════╣{getRow(2)}
\t╠══════════╬══════════╬══════════╬══════════╬══════════╣{getRow(3)}
\t╚══════════╩══════════╩══════════╩══════════╩══════════╝{Fore.WHITE}'''

    os.system("cls")
    print(table)



def game():
    try:
        showRules()
        while True:
            init()
            while not gameover():
                draw(getTableContent())
                showPlayerCount()
                move()
            state[marker['x']][marker['y']] = currentPlayer
            changePlayerCount()
            draw(getTableContent(False))
            showPlayerCount()
            showWinner()
            input()
    except KeyboardInterrupt:
        exit(0)


if __name__ == '__main__':
    game()


