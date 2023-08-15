from tkinter import *
from tkinter import ttk, filedialog#, messagebox

from window.common import *

import encryption

def basename(f): return f.name.split("/")[-1].split("\\")[-1]

def encrypt(*args):
    def inner():
        f = open("test", "rb")
        test = encryption.test_open_crypto(f, 0x000a0500, basename(f))
        # test.write(b"haiiiii")
        # test.close()
        print(test.read())
    return inner

def apply(tab_e):
    init_row()

    ttk.Label(tab_e, text="Encrypt an .app file for SD drag-n-dropping", font="sans-serif 9 bold").grid(column=0, row=row(), columnspan=3)
    ttk.Label(tab_e, text="WARNING: movable.sed is unique to your own console.\nDon't try someone else's, it will break your DLC install", font="sans-serif 8 bold").grid(column=0, row=new_row(), columnspan=3)
    ttk.Label(tab_e, text="For more information on how to get these files, see insert guide here", font="sans-serif 8").grid(column=0, row=new_row(), columnspan=3)

    ttk.Label(tab_e, text="").grid(row=new_row())

    ttk.Label(tab_e, text="Decrypted .app").grid(column=0, row=new_row())
    in_entry = ttk.Entry(tab_e)
    in_entry.grid(column=1,row=row())
    ttk.Button(tab_e, text="Browse", command=get_fname(in_entry)).grid(column=2, row=row())

    # ttk.Label(tab_e, text="Original .tmd file").grid(column=0, row=new_row())
    # in_entry = ttk.Entry(tab_e)
    # in_entry.grid(column=1,row=row())
    # ttk.Button(tab_e, text="Browse", command=get_fname(in_entry)).grid(column=2, row=row())

    ttk.Label(tab_e, text="boot9.bin file").grid(column=0, row=new_row())
    boot9_entry = ttk.Entry(tab_e)
    boot9_entry.grid(column=1,row=row())
    ttk.Button(tab_e, text="Browse", command=get_fname(boot9_entry)).grid(column=2, row=row())

    ttk.Label(tab_e, text="Your movable.sed file").grid(column=0, row=new_row())
    movable_entry = ttk.Entry(tab_e)
    movable_entry.grid(column=1,row=row())
    ttk.Button(tab_e, text="Browse", command=get_fname(movable_entry)).grid(column=2, row=row())

    ttk.Label(tab_e, text="Output directory").grid(column=0, row=new_row())
    out_entry = ttk.Entry(tab_e)
    out_entry.grid(column=1,row=row())
    ttk.Button(tab_e, text="Browse", command=get_dname(out_entry)).grid(column=2, row=row())

    ttk.Button(tab_e, text="Encrypt!", command=encrypt(in_entry, boot9_entry, movable_entry, out_entry)).grid(column=2, row=new_row())
