import shutil
import os

from colorama import Fore
from colorama import Back

from chess.board import Board
from chess.constants import DEFAULTBackColor,DEFAULTForeColor

class Game:
    def __init__(self):
        # self._init()
        self.board = Board(8,8)
        self.currentPlayer = 'Black'
        self.playersCount = {'White': '', 'Black': '', }



    # def _init(self):
    #     pass

    @staticmethod
    def showRules():
        os.system("cls")
        print("Шахматы".center(shutil.get_terminal_size().columns))
        print()
        print("Правила игры".center(shutil.get_terminal_size().columns))
        print(
            'Соперники ходят по очереди. Игрок может выбрать фигуру для которой есть хотя бы один ход.\n' +
            'Победителем является тот кто поставит мат противнику.\n' +
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

    def getMyEnemy(self):
        if self.currentPlayer == 'White':
            return 'Black'
        else:
            return 'White'

    def gameover(self):
        # print(self.board.current_figure.getPosition())
        myFiguries = self.board.gelAllMyFiguries(self.currentPlayer)
        # print(self.board.current_figure.getPosition())
        for figure in myFiguries:
            # moves, kills = figureMovesWithCheck(figure)
            moves, kills = self.board.controller.figureMoves(figure.getPosition())
            if moves or kills:
                # print(self.board.current_figure.getPosition())
                return False
        # print("GAMEOVER!")

        return True

    def render(self, moves = True, position = True):

        tableContent = self._getTableContent(moves,position)

        def getRow(row):
            result = "\n\t║"
            for j in range(8):
                result += tableContent[row][j] + "║"
            return result


        table = f'''{DEFAULTForeColor}
        \n\t   A    B    C    D    E    F    G    H\n\t╔════╦════╦════╦════╦════╦════╦════╦════╗'''
        for i in range(8):
            table += getRow(i) + ' ' + str(8 - i)
            if i < 7:
                table += '\n\t╠════╬════╬════╬════╬════╬════╬════╬════╣'
            else:
                table += f'''\n\t╚════╩════╩════╩════╩════╩════╩════╩════╝{Fore.WHITE}'''

        os.system("cls")
        # print()
        print(table)

    def showPlayerCount(self):
        print(f"\t{Fore.BLUE}White: {self.playersCount['White']}\n\t{Fore.GREEN}Black: {self.playersCount['Black']}{Fore.RESET}")

    def selectFigure(self):
        while True:
            command = input()
            if command == "d":
                for j in range(self.board.current_figure.x + 1, self.board.width):
                    if self.board.isMyFigure(self.board.state[self.board.current_figure.y][j], self.currentPlayer):
                        self.board.current_figure = self.board.state[self.board.current_figure.y][j]
                        # current_figure['x'] = j
                        if self.board.controller.canMove(self.board.current_figure.getPosition()):
                            break
                else:
                    # for i in range(8):
                    for i in range(self.board.current_figure.y + 1, self.board.height):
                        for j in range(self.board.width):

                            if self.board.isMyFigure(self.board.state[i][j], self.currentPlayer):
                                # current_figure['y'] = i
                                # current_figure['x'] = j
                                self.board.current_figure = self.board.state[i][j]
                                # if canMove():
                                #     break
                                if self.board.controller.canMove(self.board.current_figure.getPosition()):
                                    break
                        else:
                            continue
                        break
                    else:
                        for i in range(0, self.board.current_figure.y + 1):
                            for j in range(self.board.width):

                                if self.board.isMyFigure(self.board.state[i][j], self.currentPlayer):
                                    # current_figure['y'] = i
                                    # current_figure['x'] = j
                                    self.board.current_figure = self.board.state[i][j]
                                    # if canMove():
                                    #     break
                                    if self.board.controller.canMove(self.board.current_figure.getPosition()):
                                        break
                            else:
                                continue
                            break
            elif command == "s":
                for i in range(self.board.current_figure.y + 1, self.board.height):
                    if self.board.isMyFigure(self.board.state[i][self.board.current_figure.x], self.currentPlayer):
                        # current_figure['y'] = i
                        self.board.current_figure = self.board.state[i][self.board.current_figure.x]
                        # if canMove():
                        if self.board.controller.canMove(self.board.current_figure.getPosition()):
                            break
                else:
                    for j in range(self.board.current_figure.x + 1, self.board.width):
                        # for j in range(8):
                        for i in range(self.board.height):
                            if self.board.isMyFigure(self.board.state[i][j], self.currentPlayer):
                                self.board.current_figure = self.board.state[i][j]
                                if self.board.controller.canMove(self.board.current_figure.getPosition()):
                                    break
                        else:
                            continue
                        break
                    else:

                        for j in range(0, self.board.current_figure.x + 1):
                            # for j in range(8):
                            for i in range(self.board.height):
                                if self.board.isMyFigure(self.board.state[i][j], self.currentPlayer):
                                    self.board.current_figure = self.board.state[i][j]
                                    if self.board.controller.canMove(self.board.current_figure.getPosition()):
                                        break
                            else:
                                continue
                            break
            elif command == "a":
                for j in range(self.board.current_figure.x - 1, -1, -1):
                    if self.board.isMyFigure(self.board.state[self.board.current_figure.y][j], self.currentPlayer):
                        # current_figure['x'] = j
                        self.board.current_figure = self.board.state[self.board.current_figure.y][j]
                        if self.board.controller.canMove(self.board.current_figure.getPosition()):
                            break
                else:
                    # for i in range(7, -1, -1):
                    for i in range(self.board.current_figure.y - 1, -1, -1):
                        for j in range(self.board.width-1, -1, -1):
                            if self.board.isMyFigure(self.board.state[i][j], self.currentPlayer):
                                self.board.current_figure = self.board.state[i][j]
                                if self.board.controller.canMove(self.board.current_figure.getPosition()):
                                    break
                        else:
                            continue
                        break
                    else:
                        for i in range(self.board.height-1, self.board.current_figure.y - 1, -1):
                            # print("AAAA")
                            for j in range(self.board.width-1, -1, -1):
                                if self.board.isMyFigure(self.board.state[i][j], self.currentPlayer):
                                    self.board.current_figure = self.board.state[i][j]
                                    if self.board.controller.canMove(self.board.current_figure.getPosition()):
                                        break
                            else:
                                continue
                            break
            elif command == "w":
                # print("START"+ str(self.board.current_figure.getPosition()))
                for i in range(self.board.current_figure.y - 1, -1, -1):
                    if self.board.isMyFigure(self.board.state[i][self.board.current_figure.x], self.currentPlayer):
                        # current_figure['y'] = i
                        self.board.current_figure = self.board.state[i][self.board.current_figure.x]
                        # print("1" + str(self.board.current_figure.getPosition()))
                        if self.board.controller.canMove(self.board.current_figure.getPosition()):
                            break
                else:
                    for j in range(self.board.current_figure.x - 1, -1, -1):
                        # for j in range(7, -1, -1):
                        for i in range(self.board.height-1, -1, -1):
                            if self.board.isMyFigure(self.board.state[i][j], self.currentPlayer):
                                self.board.current_figure = self.board.state[i][j]
                                # print("2"+str(self.board.current_figure.getPosition()))
                                if self.board.controller.canMove(self.board.current_figure.getPosition()):
                                    break
                        else:
                            continue
                        break
                    else:
                        # print("3")
                        for j in range(self.board.width-1, self.board.current_figure.x - 1, -1):
                            # for j in range(7, -1, -1):
                            for i in range(self.board.height-1, -1, -1):
                                if self.board.isMyFigure(self.board.state[i][j], self.currentPlayer):
                                    self.board.current_figure = self.board.state[i][j]
                                    # print("3" + str(self.board.current_figure.getPosition()))
                                    if self.board.controller.canMove(self.board.current_figure.getPosition()):
                                        break
                            else:
                                continue
                            break
            elif command == '':
                # state[marker['x']][marker['y']] = currentPlayer
                # changePlayerCount()
                break
            # draw(getTableContent(position=False))
            self.render(position=False)
            self.showPlayerCount()

    def moveFigure(self):
        def isMyFigureArea(ceil):
            return ('m' in ceil) or ('k' in ceil)

        def nextPlayer():
            if self.currentPlayer == 'White':
                self.currentPlayer = 'Black'
            else:
                self.currentPlayer = 'White'

        def newMarker():
            for i in range(self.board.height):
                for j in range(self.board.width):
                    if self.board.isMyFigure(self.board.state[i][j], self.currentPlayer):
                        self.board.current_figure = self.board.state[i][j]
                        self.board.current_position['y'] = i
                        self.board.current_position['x'] = j
                        if self.board.controller.canMove(self.board.current_figure.getPosition()):
                            # print(self.board.current_figure.getPosition())
                            break
                else:
                    continue
                break

        def sync():
            # синхронизация (так как в select figure меняется только current_figure)
            self.board.current_position['y'] = self.board.current_figure.y
            self.board.current_position['x'] = self.board.current_figure.x

        sync()

        while True:
            state = self.board.getFullState(self.currentPlayer, True, True)
            # print(state)
            command = input()
            if command == "d":
                for j in range(self.board.current_position['x'] + 1, self.board.width):
                    if isMyFigureArea(state[self.board.current_position['y']][j]):
                        self.board.current_position['x'] = j
                        break
                else:
                    for i in range(self.board.current_position['y'] + 1, self.board.height):
                        # for i in range(8):
                        for j in range(self.board.width):
                            if isMyFigureArea(state[i][j]):
                                self.board.current_position['y'] = i
                                self.board.current_position['x'] = j
                                break
                        else:
                            continue
                        break
                    else:
                        for i in range(0, self.board.current_position['y'] + 1):
                            for j in range(self.board.width):
                                if isMyFigureArea(state[i][j]):
                                    self.board.current_position['y'] = i
                                    self.board.current_position['x'] = j
                                    break
                            else:
                                continue
                            break
            elif command == "s":
                # print(state)
                for i in range(self.board.current_position['y'] + 1, self.board.height):
                    # print("fl do it" + str(i))
                    if isMyFigureArea(state[i][self.board.current_position['x']]):
                        # print("do it"+str(i))
                        self.board.current_position['y'] = i
                        break
                else:
                    for j in range(self.board.current_position['x'] + 1, self.board.width):
                        # for j in range(8):
                        for i in range(self.board.height):
                            if isMyFigureArea(state[i][j]):
                                self.board.current_position['y'] = i
                                self.board.current_position['x'] = j
                                break
                        else:
                            continue
                        break
                    else:
                        for j in range(0, self.board.current_position['x'] + 1):
                            for i in range(self.board.height):
                                if isMyFigureArea(state[i][j]):
                                    self.board.current_position['y'] = i
                                    self.board.current_position['x'] = j
                                    break
                            else:
                                continue
                            break

            elif command == "a":
                for j in range(self.board.current_position['x'] - 1, -1, -1):
                    if isMyFigureArea(state[self.board.current_position['y']][j]):
                        self.board.current_position['x'] = j
                        break
                else:
                    for i in range(self.board.current_position['y'] - 1, -1, -1):
                        # for i in range(7, -1, -1):
                        for j in range(self.board.width-1, -1, -1):
                            if isMyFigureArea(state[i][j]):
                                self.board.current_position['y'] = i
                                self.board.current_position['x'] = j
                                break
                        else:
                            continue
                        break
                    else:
                        for i in range(self.board.height-1, self.board.current_position['y'] - 1, -1):
                            for j in range(self.board.width-1, -1, -1):
                                if isMyFigureArea(state[i][j]):
                                    self.board.current_position['y'] = i
                                    self.board.current_position['x'] = j
                                    break
                            else:
                                continue
                            break
            elif command == "w":
                for i in range(self.board.current_position['y'] - 1, -1, -1):
                    if isMyFigureArea(state[i][self.board.current_position['x']]):
                        self.board.current_position['y'] = i
                        break
                else:
                    for j in range(self.board.current_position['x'] - 1, -1, -1):
                        # for j in range(7, -1, -1):
                        for i in range(self.board.height-1, -1, -1):
                            if isMyFigureArea(state[i][j]):
                                self.board.current_position['y'] = i
                                self.board.current_position['x'] = j
                                break
                        else:
                            continue
                        break
                    else:
                        for j in range(self.board.width-1, self.board.current_position['x'] - 1, -1):
                            for i in range(self.board.height-1, -1, -1):
                                if isMyFigureArea(state[i][j]):
                                    self.board.current_position['y'] = i
                                    self.board.current_position['x'] = j
                                    break
                            else:
                                continue
                            break
            elif command == '':
                if self.board.current_figure.getPosition() == (self.board.current_position['y'], self.board.current_position['x']):
                    # print("ret f")
                    return True

                # move()
                killed, moveNext = self.board.controller.move(self.board.current_figure,(self.board.current_position['y'], self.board.current_position['x']))
                # print(killed)
                if killed:
                    for kill in killed:
                        self.playersCount[self.currentPlayer] += str(kill)[-1]

                # self.board.isCheck(self.getMyEnemy())
                # фигура не закончила серию взятий
                if moveNext:
                    sync()
                else:
                    break
            elif command == 'q':
                return True
            # draw(getTableContent())
            self.render()
            self.showPlayerCount()
        nextPlayer()
        newMarker()
        # print(self.board.current_figure.getPosition())
        # print("return")
        return True

    def showWinner(self):
        # мат
        if self.board.check:
            if self.currentPlayer == 'White':
                print("Black win!")
            else:
                print("White win!")
        # пат
        else:
            print('draw')

    def _getTableContent(self, moves=True, position=True):
        def getCellStyle(cell):
            def getCurrentColor():
                if 'w' in str(cell):
                    return Fore.BLUE, Back.BLUE
                elif 'b' in str(cell):
                    return Fore.GREEN, Back.GREEN
                elif self.currentPlayer == 'White':
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
                return Back.RED + ' ' + Fore.BLACK + cell[-2:] + DEFAULTForeColor + ' ' + Back.RESET
            # текущая фигура
            elif cell.startswith('c'):
                # print(cell[-2:])
                return currentBackColor + ' ' + Fore.BLACK + cell[-2:] + DEFAULTForeColor + ' ' + Back.RESET
            # шах
            elif cell.startswith('a') and 'K' in cell:
                return Back.MAGENTA + ' ' + Fore.BLACK + cell[-2:] + DEFAULTForeColor + ' ' + Back.RESET
            # aim фигуру которую может съесть противник на следующем ходу
            elif cell.startswith('a'):
                return ' ' + Fore.RED + cell[-2:] + DEFAULTForeColor + ' '
            # обычные фигуры
            else:
                return ' ' + currentForeColor + cell + DEFAULTForeColor + ' '

        fullState = self.board.getFullState(self.currentPlayer, moves, position )
        # print("FULLSTATE")
        # print(fullState)
        tableContent = [[getCellStyle(fullState[i][j]) for j in range(8)] for i in range(8)]

        return tableContent