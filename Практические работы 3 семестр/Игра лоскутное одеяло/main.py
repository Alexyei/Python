import shutil

import keyboard


import os
from IPython.display import clear_output
from colorama import Fore
from colorama import Back

# table = f'''
# ╔══════════╦══════════╦══════════╦══════════╦══════════╗
# ║++++++   +║@@@@@@    ║    **    ║          ║          ║
# ║++++    ++║     @@@@@║   ****   ║          ║          ║
# ║++    ++++║@@@@@@    ║ ******** ║          ║          ║
# ║+   ++++++║     @@@@@║**********║          ║          ║
# ╠══════════╬══════════╬══════════╬══════════╬══════════╣
# ║          ║          ║          ║          ║          ║
# ║          ║          ║          ║          ║          ║
# ║          ║          ║          ║          ║          ║
# ║          ║          ║          ║          ║          ║
# ╠══════════╬══════════╬══════════╬══════════╬══════════╣
# ║          ║          ║          ║          ║          ║
# ║          ║          ║          ║          ║          ║
# ║          ║          ║          ║          ║          ║
# ║          ║          ║          ║          ║          ║
# ╠══════════╬══════════╬══════════╬══════════╬══════════╣
# ║          ║          ║          ║          ║          ║
# ║          ║          ║          ║          ║          ║
# ║          ║          ║          ║          ║          ║
# ║          ║          ║          ║          ║          ║
# ╚══════════╩══════════╩══════════╩══════════╩══════════╝
# '''

state = [[]]
marker = {'x': 0, 'y': 0}
currentPlayer = '1'
playersCount = {'1': 0, '2': 0, '3': 0}


def init():
    global state
    global marker
    global currentPlayer
    global playersCount
    state = [['s' for j in range(5)] for i in range(4)]
    # state[2][2] = '1'
    # state[1][1] = '2'
    # state[3][1] = '3'
    # state[1][2] = '2'
    # state[2][3] = '3'
    # state[0][1] = 'm'
    # print(' '.join(state[0][:]))
    marker = {'x': 0, 'y': 0}
    currentPlayer = '1'
    playersCount = {'1': 0, '2': 0, '3': 0}


def getTableContent(drawMarker=True):
    # global state
    tableContent = [[[] for j in range(5)] for i in range(4)]
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
    for i in range(len(state)):
        for j in range(len(state[0])):
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


def changePlayerCount():
    playersCount[currentPlayer] += sum([row[max(0, marker['y'] - 1):marker['y'] + 2].count(currentPlayer) for row in
                                        state[max(0, marker['x'] - 1):marker['x'] + 2]]) - 1



def showPlayerCount():
    print(f"\t{Fore.RED}Player 1: {playersCount['1']}, {Fore.BLUE}Player 2: {playersCount['2']}, {Fore.GREEN}Player 3: {playersCount['3']}{Fore.RESET}")


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

    while True:
        command = input()
        if command == "d":
            # if marker['y'] != 4 and state[marker['x']][marker['y'] + 1] == 's':
            #     marker['y'] += 1
            # if marker['x'] != 4:
            for j in range(marker['y'] + 1, 5):
                if state[marker['x']][j] == 's':
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


