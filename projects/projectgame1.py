print("x" * 10, " TIC TAC TOE ", "0" * 10)
print("HELLO PLAYERS:\n1 - to start the GAME\n2 - HELP ")
choice = int(input())

if choice == 1:
    pass
    board = list(range(1, 10))

# drawing the playing field in a format familiar to humans using the function "def draw_board" # noqa
# Inside the program, the playing field is presented as a one-dimensional list with numbers from 1 to 9. # noqa
    def draw_board(board):
        print("-" * 13)
        for i in range(3):
            # printing our board
            print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
            print("-" * 13)

    # take_input() – Takes user input. Checks the correctness of the input
    '''
    Tasks of this function:
    1. Accept user input.

    2. Process invalid input, for example, not a number was entered.
    To convert a string to a number, use the int () function.

    3. Process situations.
    when the cell is occupied or when a number is entered
    that is not in the range 1..9.to process incorrect input,
    we use the try...except block.
    If the user enters a string, the program will not be interrupted,
    but the message “invalid input. Are you sure you entered a number?”,
    and then the loop will move to the next iteration
    with the ability to re-enter the number.
    '''
    def take_input(player_token):
        valid = False
        while not valid:
            player_answer = input("Where will we put " + player_token+"? ")
            try:
                player_answer = int(player_answer)
            except:
                print("Invalid input. Are you sure that you entered the number?")  # noqa
                continue
            if player_answer >= 1 and player_answer <= 9:
                if(str(board[player_answer-1]) not in "XO"):
                    board[player_answer-1] = player_token
                    valid = True
                else:
                    print("This cage is already occupied!")
            else:
                print("Invalid input. Enter a number between 1 and 9.")

    # check_win - function for checking the playing field, checks if the player has won  # noqa
    '''
    This function checks the playing field.
    We create a tuple with the winning coordinates and run a for loop through it.  # noqa

    If the symbols in all three specified cells are equal,
    we return the winning symbol. otherwise, we return False.

    A non-empty string(the winning symbol) when it is converted to a Boolean type,  # noqa
    it returns True.
    '''
    def check_win(board):
        win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))  # noqa
        for each in win_coord:
            if board[each[0]] == board[each[1]] == board[each[2]]:
                return board[each[0]]
        return False

    # main () is the main function of the game, which will run all the previously described functions. This function launches and controls the gameplay. # noqa
        '''
        In this function, create a while loop.
        The loop runs until one of the players wins.
        In this loop, we display the playing field, accept user input,
        and determine the player's token(x or zero).

    We are waiting for the counter variable to become greater
    than 4 in order to avoid a deliberately unnecessary call
    to the check_win function.

    The tmp variable was created in order
    not to call the check_win function once again,
    we just “remember” its value
    and use it in the “print(tmp, “won!”)”line if necessary.
        '''
    def main(board):
        counter = 0
        win = False
        while not win:
            draw_board(board)
            if counter % 2 == 0:
                take_input("X")
            else:
                take_input("O")
            counter += 1
            if counter > 4:
                tmp = check_win(board)
                if tmp:
                    print(tmp, "won!")
                    win = True
                    break
            if counter == 9:
                print("Draw!")
                break
        draw_board(board)
    main(board)


if choice == 2:
    print("Tic-tac-toe, or Xs and Os, is a paper-and-pencil game for two players, X and O, who take turns marking the spaces in a 3×3 grid. ... The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner.")  # noqa

input("Press Enter to exit!")
