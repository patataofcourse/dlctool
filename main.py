from tkinter import *
from tkinter import ttk

from window import create, extract

root = Tk()
root.title("CFA Tool")

tabs = ttk.Notebook(root)
tab_x = ttk.Frame(tabs, padding=10)
tab_c = ttk.Frame(tabs, padding=10)
tabs.add(tab_x, text='Extract')
tabs.add(tab_c, text='Create')

tabs.pack(expand=1, fill="both")

extract.apply(tab_x)
create.apply(tab_c)

root.mainloop()