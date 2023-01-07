import random
from os import system, name
from time import sleep


def cleanScreen():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def printsResults(playerWins, computerWins, draws):
    print(f"W: {playerWins}\tD: {draws}\tL: {computerWins}\n")


def defe(board, computerSymbol, x, y, z):
    """
    Checks if parameter "x" and "y" are different from empty and Computer symbol, as well as checks if parameter "z" is empty:
    If yes, it returns True, otherwise, it returns False.
    """
    if (
        board[x] != computerSymbol
        and board[x] != " "
        and board[y] != computerSymbol
        and board[y] != " "
        and board[z] == " "
    ):
        return True
    return False


def computerMove(board, computerSymbol):
    """
    Receives the board and symbol (X or O) from the computer and determines where the computer should play
    The board can be empty (if the computer is the first to play) or with some positions filled,
    being the board position 0 discarded.

    Parameters:
    board: list of size 10 representing the board
    computerSymbol: computer letter

    Return:
    Position (between 1 and 9) of the computer's move

    Strategy:


    The computer will check if there are any possible winning combinations,
    if it doesn't win, it will block, as much as possible, the user's victory (if there is a chance for the user to win).
    If there is no winning chance or defense rolls to be made, then he will simply select an empty space with the order of priority:
    [1], [2], [5], [9], [7], [3], [4], [6], [8].
    """
    # Combinações para vencer
    if board[1] == computerSymbol and board[2] == computerSymbol and board[3] == " ":
        j = 3
    elif board[1] == computerSymbol and board[3] == computerSymbol and board[2] == " ":
        j = 2
    elif board[2] == computerSymbol and board[3] == computerSymbol and board[1] == " ":
        j = 1
    elif board[4] == computerSymbol and board[5] == computerSymbol and board[6] == " ":
        j = 6
    elif board[4] == computerSymbol and board[6] == computerSymbol and board[5] == " ":
        j = 5
    elif board[5] == computerSymbol and board[6] == computerSymbol and board[4] == " ":
        j = 4
    elif board[7] == computerSymbol and board[8] == computerSymbol and board[9] == " ":
        j = 9
    elif board[7] == computerSymbol and board[9] == computerSymbol and board[8] == " ":
        j = 8
    elif board[2] == computerSymbol and board[5] == computerSymbol and board[8] == " ":
        j = 8
    elif board[9] == computerSymbol and board[8] == computerSymbol and board[7] == " ":
        j = 7
    elif board[3] == computerSymbol and board[5] == computerSymbol and board[7] == " ":
        j = 7
    elif board[1] == computerSymbol and board[4] == computerSymbol and board[7] == " ":
        j = 7
    elif board[1] == computerSymbol and board[5] == computerSymbol and board[9] == " ":
        j = 9
    elif board[1] == computerSymbol and board[9] == computerSymbol and board[5] == " ":
        j = 5
    elif board[5] == computerSymbol and board[9] == computerSymbol and board[1] == " ":
        j = 1
    elif board[7] == computerSymbol and board[1] == computerSymbol and board[4] == " ":
        j = 4
    elif board[8] == computerSymbol and board[5] == computerSymbol and board[2] == " ":
        j = 2
    elif board[9] == computerSymbol and board[3] == computerSymbol and board[6] == " ":
        j = 6
    elif board[7] == computerSymbol and board[5] == computerSymbol and board[3] == " ":
        j = 3
    elif board[3] == computerSymbol and board[6] == computerSymbol and board[9] == " ":
        j = 9
    elif board[9] == computerSymbol and board[6] == computerSymbol and board[3] == " ":
        j = 3

    # Combinations to defend yourself.

    elif (
        board[7] == computerSymbol
        and board[8] != computerSymbol
        and board[9] != computerSymbol
        and board[5] == computerSymbol
        and board[6] == computerSymbol
        and board[3] != computerSymbol
        and board[4] != computerSymbol
        and board[1] == " "
    ):
        j = 1

    elif (
        board[7] == computerSymbol
        and board[8] != computerSymbol
        and board[9] != computerSymbol
        and board[5] == computerSymbol
        and board[6] == computerSymbol
        and board[3] != computerSymbol
        and board[4] != computerSymbol
        and board[2] == " "
    ):
        j = 2

    elif defe(board, computerSymbol, 1, 2, 3):
        return 3
    elif defe(board, computerSymbol, 1, 3, 2):
        return 2
    elif defe(board, computerSymbol, 8, 5, 2):
        return 2
    elif defe(board, computerSymbol, 2, 3, 1):
        return 1
    elif defe(board, computerSymbol, 4, 5, 6):
        return 6
    elif defe(board, computerSymbol, 4, 6, 5):
        return 5
    elif defe(board, computerSymbol, 5, 6, 4):
        return 4
    elif defe(board, computerSymbol, 7, 1, 4):
        return 4
    elif defe(board, computerSymbol, 7, 8, 9):
        return 9
    elif defe(board, computerSymbol, 7, 9, 8):
        return 8
    elif defe(board, computerSymbol, 9, 8, 7):
        return 7
    elif defe(board, computerSymbol, 1, 4, 7):
        return 7
    elif defe(board, computerSymbol, 1, 5, 9):
        return 9
    elif defe(board, computerSymbol, 1, 9, 5):
        return 5
    elif defe(board, computerSymbol, 5, 9, 1):
        return 1
    elif defe(board, computerSymbol, 3, 5, 7):
        return 7
    elif defe(board, computerSymbol, 2, 5, 8):
        return 8
    elif defe(board, computerSymbol, 9, 3, 6):
        return 6
    elif defe(board, computerSymbol, 9, 6, 3):
        return 3
    elif defe(board, computerSymbol, 3, 6, 9):
        return 9
    elif defe(board, computerSymbol, 7, 2, 5):
        return 5
    elif defe(board, computerSymbol, 2, 8, 5):
        return 5
    elif defe(board, computerSymbol, 7, 3, 8) or defe(board, computerSymbol, 9, 1, 8):
        return 8
    elif defe(board, computerSymbol, 7, 5, 3):
        return 3
    elif defe(board, computerSymbol, 7, 4, 1):
        return 1
    elif board[1] == computerSymbol and board[8] == computerSymbol and board[9] == " ":
        j = 9
    elif board[3] == computerSymbol and board[8] == computerSymbol and board[7] == " ":
        j = 7
    elif board[9] == computerSymbol and board[2] == computerSymbol and board[1] == " ":
        j = 1
    elif board[7] == computerSymbol and board[2] == computerSymbol and board[3] == " ":
        j = 3
    elif (
        board[6] != computerSymbol
        and board[6] != " "
        and defe(board, computerSymbol, 8, 2, 9)
    ):
        return 9

    elif (
        board[1] == computerSymbol
        and board[3] != computerSymbol
        and board[2] != computerSymbol
        and board[5] == " "
    ):
        j = 5

    elif (
        board[8] != computerSymbol
        and board[7] == computerSymbol
        and board[4] != computerSymbol
        and board[3] == " "
    ):
        j = 5

    elif (
        board[1] == computerSymbol
        and board[3] == computerSymbol
        and board[4] != computerSymbol
        and board[5] == " "
    ):
        j = 5

    elif (
        board[1] == computerSymbol
        and board[2] != computerSymbol
        and board[3] == computerSymbol
        and board[7] == " "
    ):
        j = 7
    elif board[1] == computerSymbol and board[3] == computerSymbol and board[5] == " ":
        j = 5
    elif (
        board[1] == computerSymbol
        and board[2] != computerSymbol
        and board[2] != " "
        and board[4] == " "
    ):
        j = 4
    elif (
        board[1] == computerSymbol
        and board[5] != computerSymbol
        and board[5] != " "
        and board[9] == " "
    ):
        j = 9
    elif (
        board[1] == computerSymbol
        and board[7] != computerSymbol
        and board[7] != " "
        and board[9] == " "
    ):
        j = 9
    elif (
        board[8] != computerSymbol
        and board[8] != " "
        and board[3] != computerSymbol
        and board[3] != " "
        and board[9] == " "
    ):
        j = 9

    elif (
        board[2] != computerSymbol
        and board[2] != " "
        and board[4] != computerSymbol
        and board[4] != " "
        and board[5] == " "
    ):
        j = 5
    elif (
        board[6] != computerSymbol
        and board[6] != " "
        and board[2] != computerSymbol
        and board[2] != " "
        and board[3] == computerSymbol
        and board[5] == " "
    ):
        j = 5
    elif (
        board[8] != computerSymbol
        and board[8] != " "
        and board[6] != computerSymbol
        and board[6] != " "
        and board[3] == " "
    ):
        j = 3
    elif (
        board[8] != computerSymbol
        and board[8] != " "
        and board[6] != computerSymbol
        and board[6] != " "
        and board[1] == " "
    ):
        j = 1
    elif (
        board[8] != computerSymbol
        and board[8] != " "
        and board[4] != computerSymbol
        and board[4] != " "
        and board[1] == " "
    ):
        j = 7
    elif (
        board[2] != computerSymbol
        and board[2] != " "
        and board[6] != computerSymbol
        and board[6] != " "
        and board[3] == " "
    ):
        j = 3
    elif (
        board[2] != computerSymbol
        and board[2] != " "
        and board[4] != computerSymbol
        and board[4] != " "
        and board[1] == " "
    ):
        j = 1
    elif (
        board[1] != computerSymbol
        and board[1] != " "
        and board[8] != computerSymbol
        and board[8] != " "
        and board[7] == " "
    ):
        j = 7

    elif board[1] == computerSymbol and board[9] != computerSymbol and board[3] == " ":
        j = 3
    elif board[1] != computerSymbol and board[1] != " " and board[5] == " ":
        j = 5
    elif board[3] != computerSymbol and board[3] != " " and board[5] == " ":
        j = 5
    elif board[7] != computerSymbol and board[7] != " " and board[5] == " ":
        j = 5
    elif board[9] != computerSymbol and board[9] != " " and board[5] == " ":
        j = 5
    elif board[6] != computerSymbol and board[6] != " " and board[3] == " ":
        j = 3

    elif board[8] != computerSymbol and board[8] != " " and board[7] == " ":
        j = 7
    elif (
        board[5] != computerSymbol
        and board[5] != " "
        and board[9] != computerSymbol
        and board[9] != " "
        and board[3] == " "
    ):
        j = 3

    elif (
        board[5] != computerSymbol
        and board[5] != " "
        and board[6] != computerSymbol
        and board[6] != " "
        and board[4] != computerSymbol
        and board[4] != " "
        and board[2] == " "
    ):
        j = 2

    # choose empty positions.
    elif board[1] == " ":
        j = 1
    elif board[2] == " ":
        j = 2
    elif board[5] == " ":
        j = 5
    elif board[9] == " ":
        j = 9
    elif board[7] == " ":
        j = 7
    elif board[3] == " ":
        j = 3
    elif board[4] == " ":
        j = 4
    elif board[6] == " ":
        j = 6
    elif board[8] == " ":
        j = 8
    return j


