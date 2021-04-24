import pygame
from .constants import ROWS, SQUARE_SIZE, COLS, BTNHEIGHT, BTNWIDTH, GREEN, ORANGE, TOMATO, BORDERIN, \
    BORDEROUT, WIDTH, HEIGHT, FOOTER, DARKGREEN
from .piece import Piece
import random


class Board:
    def __init__(self):
        self.board = []
        self.font = None
        self.font_size = 32
        self.btn_text = "Начать"
        self.time = 0
        self.move_count = 0
        self.create_board()

    def change_btn_text(self, text):
        self.btn_text = text

    def change_time(self, value):
        self.time = value

    def draw_win(self, win):
        pygame.draw.rect(win, TOMATO, (
            BORDEROUT, BORDEROUT, WIDTH - BORDEROUT * 2, HEIGHT - BORDEROUT - FOOTER))
        f = pygame.font.Font(self.font, self.font_size * 2)
        win_text = f.render("Вы выиграли!", 1, DARKGREEN)
        win.blit(win_text,
                 win_text.get_rect(center=(WIDTH // 2, BORDEROUT + (HEIGHT - BORDEROUT - FOOTER) // 2)))

    def draw_board(self, win):
        win.fill(ORANGE)
        pygame.draw.rect(win, TOMATO, (
            BORDEROUT, BORDEROUT, WIDTH - BORDEROUT * 2, HEIGHT - BORDEROUT - FOOTER))

        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(win, GREEN, (
                    BORDEROUT + col * SQUARE_SIZE + (col + 1) * BORDERIN,
                    BORDEROUT + row * SQUARE_SIZE + (row + 1) * BORDERIN, SQUARE_SIZE,
                    SQUARE_SIZE))

        f = pygame.font.Font(self.font, self.font_size)
        # draw btn play
        pygame.draw.rect(win, TOMATO, (BORDEROUT, HEIGHT - BORDEROUT - BTNHEIGHT, BTNWIDTH, BTNHEIGHT))

        btn_text = f.render(self.btn_text, 1, GREEN)
        win.blit(btn_text,
                 btn_text.get_rect(center=(BORDEROUT + BTNWIDTH // 2, HEIGHT - FOOTER + BORDEROUT + BTNHEIGHT // 2)))

        # draw move count
        move_text = f.render(f"Ходы: {self.move_count}", 1, GREEN)
        win.blit(move_text, move_text.get_rect(
            center=(WIDTH - BORDEROUT - move_text.get_rect().width // 2, HEIGHT - FOOTER + BORDEROUT + BTNHEIGHT // 2)))

        # draw time
        time_text = f.render(f"Время: {self.time}", 1, GREEN)
        win.blit(time_text, time_text.get_rect(center=(
        BORDEROUT + BTNWIDTH + (WIDTH - BORDEROUT - BTNWIDTH - move_text.get_rect().width) // 2,
        HEIGHT - FOOTER + BORDEROUT + BTNHEIGHT // 2)))

    def getTopBox(self, box):
        if (box.row == 0): return None
        return self.board[box.row - 1][box.col]

    def getBottomBox(self, box):
        if (box.row == COLS - 1): return None
        return self.board[box.row + 1][box.col]

    def getLeftBox(self, box):
        if (box.col == 0): return None
        return self.board[box.row][box.col - 1]

    def getRightBox(self, box):
        if (box.col == COLS - 1): return None
        return self.board[box.row][box.col + 1]

    def getNextBoxes(self, box):
        return list(filter(lambda x: x != None,
                           [self.getTopBox(box), self.getLeftBox(box), self.getBottomBox(box), self.getRightBox(box)]))

    def getRandomNextBox(self, box):
        next = self.getNextBoxes(box)
        return next[random.randint(0, len(next) - 1)]

    def swapBoxes(self, box1, box2):
        box1.value, box2.value = box2.value, box1.value

    def create_board(self):

        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append(Piece(row, col, (row * ROWS + col + 1) % 16))

        # Shuffle
        while True:
            blankBox = self.board[-1][-1]
            for i in range(1000):
                nextBox = self.getRandomNextBox(blankBox)
                self.swapBoxes(blankBox, nextBox)
                blankBox = nextBox
            if not self.winner():
                break

    def move(self, row, col):
        next = self.getNextBoxes(self.board[row][col])
        blankBox = [x for x in next if x.value == 0]
        if blankBox:
            self.swapBoxes(self.board[row][col], blankBox[0])
            if self.move_count >= 1000:
                self.move_count = 0
            self.move_count += 1

    def draw(self, win):
        for row in range(ROWS):
            for col in range(COLS):
                self.board[row][col].draw(win)

    def winner(self):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col].value != (row * ROWS + col + 1) % 16:
                    return False
        return True
