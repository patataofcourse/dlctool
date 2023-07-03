import os
import subprocess

_3dstool = "./3dstool" if os.path.isfile("3dstool") and os.name == "posix" else "3dstool"

def extract_3dstool(header_path, romfs_path, in_path):
    #TODO: get proper temp path
    subprocess.check_call([_3dstool, "-x", "-t", "cfa", "-f", in_path, "--header", header_path, "--romfs", "temp_romfs.bin"])
    subprocess.check_call([_3dstool, "-x", "-t", "romfs", "-f", "temp_romfs.bin", "--romfs-dir", romfs_path])
    os.remove("temp_romfs.bin")

def create_3dstool(header_path, romfs_path, out_path):
    #TODO: get proper temp path
    subprocess.check_call([_3dstool, "-c", "-t", "romfs", "-f", "temp_romfs.bin", "--romfs-dir", romfs_path])
    subprocess.check_call([_3dstool, "-c", "-t", "cfa", "-f", out_path, "--header", header_path, "--romfs", "temp_romfs.bin"])
    os.remove("temp_romfs.bin")