def checksWinner(x, o, c, d, e):
    """
    It receives the "x" and "o" parameters, the board positions and checks if there was a combination
    of three positions with the same parameter. Finally, returns the winner (if there is a winner), otherwise returns
    None.
    """
    if x == c and x == d and x == e:
        return x
    elif o == c and o == d and o == e:
        return o
    else:
        return None


def checksMove(board, symbol, computerSymbol, playerWins, computerWins, draws):
    """
    Get the board,
    prints if a player ('x' or 'o') won the game and asks if the user wants to play again.
    """
    if (
        checksWinner(symbol, computerSymbol, board[3], board[5], board[7]) == symbol
        or checksWinner(symbol, computerSymbol, board[1], board[5], board[9]) == symbol
        or checksWinner(symbol, computerSymbol, board[1], board[2], board[3]) == symbol
        or checksWinner(symbol, computerSymbol, board[4], board[5], board[6]) == symbol
        or checksWinner(symbol, computerSymbol, board[7], board[8], board[9]) == symbol
        or checksWinner(symbol, computerSymbol, board[1], board[4], board[7]) == symbol
        or checksWinner(symbol, computerSymbol, board[2], board[5], board[8]) == symbol
        or checksWinner(symbol, computerSymbol, board[3], board[6], board[9]) == symbol
    ):
        cleanScreen()
        playerWins += 1
        printsResults(playerWins, computerWins, draws)
        printsBoard(board)
        print("Congratulations! you won the game!")
        choice = input(
            "What a great move, my dear!! Would you like to play again? (Type 'Y' to continue or any other key to end): "
        )
        if choice == "Y" or choice == "y":
            program(playerWins, computerWins, draws)
        else:
            quit()
    elif (
        checksWinner(symbol, computerSymbol, board[3], board[5], board[7])
        == computerSymbol
        or checksWinner(symbol, computerSymbol, board[1], board[5], board[9])
        == computerSymbol
        or checksWinner(symbol, computerSymbol, board[1], board[2], board[3])
        == computerSymbol
        or checksWinner(symbol, computerSymbol, board[4], board[5], board[6])
        == computerSymbol
        or checksWinner(symbol, computerSymbol, board[7], board[8], board[9])
        == computerSymbol
        or checksWinner(symbol, computerSymbol, board[1], board[4], board[7])
        == computerSymbol
        or checksWinner(symbol, computerSymbol, board[2], board[5], board[8])
        == computerSymbol
        or checksWinner(symbol, computerSymbol, board[3], board[6], board[9])
        == computerSymbol
    ):
        cleanScreen()
        computerWins += 1
        printsResults(playerWins, computerWins, draws)
        printsBoard(board)
        print("What a shame! The computer won the game!")
        choice = input(
            "Sometimes life is really complex, my dear. Would you like a rematch? (Type 'Y' to continue or any other key to end): "
        )
        if choice == "Y" or choice == "y":
            program(playerWins, computerWins, draws)
        else:
            quit()
    elif (
        board[1] != " "
        and board[2] != " "
        and board[3] != " "
        and board[4] != " "
        and board[5] != " "
        and board[6] != " "
        and board[7] != " "
        and board[8] != " "
        and board[9] != " "
    ):
        cleanScreen()
        draws += 1
        printsResults(playerWins, computerWins, draws)
        printsBoard(board)
        print("Draw!")
        choice = input(
            "Would you like to play again and make your superiority clear? (Type 'Y' to continue or any other key to end): "
        )
        if choice == "Y" or choice == "y":
            program(playerWins, computerWins, draws)
        else:
            cleanScreen()
            quit()


