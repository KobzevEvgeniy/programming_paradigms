import ziro_cross

if __name__ == '__main__':

    game = ziro_cross.TicTacToe()
    while True:
        position = int(input("Enter your move (0-8): "))
        if game.move(position):
            break
