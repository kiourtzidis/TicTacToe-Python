from time import sleep
from functions import *

def main():

    stats = {
    'friend': {'X': 0, 'O': 0, 'round': 1},
    'computer': {'player': 0, 'computer': 0}
    }

    prev_mode = None

    print('\nWelcome To Tic Tac Toe!')

    while True:

        print('\n1 - Friend')
        print('2 - Computer\n')

        game_choice = input_validation('Who Do You Want To Play Against?: ', 1, 2)

        if game_choice == 1:

            board = reset_board()

            if prev_mode == 'computer' and stats['friend']['round'] > 1:
                reset = input('\nStart A New Match?(y/n): ').lower()
                while reset not in ('y', 'n'):
                    reset = input('Invalid input, please enter \'y\' for yes or \'n\' for no: ').lower()
                if reset == 'y':
                    reset_score(stats)
                else:
                    print('\nRetrieving Saved Game Data', end = '')
                    for i in range(3):
                        print('.', end='', flush = True)
                        sleep(0.5)
                    print('')
                     
            print(f'\nRound {stats['friend']['round']}')
            
            player = 'O'

            for turn in range(9):

                print_board(board)

                if player == 'X':
                    player = 'O'
                else:
                    player = 'X'
                print(f'\nPlayer\'s {player} Turn')

                while True:
                    row = input_validation('Enter row: ', 1, 3)
                    column = input_validation('Enter column: ', 1, 3)
                    if board[row - 1][column - 1] != ' ':
                        print('Pick an empty box\n')
                        continue
                    else:
                        board[row - 1][column - 1] = player
                        break

                winner = False
                for i in range(3):
                    if check_row(board, i):
                        winner = player
                        break
                    elif check_column(board, i):
                        winner = player
                        break
                if not winner:
                    if check_diagonals(board):
                        winner = player
                if winner:
                    print_board(board)
                    print(f'\nPlayer {player} Won!')

                    if winner == 'X':
                        stats['friend']['X'] += 1
                    else:
                        stats['friend']['O'] += 1

                    print_score(stats['friend']['X'], stats['friend']['O'])
                    stats['friend']['round'] += 1
                    break
            else:
                print_board(board)
                print('\nTie!')
                print_score(stats['friend']['X'], stats['friend']['O'])
                stats['friend']['round'] += 1

            prev_mode = 'friend'

            end_choice = input('\nDo you want to play another round?(y/n): ').lower()
            while end_choice not in ('y', 'n'):
                end_choice = input('Invalid input, please enter \'y\' for yes or \'n\' for no: ').lower()

            if end_choice == 'y':
                continue 
            else:
                print('\nThanks For Playing!\n')
                break 

        elif game_choice == 2:

            board = reset_board()

            print('\n1 - Easy\n2 - Medium\n3 - Hard\n4 - Impossible\n')
            level = input_validation('Choose the computer\'s AI level: ', 1, 4)

            player_symbol = input('\nChoose your symbol(X/O): ').upper()
            while player_symbol not in ('X', 'O'):
                player_symbol = input('\nPlease choose a valid symbol(X/O): ').upper()
            computer_symbol = 'O' if player_symbol == 'X' else 'X'

            current_player = 'X'

            for turn in range(9):

                print_board(board)

                if current_player == player_symbol:
                    print('\nYour Turn!')
                else:
                    print('\nComputer is thinking', end = '')
                    for i in range(3):
                        print('.', end='', flush = True)
                        sleep(0.5)
                    print('')

                while True:
                    if current_player == player_symbol:
                        row = input_validation('Enter row: ', 1, 3)
                        column = input_validation('Enter column: ', 1, 3)
                        if board[row - 1][column - 1] != ' ':
                            print('Pick an empty box\n')
                            continue
                        else:
                            board[row - 1][column - 1] = player_symbol
                            break
                    else:
                        pos = computer_move(board, level, player_symbol, computer_symbol)
                        if pos is None:
                            break
                        board[pos[0]][pos[1]] = computer_symbol
                        break

                winner = False
                for i in range(3):
                    if check_row(board, i):
                        winner = current_player
                        break
                    elif check_column(board, i):
                        winner = current_player
                        break
                if not winner:
                    if check_diagonals(board):
                        winner = current_player
                if winner:
                    print_board(board)
                    print('You Won!') if current_player == player_symbol else print('Game Over')
                    break

                current_player = computer_symbol if current_player == player_symbol else player_symbol
            else:
                print_board(board)
                print('\nTie!')

            prev_mode = 'computer'

            end_choice = input('\nDo you want to play another round?(y/n): ').lower()
            while end_choice not in ('y', 'n'):
                end_choice = input('Invalid input, please enter \'y\' for yes or \'n\' for no: ').lower()

            if end_choice == 'y':
                continue
            else:
                print('\nThanks For Playing!\n')
                break

if __name__ == '__main__':
    main() 