from tkinter import *
from tkinter import ttk, filedialog, messagebox

from window.common import *

import cli

def extract(header_path, romfs_path, in_path):
    def inner():
        #TODO: detect if it's a CIA
        cli.extract_3dstool(header_path.get(), romfs_path.get(), in_path.get())
        messagebox.showinfo("Extracting completed", "Done!")
    return inner


def apply(tab_x):
    init_row()

    ttk.Label(tab_x, text="Extract a DLC .app to header + RomFS", font="sans-serif 9 bold").grid(column=0, row=row(), columnspan=3)

    ttk.Label(tab_x, text="Input file (.app)").grid(column=0, row=new_row())
    in_entry = ttk.Entry(tab_x)
    in_entry.grid(column=1,row=row())
    ttk.Button(tab_x, text="Browse", command=get_fname(in_entry)).grid(column=2, row=row())

    ttk.Label(tab_x, text="Header (ncch.bin)").grid(column=0, row=new_row())
    ncch_entry = ttk.Entry(tab_x)
    ncch_entry.grid(column=1,row=row())
    ttk.Button(tab_x, text="Browse", command=get_fname_out(ncch_entry, initialfile="ncch.bin")).grid(column=2, row=row())

    ttk.Label(tab_x, text="RomFS folder").grid(column=0, row=new_row())
    romfs_entry = ttk.Entry(tab_x)
    romfs_entry.grid(column=1,row=row())
    ttk.Button(tab_x, text="Browse", command=get_fname_out(romfs_entry, initialfile="romfs")).grid(column=2, row=row())

    ttk.Button(tab_x, text="Convert!", command=extract(ncch_entry, romfs_entry, in_entry)).grid(column=2, row=new_row())
