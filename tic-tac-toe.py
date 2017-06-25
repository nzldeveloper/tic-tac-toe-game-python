'''
This is a tic tac toe game for 2 players
player 1 = X
player 2 = O
type start() to start the game
The game splits the board into 9 squares, and players enter which square they'd like to mark next
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
'''

board = dict.fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9], ' ')


def print_board():
    print('| ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' |')
    print('-------------')
    print('| ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' |')
    print('-------------')
    print('| ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' |')
    print('-------------')


def start():
    print("*****The game splits the board into 9 squares, and players enter which square they'd like to mark next. "
          "\nFirst player to go is X and second player is O"
          "\n1 | 2 | 3"
          "\n---------"
          "\n4 | 5 | 6"
          "\n---------"
          "\n7 | 8 | 9*****")
    print('')
    print('***GAME START***')
    for moves in range(1, 10):
        win = False
        player_input = int(input('Please enter your next move: '))
        if player_input > 9 or player_input < 0:
            #restarting the game if player enters invalid numbers
            print('Please enter a number between 1 and 9. Restarting the game...')
            restart()
        else:
            if moves % 2 != 0:
                board[player_input] = 'X'
                print_board()
            else:
                board[player_input] = 'O'
                print_board()
            if moves >= 5:
                winning = [[board[1], board[2], board[3]], [board[4], board[5], board[6]], [board[7], board[8], board[9]],
                           [board[1], board[4], board[7]], [board[2], board[5], board[8]], [board[3], board[6], board[9]],
                           [board[1], board[5], board[9]], [board[3], board[5], board[7]]]
                for items in winning:
                    if set(items) == {'X'}:
                        print('Player X won')
                        win = True
                        break
                    elif set(items) == {'O'}:
                        print('Player O won')
                        win = True
                        break
            if win:
                break

    else:
        print('It is a tie!')
    play_again = input("Want to play again? (Y/N): ")
    if play_again == "y" or play_again == "Y":
        restart()

#restart function clears the board and runs the start() function again
def restart():
    global board
    board = dict.fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9], ' ')
    start()

start()

