import pygame
from puzzle_game.constants import WIDTH, HEIGHT, SQUARE_SIZE, BORDEROUT, BORDERIN, FOOTER, BTNWIDTH, BTNHEIGHT
from puzzle_game.game import Game

pygame.init()

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Пятнашки')


def pos_on_btn(pos):
    x, y = pos
    if x >= BORDEROUT and x <= BTNWIDTH + BORDEROUT and y >= HEIGHT - BTNHEIGHT - BORDEROUT and y <= HEIGHT - BORDEROUT:
        return True
    return False


def pos_on_board(pos):
    on = True
    x, y = pos
    if x >= BORDEROUT + BORDERIN and x <= WIDTH - BORDEROUT and y >= BORDEROUT + BORDERIN and y <= HEIGHT - FOOTER:
        row, col = get_row_col_from_mouse((x - BORDEROUT - BORDERIN, y - BORDEROUT - BORDERIN))

        if (x - BORDEROUT - BORDERIN - col * (SQUARE_SIZE + BORDERIN) < SQUARE_SIZE) and (
                y - BORDEROUT - BORDERIN - row * (SQUARE_SIZE + BORDERIN) < SQUARE_SIZE):
            return (True, row, col)
    return (False, 0, 0)


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // (SQUARE_SIZE + BORDERIN)
    col = x // (SQUARE_SIZE + BORDERIN)
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        winner = game.winner()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                on, row, col = pos_on_board(pos)
                if on:
                    if not winner:
                        game.select(row, col)
                elif pos_on_btn(pos):
                    game.start()

        game.update()

    pygame.quit()


if __name__ == "__main__":
    main()
