from tkinter import *

board = [i for i in range(1, 10)]
text = "Добро пожаловать в Крестики-Нолики!"
counter = 0



def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def click_button(num):
    global counter
    global text
    if counter % 2 == 0:
        board[num - 1] = "X"
    else:
        board[num - 1] = "О"
    counter += 1
    if counter > 4:
        tmp = check_win(board)
        if tmp:
            text = f"{tmp} выиграл!"
        if counter == 9:
            text = "Ничья!"

window = Tk()
window.title(f'{text}')
frame = Frame(master=window, bg="lightgray", padx=30, pady=30)
frame.pack()

button_1 = Button(master=frame, text=f"{board[0]}", padx=10, pady=10, width=6, height=2, bg="blue", fg="yellow",
                  command=lambda: click_button(1))
button_1.grid(row=0, column=0)
button_2 = Button(master=frame, text=f"{board[1]}", padx=10, pady=10, width=6, height=2, bg="blue", fg="yellow",
                  command=lambda: click_button(2))
button_2.grid(row=0, column=1)
button_3 = Button(master=frame, text=f"{board[2]}", padx=10, pady=10, width=6, height=2, bg="blue", fg="yellow",
                  command=lambda: click_button(3))
button_3.grid(row=0, column=2)
button_4 = Button(master=frame, text=f"{board[3]}", padx=10, pady=10, width=6, height=2, bg="blue", fg="yellow",
                  command=lambda: click_button(4))
button_4.grid(row=1, column=0)
button_5 = Button(master=frame, text=f"{board[4]}", padx=10, pady=10, width=6, height=2, bg="blue", fg="yellow",
                  command=lambda: click_button(5))
button_5.grid(row=1, column=1)
button_6 = Button(master=frame, text=f"{board[5]}", padx=10, pady=10, width=6, height=2, bg="blue", fg="yellow",
                  command=lambda: click_button(6))
button_6.grid(row=1, column=2)
button_7 = Button(master=frame, text=f"{board[6]}", padx=10, pady=10, width=6, height=2, bg="blue", fg="yellow",
                  command=lambda: click_button(7))
button_7.grid(row=3, column=0)
button_8 = Button(master=frame, text=f"{board[7]}", padx=10, pady=10, width=6, height=2, bg="blue", fg="yellow",
                  command=lambda: click_button(8))
button_8.grid(row=3, column=1)
button_9 = Button(master=frame, text=f"{board[8]}", padx=10, pady=10, width=6, height=2, bg="blue", fg="yellow",
                  command=lambda: click_button(9))
button_9.grid(row=3, column=2)


window.mainloop()