def board():
    """
    Generates the initial list for building the board.
    """
    l = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    return l


def printsBoard(l):
    """
    Receives the board and prints it.
    """
    print(f" {l[7]} | {l[8]} | {l[9]} ")
    print("---+---+---")
    print(f" {l[4]} | {l[5]} | {l[6]} ")
    print("---+---+---")
    print(f" {l[1]} | {l[2]} | {l[3]} ")


def xo():
    """
    Checks which symbol (X or O) the user wants to be: if he chooses "X" then the computer will be "O" and vice versa.
    Returns the user and computer symbol.
    (The program will accept lowercase X and O as well)
    """
    symbol = input("Hey! Which letter (X or O) would you like to be? ")
    if symbol != "X" and symbol != "O" and symbol != "x" and symbol != "o":
        print("ERROR! Invalid symbol!")
        return xo()
    if symbol == "X":
        computerSymbol = "O"
    if symbol == "O":
        computerSymbol = "X"
    # Minúsculo
    if symbol == "x":
        computerSymbol = "o"
    if symbol == "o":
        computerSymbol = "x"
    return symbol, computerSymbol


def first():
    """
    Randomly chooses who starts playing and returns the choice.
    """
    choice = random.choice(["player", "computer"])
    return choice


def list(position, board, symbol):
    """
    Generates the board update as the game progresses.
    """
    board[position] = symbol
    return board


