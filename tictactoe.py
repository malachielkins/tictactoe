# Tic Tac Toe Game class module

import random


class Game:

    # p1 and p2 are the letters that the two players chose
    # game_status set to 1 means the game is still being played. 0 means the game is over
    # current_player is the current player who is still on their turn (0 is player 1, 1 is player 2)
    def __init__(self, p1, p2, current_player):
        self.board = [' '] * 10
        self.p1 = p1
        self.p2 = p2
        self.game_status = 1
        self.current_player = current_player

    def __repr__(self):
        return ('<' + self.__class__.__name__ +
                ' board=' + str(self.board) +
                ' player1=' + str(self.p1) +
                ' player2=' + str(self.p2) +
                ' game_status=' + str(self.game_status) +
                ' current_player=' + str(self.current_player) +
                '>')

    def getBoardCopy(self):
        # Make a duplicate of the board list and return it the duplicate.
        dupe_board = []

        for i in self.board:
            dupe_board.append(i)

        return dupe_board

    def getCurrentPlayer(self):
        return self.current_player

    def printBoard(self):
        # This function prints out the board that it was passed.

        # "board" is a list of 10 strings representing the board (ignore index 0)
        print()
        print('   |   |')
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print('   |   |')

    def makeMove(self, player_letter, location):
        self.board[location] = player_letter

    def isSpaceFree(self, location):
        # Return true if the passed move is free on the passed board.
        return self.board[location] == ' '

    def getPlayerMove(self):
        # Let the player type in his move.
        move = ' '

        if self.getCurrentPlayer() == 0:
            while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.isSpaceFree(int(move)):
                print('Player 1, what is your next move? (1-9)')
                move = input()
        else:
            while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.isSpaceFree(int(move)):
                print('Player 2, what is your next move? (1-9)')
                move = input()

        return int(move)

    def advanceTurn(self):
        if self.getCurrentPlayer() == 0:
            self.current_player = 1
        else:
            self.current_player = 0

    def isWinner(self, le):
        bo = self.board

        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
                (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
                (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
                (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
                (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
                (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
                (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
                (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal

    def isBoardFull(self):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if self.isSpaceFree(i):
                return False
        return True

    def endGame(self):
        self.game_status = 0


def inputPlayerLetters():
    # Chooses a random player and stores it in random_player
    random_int = random.randint(0, 1)
    random_player = "Player 1"

    if random_int == 1:
        random_player = "Player 2"

    # Lets a random player type which letter they want to be.
    # Returns a list with Player 1's letter as the first item, and Player 2's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Choosing a random player to select their letter...')
        print('%s, do you want to be X or O?' % random_player)
        letter = input().upper()

    # the first element in the tuple is the chosen player's letter, the second is the second player's letter.
    if letter == 'O':
        if random_int == 1:
            print('Player 1 will be X, Player 2 will be O.')
            return ['X', 'O']

        print('Player 1 will be O, Player 2 will be X.')
        return ['O', 'X']
    else:
        if random_int == 1:
            print('Player 1 will be O, Player 2 will be X.')
            return ['O', 'X']

        print('Player 1 will be X, Player 2 will be O.')
        return ['X', 'O']

def score(p1, p2, ties):
    # This function shows how many times each player has won, as well as how many ties there have been.
    return('''Score:
    P1 wins: %s
    P2 wins: %s
    Ties: %s''' % (p1, p2, ties))

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')
