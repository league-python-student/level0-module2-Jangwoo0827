import random
from tkinter import messagebox, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
for i in range(10):
    r = random.randint(1, 5)
    if r == 1:
        messagebox.showinfo(title=None, message="Good!")
    if r == 2:
        messagebox.showinfo(title=None, message="Excellent!")
    if r == 3:
        messagebox.showinfo(title=None, message="Nice!")
    if r == 4:
        messagebox.showinfo(title=None, message="Really good!")
    if r == 5:
        messagebox.showinfo(title=None, message="Really nice!")

    # TODO 1) Use each value of random_number to give the user a random compliment

    # TODO 2) Repeat all the code above 10 times

    # TODO 3) Find someone to test out your program. They will like it :)
