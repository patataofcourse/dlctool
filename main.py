from tkinter import *
from tkinter import ttk, filedialog, messagebox
import subprocess
import os

_3dstool = "./3dstool" if os.path.isfile("3dstool") and os.name == "posix" else "3dstool"

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

def extract_3dstool(header_path, romfs_path, out_path):
    #todo: get proper temp path
    subprocess.check_call([_3dstool, "-x", "-t", "cfa", "-f", out_path, "--header", header_path, "--romfs", "temp_romfs.bin"])
    subprocess.check_call([_3dstool, "-x", "-t", "romfs", "-f", "temp_romfs.bin", "--romfs-dir", romfs_path])
    os.remove("temp_romfs.bin")

def create_3dstool(header_path, romfs_path, out_path):
    #todo: get proper temp path
    subprocess.check_call([_3dstool, "-c", "-t", "romfs", "-f", "temp_romfs.bin", "--romfs-dir", romfs_path])
    subprocess.check_call([_3dstool, "-c", "-t", "cfa", "-f", out_path, "--header", header_path, "--romfs", "temp_romfs.bin"])
    os.remove("temp_romfs.bin")

def create(header_path, romfs_path, out_path, out_type):
    def inner():
        if out_type.get() == "CIA (.cia)":
            messagebox.showwarning("Cannot do CIA", "CIA not done yet")
        create_3dstool(header_path.get(), romfs_path.get(), out_path.get())
        messagebox.showinfo("Creating completed", "Done!")
    return inner

root = Tk()
root.title("dlc shit")

tabs = ttk.Notebook(root)
tab_x = ttk.Frame(tabs, padding=10)
tab_c = ttk.Frame(tabs, padding=10)
tabs.add(tab_x, text='Extract')
tabs.add(tab_c, text='Create')

tabs.pack(expand=1, fill="both")

ttk.Label(tab_x, text="Hello World!").grid(column=0, row=0)
ttk.Button(tab_x, text="Quit", command=root.destroy).grid(column=1, row=0)

ttk.Label(tab_c, text="Hello World!").grid(column=0, row=0)

ttk.Label(tab_c, text="Header (ncch.bin)").grid(column=0, row=1)
ncch_entry = ttk.Entry(tab_c)
ncch_entry.grid(column=1,row=1)
ttk.Button(tab_c, text="Browse", command=get_fname(ncch_entry)).grid(column=2, row=1)

ttk.Label(tab_c, text="RomFS folder").grid(column=0, row=2)
romfs_entry = ttk.Entry(tab_c)
romfs_entry.grid(column=1,row=2)
ttk.Button(tab_c, text="Browse", command=get_dname(romfs_entry)).grid(column=2, row=2)

ttk.Label(tab_c, text="Output file").grid(column=0, row=3)
out_entry = ttk.Entry(tab_c)
out_entry.grid(column=1,row=3)
ttk.Button(tab_c, text="Browse", command=get_fname_out(out_entry, initialfile="romfs")).grid(column=2, row=3)

ttk.Label(tab_c, text="Output type").grid(column=0, row=4)
out_type = ttk.Combobox(tab_c,values=["CIA (.cia)", "CFA/NCCH (.app)"])
out_type.set("CIA (.cia)")
out_type.grid(column=1,row=4)

ttk.Button(tab_c, text="Convert!", command=create(ncch_entry, romfs_entry, out_entry, out_type)).grid(column=2, row=5)

root.mainloop()