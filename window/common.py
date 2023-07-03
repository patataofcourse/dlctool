from tkinter import *
from tkinter import ttk, filedialog, messagebox

def get_fname(entry, **options):
    def inner():
        entry.delete(0, END)
        entry.insert(0, filedialog.askopenfilename(**options))
    return inner

def get_dname(entry, **options):
    def inner():
        entry.delete(0, END)
        entry.insert(0, filedialog.askdirectory(**options))
    return inner

def get_fname_out(entry, **options):
    def inner():
        entry.delete(0, END)
        entry.insert(0, filedialog.asksaveasfilename(**options))
    return inner