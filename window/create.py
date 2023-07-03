from tkinter import *
from tkinter import ttk, filedialog, messagebox

from window.common import *

import cli

def create(header_path, romfs_path, out_path):
    def inner():
        cli.create_3dstool(header_path.get(), romfs_path.get(), out_path.get())
        messagebox.showinfo("Creating completed", "Done!")
    return inner


def apply(tab_c):
    ttk.Label(tab_c, text="Create a DLC .app from header + RomFS", font="sans-serif 9 bold").grid(column=0, row=0, columnspan=3)

    ttk.Label(tab_c, text="Header (ncch.bin)").grid(column=0, row=1)
    ncch_entry = ttk.Entry(tab_c)
    ncch_entry.grid(column=1,row=1)
    ttk.Button(tab_c, text="Browse", command=get_fname(ncch_entry)).grid(column=2, row=1)

    ttk.Label(tab_c, text="RomFS folder").grid(column=0, row=2)
    romfs_entry = ttk.Entry(tab_c)
    romfs_entry.grid(column=1,row=2)
    ttk.Button(tab_c, text="Browse", command=get_dname(romfs_entry)).grid(column=2, row=2)

    ttk.Label(tab_c, text="Output file (.app)").grid(column=0, row=3)
    out_entry = ttk.Entry(tab_c)
    out_entry.grid(column=1,row=3)
    ttk.Button(tab_c, text="Browse", command=get_fname_out(out_entry, initialfile="romfs")).grid(column=2, row=3)

    #ttk.Label(tab_c, text="Output type").grid(column=0, row=4)
    #out_type = ttk.Combobox(tab_c,values=["CIA (.cia)", "CFA/NCCH (.app)"])
    #out_type.set("CIA (.cia)")
    #out_type.grid(column=1,row=4)

    ttk.Button(tab_c, text="Convert!", command=create(ncch_entry, romfs_entry, out_entry)).grid(column=2, row=5)
