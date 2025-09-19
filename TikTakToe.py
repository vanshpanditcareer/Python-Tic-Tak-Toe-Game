import tkinter as tk
from tkinter import messagebox

def check_winner():
    global winner
    win_combos = [[0,1,2],[3,4,5],[6,7,8],
                  [0,3,6],[1,4,7],[2,5,8],
                  [0,4,8],[2,4,6]]
    for combo in win_combos:
        if (buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"]) and buttons[combo[0]]["text"] != "":
            for i in combo:
                buttons[i].config(bg="lightgreen")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} Wins!")
            winner = True
            return

def button_click(index):
    global current_player
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        if not winner:
            toggle_player()

def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")

root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = [tk.Button(root, text="", font=("normal", 25), width=6, height=2, 
            command=lambda i=i: button_click(i)) for i in range(9)]

for i, btn in enumerate(buttons):
    btn.grid(row=i//3, column=i%3)

current_player = "X"
winner = False
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()
