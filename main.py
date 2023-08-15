from tkinter import *
from tkinter import ttk

from window import create, extract, encrypt

root = Tk()
root.title("3DS DLC/CFA Tool")

tabs = ttk.Notebook(root)
tab_x = ttk.Frame(tabs, padding=10)
tab_c = ttk.Frame(tabs, padding=10)
tab_e = ttk.Frame(tabs, padding=10)
tabs.add(tab_x, text='Extract')
tabs.add(tab_c, text='Create')
tabs.add(tab_e, text='Encrypt')

tabs.pack(expand=1, fill="both")

extract.apply(tab_x)
create.apply(tab_c)
encrypt.apply(tab_e)

root.mainloop()