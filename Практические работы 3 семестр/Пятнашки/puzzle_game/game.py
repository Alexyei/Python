import pygame
from .board import Board
import time


class Game:
    def __init__(self, win):
        self._init()
        self.win = win
        self.run = False

    def _init(self):
        self.board = Board()
        self.win_flag = False

    def select(self, row, col):
        self.board.move(row, col)

    def start(self):
        if self.run:
            self._init()
        self.run = True
        self.start_time = time.time()
        self.board.change_btn_text("Заново")

    def update(self):
        self.board.draw_board(self.win)
        if self.win_flag:
            self.board.draw_win(self.win)
        elif self.run:
            self.board.draw(self.win)
            time_diff = round(time.time() - self.start_time)
            if time_diff >= 10000:
                self.start_time = time_diff = 0
            self.board.change_time(time_diff)

        pygame.display.update()

    def winner(self):
        self.win_flag = self.board.winner()
        if (self.win_flag):
            self.board.change_btn_text("Начать")
        return self.win_flag

    def reset(self):
        self._init()
