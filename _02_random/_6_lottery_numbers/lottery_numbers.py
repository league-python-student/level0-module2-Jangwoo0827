import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    # TODO 1) Get 6 random numbers to put on your lottery ticket
    r: int = random.randint(1, 6)
    # TODO 2) Display the selected numbers to the user in a pop-up
    if r == 1:
        messagebox.showinfo(title="AA", message="lottery ticket 1")
    if r == 2:
        messagebox.showinfo(title="BB", message="lottery ticket 2")
    if r == 3:
        messagebox.showinfo(title="CC", message="lottery ticket 3")
    if r == 4:
        messagebox.showinfo(title="DD", message="lottery ticket 4")
    if r == 5:
        messagebox.showinfo(title="EE", message="lottery ticket 5")
    if r == 6:
        messagebox.showinfo(title="FF", message="lottery ticket 6")
    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
