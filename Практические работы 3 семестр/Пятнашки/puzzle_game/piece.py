from .constants import SQUARE_SIZE, GREEN, BORDERIN, BORDEROUT, DARKGREEN
import pygame


class Piece:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value

    def draw(self, win):
        if self.value != 0:
            pygame.draw.rect(win, GREEN, (
                BORDEROUT + self.col * SQUARE_SIZE + (self.col + 1) * BORDERIN,
                BORDEROUT + self.row * SQUARE_SIZE + (self.row + 1) * BORDERIN,
                SQUARE_SIZE,
                SQUARE_SIZE))
            f = pygame.font.Font(None, 48)
            box_text = f.render(str(self.value), 1, DARKGREEN)
            win.blit(box_text, box_text.get_rect(
                center=(BORDEROUT + self.col * SQUARE_SIZE + (self.col + 1) * BORDERIN + (SQUARE_SIZE // 2),
                        BORDEROUT + self.row * SQUARE_SIZE + (self.row + 1) * BORDERIN + (SQUARE_SIZE // 2))))