def showPlayer(index):
    if index == '1':
        #         playerStr = Fore.RED + f'''
        # {Back.RED + ' ' * 10 + Back.RESET + ' '}++++++++  ++          +++    ++    ++ ++++++++ ++++++++        ++
        # {Back.RED + ' ' * 10 + Back.RESET + ' '}++     ++ ++         ++ ++    ++  ++  ++       ++     ++     ++++
        # {Back.RED + ' ' * 10 + Back.RESET + ' '}++     ++ ++        ++   ++    ++++   ++       ++     ++       ++
        # {Back.RED + ' ' * 10 + Back.RESET + ' '}++++++++  ++       ++     ++    ++    ++++++   ++++++++        ++
        # {Back.RED + ' ' * 10 + Back.RESET + ' '}++        ++       +++++++++    ++    ++       ++   ++         ++
        # {Back.RED + ' ' * 10 + Back.RESET + ' '}++        ++       ++     ++    ++    ++       ++    ++        ++
        # {Back.RED + ' ' * 10 + Back.RESET + ' '}++        ++++++++ ++     ++    ++    ++++++++ ++     ++     ++++++''' \
        #                     + Fore.RESET
        playerStr = Fore.RED + f'''
{Back.RED + ' ' * 10 + Back.RESET + ' '}++++++++  ++          +++    ++    ++ ++++++++ ++++++++        ++      ++      ++ ++++ ++    ++
{Back.RED + ' ' * 10 + Back.RESET + ' '}++     ++ ++         ++ ++    ++  ++  ++       ++     ++     ++++      ++  ++  ++  ++  +++   ++
{Back.RED + ' ' * 10 + Back.RESET + ' '}++     ++ ++        ++   ++    ++++   ++       ++     ++       ++      ++  ++  ++  ++  ++++  ++
{Back.RED + ' ' * 10 + Back.RESET + ' '}++++++++  ++       ++     ++    ++    ++++++   ++++++++        ++      ++  ++  ++  ++  ++ ++ ++
{Back.RED + ' ' * 10 + Back.RESET + ' '}++        ++       +++++++++    ++    ++       ++   ++         ++      ++  ++  ++  ++  ++  ++++
{Back.RED + ' ' * 10 + Back.RESET + ' '}++        ++       ++     ++    ++    ++       ++    ++        ++      ++  ++  ++  ++  ++   +++
{Back.RED + ' ' * 10 + Back.RESET + ' '}++        ++++++++ ++     ++    ++    ++++++++ ++     ++     ++++++     +++  +++  ++++ ++    ++''' \
                    + Fore.RESET
        print(playerStr)
    elif index == '2':
        #         playerStr = Fore.BLUE + f'''
        # {Back.BLUE + ' ' * 10 + Back.RESET + ' '}@@@@@@@@  @@          @@@    @@    @@ @@@@@@@@ @@@@@@@@      @@@@@@@
        # {Back.BLUE + ' ' * 10 + Back.RESET + ' '}@@     @@ @@         @@ @@    @@  @@  @@       @@     @@    @@     @@
        # {Back.BLUE + ' ' * 10 + Back.RESET + ' '}@@     @@ @@        @@   @@    @@@@   @@       @@     @@           @@
        # {Back.BLUE + ' ' * 10 + Back.RESET + ' '}@@@@@@@@  @@       @@     @@    @@    @@@@@@   @@@@@@@@      @@@@@@@
        # {Back.BLUE + ' ' * 10 + Back.RESET + ' '}@@        @@       @@@@@@@@@    @@    @@       @@   @@      @@
        # {Back.BLUE + ' ' * 10 + Back.RESET + ' '}@@        @@       @@     @@    @@    @@       @@    @@     @@
        # {Back.BLUE + ' ' * 10 + Back.RESET + ' '}@@        @@@@@@@@ @@     @@    @@    @@@@@@@@ @@     @@    @@@@@@@@@''' \
        #                     + Fore.RESET
        playerStr = Fore.BLUE + f'''
{Back.BLUE + ' ' * 10 + Back.RESET + ' '}@@@@@@@@  @@          @@@    @@    @@ @@@@@@@@ @@@@@@@@      @@@@@@@     @@      @@ @@@@ @@    @@
{Back.BLUE + ' ' * 10 + Back.RESET + ' '}@@     @@ @@         @@ @@    @@  @@  @@       @@     @@    @@     @@    @@  @@  @@  @@  @@@   @@
{Back.BLUE + ' ' * 10 + Back.RESET + ' '}@@     @@ @@        @@   @@    @@@@   @@       @@     @@           @@    @@  @@  @@  @@  @@@@  @@
{Back.BLUE + ' ' * 10 + Back.RESET + ' '}@@@@@@@@  @@       @@     @@    @@    @@@@@@   @@@@@@@@      @@@@@@@     @@  @@  @@  @@  @@ @@ @@
{Back.BLUE + ' ' * 10 + Back.RESET + ' '}@@        @@       @@@@@@@@@    @@    @@       @@   @@      @@           @@  @@  @@  @@  @@  @@@@
{Back.BLUE + ' ' * 10 + Back.RESET + ' '}@@        @@       @@     @@    @@    @@       @@    @@     @@           @@  @@  @@  @@  @@   @@@
{Back.BLUE + ' ' * 10 + Back.RESET + ' '}@@        @@@@@@@@ @@     @@    @@    @@@@@@@@ @@     @@    @@@@@@@@@     @@@  @@@  @@@@ @@    @@''' \
                    + Fore.RESET
        print(playerStr)
    else:
        #         playerStr = Fore.GREEN + f'''
        # {Back.GREEN + ' ' * 10 + Back.RESET + ' '}********  **          ***    **    ** ******** ********      *******
        # {Back.GREEN + ' ' * 10 + Back.RESET + ' '}**     ** **         ** **    **  **  **       **     **    **     **
        # {Back.GREEN + ' ' * 10 + Back.RESET + ' '}**     ** **        **   **    ****   **       **     **           **
        # {Back.GREEN + ' ' * 10 + Back.RESET + ' '}********  **       **     **    **    ******   ********      *******
        # {Back.GREEN + ' ' * 10 + Back.RESET + ' '}**        **       *********    **    **       **   **             **
        # {Back.GREEN + ' ' * 10 + Back.RESET + ' '}**        **       **     **    **    **       **    **     **     **
        # {Back.GREEN + ' ' * 10 + Back.RESET + ' '}**        ******** **     **    **    ******** **     **     *******''' \
        #                     + Fore.RESET
        playerStr = Fore.GREEN + f'''
{Back.GREEN + ' ' * 10 + Back.RESET + ' '}********  **          ***    **    ** ******** ********      *******     **      ** **** **    **
{Back.GREEN + ' ' * 10 + Back.RESET + ' '}**     ** **         ** **    **  **  **       **     **    **     **    **  **  **  **  ***   **
{Back.GREEN + ' ' * 10 + Back.RESET + ' '}**     ** **        **   **    ****   **       **     **           **    **  **  **  **  ****  **
{Back.GREEN + ' ' * 10 + Back.RESET + ' '}********  **       **     **    **    ******   ********      *******     **  **  **  **  ** ** **
{Back.GREEN + ' ' * 10 + Back.RESET + ' '}**        **       *********    **    **       **   **             **    **  **  **  **  **  ****
{Back.GREEN + ' ' * 10 + Back.RESET + ' '}**        **       **     **    **    **       **    **     **     **    **  **  **  **  **   ***
{Back.GREEN + ' ' * 10 + Back.RESET + ' '}**        ******** **     **    **    ******** **     **     *******      ***  ***  **** **    **''' \
                    + Fore.RESET
        print(playerStr)


