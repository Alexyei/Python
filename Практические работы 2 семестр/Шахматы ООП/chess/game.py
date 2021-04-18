import shutil
import os

from colorama import Fore
from colorama import Back

from board import Board
from constants import DEFAULTBackColor,DEFAULTForeColor

class Game:
    def __init__(self):
        # self._init()
        self.board = Board(8,8)
        self.currentPlayer = 'White'
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

    def gameover(self):
        pass

    def render(self, moves = True, position = True):

        tableContent = self._getTableContent(moves,position)

        def getRow(row):
            result = "\n\t║"
            for j in range(8):
                result += tableContent[row][j] + "║"
            return result

        table = f'''{DEFAULTForeColor}
        \t   A    B    C    D    E    F    G    H
        \t╔════╦════╦════╦════╦════╦════╦════╦════╗'''
        for i in range(8):
            table += getRow(i) + ' ' + str(8 - i)
            if i < 7:
                table += '\n\t╠════╬════╬════╬════╬════╬════╬════╬════╣'
            else:
                table += f'''\n\t╚════╩════╩════╩════╩════╩════╩════╩════╝{Fore.WHITE}'''

        os.system("cls")
        print(table)

    def showPlayerCount(self):
        print(f"\t{Fore.BLUE}White: {self.playersCount['White']}\n\t{Fore.GREEN}Black: {self.playersCount['Black']}{Fore.RESET}")

    def selectFigure(self):
        pass

    def moveFigure(self):
        pass

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
                if 'w' in cell:
                    return Fore.BLUE, Back.BLUE
                elif 'b' in cell:
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

        fullState = self.board.getFullState(moves, position)
        # print("FULLSTATE")
        # print(fullState)
        tableContent = [[getCellStyle(fullState[i][j]) for j in range(8)] for i in range(8)]

        return tableContent