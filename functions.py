from random import random, randrange

def input_validation(prompt, min_val, max_val):

    while True:

        try:
            num = int(input(prompt))
            if min_val <= num <= max_val:
                return num
            else:
                print(f'\nPlease enter a valid option({min_val}-{max_val})')

        except ValueError:
            print(f'\nPlease enter a valid option({min_val}-{max_val})')


def print_board(board):

    print('\n    1   2   3')
    print('  +---+---+---+ ')
    for i in range(3):
        print(f'{i+1} | {board[i][0]} | {board[i][1]} | {board[i][2]} |')
        print('  +---+---+---+')
    print('')


def print_score(score1, score2):
    print(f'\n| Player X: {score1}')
    print(f'| Player O: {score2}')


def reset_board():
    return [[' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]


def reset_score(stats):

    stats['friend']['X'] = 0
    stats['friend']['O'] = 0
    stats['friend']['round'] = 1


def check_row(board, row):
    return (board[row][0] == board[row][1] == board[row][2]) and board[row][0] != ' '


def check_column(board, column):
    return (board[0][column] == board[1][column] == board[2][column]) and board[0][column] != ' '


def check_diagonals(board):
    return ((board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ')
            or (board[2][0] == board[1][1] == board[0][2] and board[2][0] != ' '))


def computer_move(board, level, player_symbol, computer_symbol):

    def check_threat(sequence, symbol):
        cnt = 0
        empty = None
        for pos in sequence:
            if board[pos[0]][pos[1]] == symbol:
                cnt += 1
            elif board[pos[0]][pos[1]] == ' ':
                empty = pos

        if cnt == 2 and empty is not None:
            return empty
        return None


    def danger(symbol):
        for i in range(3):
            row = [(i, j) for j in range(3)]
            pos = check_threat(row, symbol)
            if pos is not None:
                return pos

        for j in range(3):
            column = [(i, j) for i in range(3)]
            pos = check_threat(column, symbol)
            if pos is not None:
                return pos

        pos = check_threat([(0, 0), (1, 1), (2, 2)], symbol)
        if pos is not None:
            return pos

        pos = check_threat([(0, 2), (1, 1), (2, 0)], symbol)
        if pos is not None:
            return pos


    if level == 1:
        pos = danger(computer_symbol)
        if pos is not None and random() < 0.3:
            return pos
        pos = danger(player_symbol)
        if pos is not None and random() < 0.3:
            return pos
        
        empty_squares = [] 
        for i in range(3): 
            for j in range(3): 
                if board[i][j] == ' ': 
                    empty_squares.append((i, j))

        if not empty_squares: 
            return None
        
        return empty_squares[randrange(len(empty_squares))]

    elif level == 2:
        pos = danger(computer_symbol)
        if pos is not None and random() < 0.65:
            return pos
        pos = danger(player_symbol)
        if pos is not None and random() < 0.65:
            return pos
        elif board[1][1] == ' ' and random() < 0.7:
            return (1, 1)
        else:
            empty_squares = [] 
            for i in range(3): 
                for j in range(3): 
                    if board[i][j] == ' ': 
                        empty_squares.append((i, j))

            if not empty_squares: 
                return None
        
            return empty_squares[randrange(len(empty_squares))]

    elif level == 3:
        pos = danger(computer_symbol)
        if pos is not None and random() < 0.90:
            return pos
        pos = danger(player_symbol)
        if pos is not None and random() < 0.90:
            return pos
        elif board[1][1] == ' ':
            return (1, 1)
        else:
            empty_squares = [] 
            for i in range(3): 
                for j in range(3): 
                    if board[i][j] == ' ': 
                        empty_squares.append((i, j))

            if not empty_squares: 
                return None
        
            return empty_squares[randrange(len(empty_squares))]

    elif level == 4:
        pos = danger(computer_symbol)
        if pos is not None:
            return pos
        pos = danger(player_symbol)
        if pos is not None:
            return pos
        elif board[1][1] == ' ':
            return (1, 1)
        else:
            corner_squares = [(0, 0), (0, 2), (2, 0), (2, 2)]
            empty_squares = []
            for pos in corner_squares:
                if board[pos[0]][pos[1]] == ' ':
                    empty_squares.append(pos)
            if empty_squares:
                return empty_squares[randrange(len(empty_squares))]

            middle_squares = [(1, 0), (0, 1), (1, 2), (2, 1)]
            empty_squares = []
            for pos in middle_squares:
                if board[pos[0]][pos[1]] == ' ':
                    empty_squares.append(pos)
            if empty_squares:
                return empty_squares[randrange(len(empty_squares))]
            
            return None 