from chess.game import Game

def main():
    try:
        Game.showRules()
        while True:
            game = Game()
            while not game.gameover():
                game.render(position=False)
                game.showPlayerCount()
                game.selectFigure()
                game.moveFigure()
            game.render(False)
            game.showPlayerCount()
            game.showWinner()
            input()
    except KeyboardInterrupt:
        exit(0)

if __name__ == '__main__':
    main()