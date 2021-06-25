from tkinter import *
import random
from types import BuiltinFunctionType

window = Tk()


def Result(x, pos_x, pos_y):
        # this creates a new label to the GUI
    label = Label(
        window, fg='white', bg='black', text=str(x))
    label.place(x=pos_x, y=pos_y)
    # label.pack()


def which_button(user_choice):
    d = {'r': 'Rock!', 'p': 'Paper!', 's': 'Scissors!'}

    x = "Challenger uses " + d[user_choice] + "    "
    Result(x, 80, 150)

    computer = random.choice(['r', 'p', 's'])
    y = "Opponent uses " + d[computer] + "    "
    Result(y, 80, 180)

    if user_choice == computer:
        Result('It\'s a tie!                  ', 80, 230)
    elif (user_choice == 'r' and computer == 's') or (user_choice == 'p' and computer == 'r') or (user_choice == 's' and computer == 'p'):
        Result('Challenger Wins!    ', 80, 230)
    else:
        Result('Opponent Wins!   ', 80, 230)


def __main__():
    lbl = Label(window, text="Choose your Weapon!",
                fg='White', bg='black', font=("Raleway", 12))
    lbl.place(x=60, y=50)

    rock = Button(window, text="Rock",
                  command=lambda: which_button('r'))
    paper = Button(window, text="Paper",
                   command=lambda: which_button('p'))
    scissor = Button(window, text="Scissor",
                     command=lambda: which_button('s'))
    rock.place(x=60, y=100)
    paper.place(x=115, y=100)
    scissor.place(x=170, y=100)
    window.title('Rock-Paper-Scissors')
    window.geometry("300x300+10+10")
    window.configure(background='black')
    window.mainloop()


__main__()