def ocupation(board, positionn):
    """
    Checks if the position the user has chosen is already occupied.
    If it is, it generates an error message and returns to the position choice again.
    """
    if board[positionn] != " ":
        print("Position already occupied!")
        return position(board)
    return positionn


def position(board):
    """
    Prompts for the user's position choice and checks if it is valid.
    If not valid, it displays an error message and prompts you to choose again.
    Finally, it returns the user's valid choice.
    """
    positionn = input("Choose Which position you want to move: ")
    if (
        positionn != "1"
        and positionn != "2"
        and positionn != "3"
        and positionn != "4"
        and positionn != "5"
        and positionn != "6"
        and positionn != "7"
        and positionn != "8"
        and positionn != "9"
    ):
        print("ERROR: you must type a number between 1-9!")
        return position(board)
    p = int(positionn)
    positionn = ocupation(board, p)
    return positionn


def move(board, symbol, computerSymbol, playerWins, computerWins, draws):
    """
    It promotes the flow of the game when the user is the one who starts.
    """
    printsResults(playerWins, computerWins, draws)
    printsBoard(board)
    positionn = position(board)
    t = list(positionn, board, symbol)
    checksMove(board, symbol, computerSymbol, playerWins, computerWins, draws)
    compMove = computerMove(t, computerSymbol)
    cleanScreen()
    printsResults(playerWins, computerWins, draws)
    printsBoard(t)
    t = list(compMove, t, computerSymbol)
    checksMove(board, symbol, computerSymbol, playerWins, computerWins, draws)
    print("Computer is thinking...")
    sleep(2)
    cleanScreen()
    return move(t, symbol, computerSymbol, playerWins, computerWins, draws)


