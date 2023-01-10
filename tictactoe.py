import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha")
        
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.player = 'X'
        
        self.create_widgets()
        
    def create_widgets(self):
        self.buttons = [[tk.Button(self.root, width=5, height=2, command=lambda r=r, c=c: self.play(r, c)) for c in range(3)] for r in range(3)]
        
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].grid(row=r, column=c)
                
        self.restart_button = tk.Button(self.root, text="Reiniciar", command=self.restart)
        self.restart_button.grid(row=3, column=1)
        
    def play(self, row, col):
        if self.board[row][col] != ' ':
            return
        
        self.buttons[row][col]["text"] = self.player
        self.board[row][col] = self.player
        
        winner = self.check_winner()
        if winner:
            self.show_winner(winner)
        elif self.is_full():
            self.show_winner('empate')
        else:
            self.player = 'O' if self.player == 'X' else 'X'
    
    def check_winner(self):
        lines = (
            self.board[0],  # first row
            self.board[1],  # second row
            self.board[2],  # third row
            [self.board[0][0], self.board[1][0], self.board[2][0]],  # first col
            [self.board[0][1], self.board[1][1], self.board[2][1]],  # second col
            [self.board[0][2], self.board[1][2], self.board[2][2]],  # third col
            [self.board[0][0], self.board[1][1], self.board[2][2]],  # diagonal
            [self.board[0][2], self.board[1][1], self.board[2][0]],  # diagonal
        )
        if any(all(cell == self.player for cell in line) for line in lines):
            return self.player
        return None
    
    def is_full(self):
        return all(all(cell != ' ' for cell in row) for row in self.board)
    
    def show_winner(self, winner):
        if winner == 'empate':
            message = "Empate!"
        else:
            message = winner + " ganhou!"
        messagebox.showinfo("Fim de Jogo", message)
    
    def restart(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.player = 'X'
        for r in range(3):
            for c in range(3):
                self.buttons[r][c]["text"] = ' '
                
if __name__ == '__main__':
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