def showWinner():
    count = len(set(playersCount.values()))
    if count == 1:
        tempStr = Fore.CYAN + f'''
{Back.CYAN + ' ' * 10 + Back.RESET + ' '}##     ## ##     ## ##     ## ##         ######## 
{Back.CYAN + ' ' * 10 + Back.RESET + ' '}##     ## ##    ### ##     ## ##        ##     ##
{Back.CYAN + ' ' * 10 + Back.RESET + ' '}##     ## ##   #### ##     ## ##        ##     ##
{Back.CYAN + ' ' * 10 + Back.RESET + ' '}######### ## ### ## ######### ########   ########
{Back.CYAN + ' ' * 10 + Back.RESET + ' '}##     ## ####   ##        ## ##     ##   ##   ##
{Back.CYAN + ' ' * 10 + Back.RESET + ' '}##     ## ###    ##        ## ##     ##  ##    ##
{Back.CYAN + ' ' * 10 + Back.RESET + ' '}##     ## ##     ##        ## ########  ##     ##''' + Fore.RESET
        print(tempStr)
    elif count == 2:
        winners = [key for key, value in playersCount.items() if value == min(playersCount.values())]
        # print(f"Победили: player {winners[0]} и player {winners[1]}")
        # print("Победили")
        for winner in winners:
            showPlayer(winner)
    else:
        # print(f"Плбедил: {[key for key, value in playersCount.items() if value == min(playersCount.values())][0]}")
        # print("Победил")
        showPlayer([key for key, value in playersCount.items() if value == min(playersCount.values())][0])


