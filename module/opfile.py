import tkinter as tk
from tkinter import filedialog


def opfile():
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askopenfilename()
    return (path)


def opdir():
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askdirectory()
    return (path)


def opfiles(title='打开'):
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askopenfilename(multiple='True', title=title)
    return (path)
