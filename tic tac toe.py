import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = 'X'
        self.board = [' ' for _ in range(9)]
        self.buttons = []
        self.create_widgets()
        self.game_mode = 'Player'

    def create_widgets(self):
        # Create a grid of buttons
        for i in range(9):
            button = tk.Button(self.root, text=' ', font=('Arial', 20), width=5, height=2,
                               command=lambda i=i: self.button_click(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

        # Create the game mode buttons
        tk.Button(self.root, text="Play vs Player", command=self.set_player_mode).grid(row=3, column=0, columnspan=3)
        tk.Button(self.root, text="Play vs AI", command=self.set_ai_mode).grid(row=4, column=0, columnspan=3)
        tk.Button(self.root, text="Reset", command=self.reset_game).grid(row=5, column=0, columnspan=3)

    def set_player_mode(self):
        self.game_mode = 'Player'
        self.reset_game()

    def set_ai_mode(self):
        self.game_mode = 'AI'
        self.reset_game()

    def button_click(self, index):
        if self.board[index] == ' ' and self.current_player != ' ':
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner(self.current_player):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.current_player = ' '
            elif ' ' not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.current_player = ' '
            else:
                if self.game_mode == 'AI' and self.current_player == 'X':
                    self.current_player = 'O'
                    self.ai_move()
                else:
                    self.current_player = 'X' if self.current_player == 'O' else 'O'

    def ai_move(self):
        empty_indices = [i for i, x in enumerate(self.board) if x == ' ']
        if empty_indices:
            move = random.choice(empty_indices)
            self.board[move] = 'O'
            self.buttons[move].config(text='O')
            if self.check_winner('O'):
                messagebox.showinfo("Game Over", "AI wins!")
                self.current_player = ' '
            elif ' ' not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.current_player = ' '

    def check_winner(self, player):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for condition in win_conditions:
            if all(self.board[i] == player for i in condition):
                return True
        return False

    def reset_game(self):
        self.board = [' ' for _ in range(9)]
        for button in self.buttons:
            button.config(text=' ')
        self.current_player = 'X'

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
