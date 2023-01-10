import tkinter as tk

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Jogo da Velha")

        self.buttons = []
        for i in range(3):
            self.buttons.append([])
            for j in range(3):
                button = tk.Button(self.root, width=10, height=5, command=lambda i=i, j=j: self.play(i, j))
                button.grid(row=i, column=j)
                self.buttons[i].append(button)

        self.player = "X"
        self.root.mainloop()

    def play(self, i, j):
        button = self.buttons[i][j]
        if button["text"] == "":
            button["text"] = self.player
            self.check_win()
            self.player = "O" if self.player == "X" else "X"

    def check_win(self):
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                self.end_game(self.buttons[i][0]["text"] + " ganhou!")
            elif self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != "":
                self.end_game(self.buttons[0][i]["text"] + " ganhou!")
        
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            self.end_game(self.buttons[0][0]["text"] + " ganhou!")
        elif self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            self.end_game(self.buttons[0][2]["text"] + " ganhou!")

    def end_game(self, message):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["state"] = "disabled"
        
        tk.Label(self.root, text=message).grid(row=3, column=0, columnspan=3)


if __name__ == "__main__":
    TicTacToe()
