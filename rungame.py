import tictactoe
import random
p1score = 0
p2score = 0
ties = 0

print('Welcome to Tic-Tac-Toe!')

while True:
    print()
    print('Please decide who is Player 1 and who is Player 2.')
    print()
    p1, p2 = tictactoe.inputPlayerLetters()
    print()
    print('Selecting a random player to begin the first turn.')

    game = tictactoe.Game(p1, p2, random.randint(0, 1))

    while game.game_status == 1:
        if game.getCurrentPlayer() == 0:
            # Player 1's turn.
            game.printBoard()
            move = game.getPlayerMove()
            game.makeMove(game.p1, move)

            if game.isWinner(game.p1):
                game.printBoard()
                print('Player 1 has won the game!')
                p1score += 1
                game.endGame()
            else:
                if game.isBoardFull():
                    game.printBoard()
                    print('The game is a tie!')
                    ties += 1
                    break
                else:
                    game.advanceTurn()

        else:
            # Player 2's turn.
            game.printBoard()
            move = game.getPlayerMove()
            game.makeMove(game.p2, move)

            if game.isWinner(game.p2):
                game.printBoard()
                print('Player 2 has won the game!')
                p2score += 1
                game.endGame()
            else:
                if game.isBoardFull():
                    game.printBoard()
                    print('The game is a tie!')
                    ties += 1
                    break
                else:
                    game.advanceTurn()

    # this statement deletes the object so a new game can be created
    game = None

    # displays the score
    score = tictactoe.score(p1score, p2score, ties)
    print(score)

    if not tictactoe.playAgain():
        print()
        print('Goodbye')
        break