def move2(board, symbol, computerSymbol, playerWins, computerWins, draws):
    """
    It promotes the flow of the game when the computer starts.
    """
    compMove = computerMove(board, computerSymbol)
    printsResults(playerWins, computerWins, draws)
    printsBoard(board)
    t = list(compMove, board, computerSymbol)
    checksMove(board, symbol, computerSymbol, playerWins, computerWins, draws)
    print("Computer is thinking...")
    sleep(2)
    cleanScreen()
    printsResults(playerWins, computerWins, draws)
    printsBoard(t)
    positionn = position(t)
    t = list(positionn, t, symbol)
    checksMove(board, symbol, computerSymbol, playerWins, computerWins, draws)
    cleanScreen()
    return move2(t, symbol, computerSymbol, playerWins, computerWins, draws)


def game(choice, symbol, computerSymbol, playerWins, computerWins, draws):
    """
    Receives the choice of who starts and the symbols of the participants, then directs the game to
    flow 1 or 2 (move and move2).
    """
    l = board()  # Initial board.
    if choice == "player":
        print("You go first.")
        move(l, symbol, computerSymbol, playerWins, computerWins, draws)
    elif choice == "computer":
        print("Computer goes first.")
        move2(l, symbol, computerSymbol, playerWins, computerWins, draws)


def program(playerWins, computerWins, draws):
    """
    It generates the basic parameters for the rest of the functions and directs them to the rest of the program.
    """
    cleanScreen()
    print("Welcome to TicTacToe!")
    symbol, computerSymbol = xo()
    choice = first()
    game(choice, symbol, computerSymbol, playerWins, computerWins, draws)


def main():
    cleanScreen()
    _ = input("Press any button to continue -->")
    playerWins = 0
    computerWins = 0
    draws = 0
    program(playerWins, computerWins, draws)


if __name__ == "__main__":
    main()