def showRules():
    os.system("cls")
    print("Игра лоскутное одеяло".center(shutil.get_terminal_size().columns))
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
{Back.RED + ' ' * 10 + Back.RESET + ' '}{Fore.RED + '+' * 6 + ' ' * 3 + '+' + Fore.CYAN}
{Back.RED + ' ' * 10 + Back.RESET + ' '}{Fore.RED + '+' * 4 + ' ' * 4 + '+' * 2 + Fore.CYAN}
{Back.RED + ' ' * 10 + Back.RESET + ' '}{Fore.RED + '+' * 2 + ' ' * 4 + '+' * 4 + Fore.CYAN}
{Back.RED + ' ' * 10 + Back.RESET + ' '}{Fore.RED + '+' + ' ' * 3 + '+' * 6 + Fore.CYAN}'''
    print(tempStr)
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
    print()
    print("Что-бы запустить игру -нажмите Enter".center(shutil.get_terminal_size().columns))
    input()


def game():
    try:
        showRules()
        while True:
            init()
            for i in range(19):
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


def main():
    # print(shutil.get_terminal_size().columns)
    # print(f'╔══════════╦══════════╦══════════╦══════════╦══════════╗'.center(shutil.get_terminal_size().columns))
    # print(table)
    # keyboard.wait('enter')
    # os.system("cls")
    # clear_output()
    # print("100")
    # init()
    # print(state)
    # print(marker)
    # print(currentPlayer)
    # draw(getTableContent())
    # print(len(input()))
    # while True:
    #     for i in range(5):
    #         print(i)
    #         # if i == 2:
    #         #     break
    #     else:
    #         for j in range(10, 100):
    #             print(j)
    #     break
    game()
    # arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 19, 19], [17, 18, 19, 19]]
    # x = 4
    # y = 3
    # print(arr[x - 1:x + 2])
    # print([row[max(0, y - 1):y + 2] for row in arr[max(0, x - 1):x + 2]])
    # print(sum([row[max(0, y - 1):y + 2].count(19) for row in arr[max(0, x - 1):x + 2]]) - 1)
    # print(arr[x-1:x+2][y-1:y+2])


#     str1 = '''
# ########  ##          ###    ##    ## ######## ########      #######     ##      ## #### ##    ##
# ##     ## ##         ## ##    ##  ##  ##       ##     ##    ##     ##    ##  ##  ##  ##  ###   ##
# ##     ## ##        ##   ##    ####   ##       ##     ##           ##    ##  ##  ##  ##  ####  ##
# ########  ##       ##     ##    ##    ######   ########      #######     ##  ##  ##  ##  ## ## ##
# ##        ##       #########    ##    ##       ##   ##             ##    ##  ##  ##  ##  ##  ####
# ##        ##       ##     ##    ##    ##       ##    ##     ##     ##    ##  ##  ##  ##  ##   ###
# ##        ######## ##     ##    ##    ######## ##     ##     #######      ###  ###  #### ##    ##
# '''
#     print(str1.replace('#', '*'))
#     showPlayer('1')
#     showPlayer('2')
#     showPlayer('3')


if __name__ == '__main__':
    main()
