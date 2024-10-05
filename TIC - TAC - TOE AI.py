import random

board = ["_", "_", "_",
         "_" ,"_", "_",
         "_", "_", "_"]
currentplayer = "x"
winner = None
gameRunning = True

# Printing the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

def playerInput(board, player):
    while True:
        try:
            inp = int(input(f"Player {player}, enter a number 1-9: "))
            if inp >= 1 and inp <= 9:
                if board[inp - 1] == "_":
                    board[inp - 1] = player
                    break
                else:
                    print("Oops! The spot is already taken. Try again.")
            else:
                print("Invalid number! Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def checkWinner(board):
    # Define winning combinations
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]               # Diagonals
    ]
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "_":
            return board[combo[0]]
    
    if "_" not in board:
        return "Tie"
    
    return None

def main():
    global currentplayer, winner, gameRunning
    printBoard(board)
    
    while gameRunning:
        playerInput(board, currentplayer)
        printBoard(board)
        
        winner = checkWinner(board)
        
        if winner:
            if winner == "Tie":
                print("It's a tie!")
            else:
                print(f"Player {winner} wins!")
            gameRunning = False
        else:
            currentplayer = "o" if currentplayer == "x" else "x"
           # Start the game
main()
    