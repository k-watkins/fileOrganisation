import os
import shutil
import tkinter as tk

source_folder = "\\Users\\d891410\\Documents\\Extracts\\DevineHomesMI\\"
target_folder = '\\Users\\d891410\\Documents\\test\\'
src_directory = os.listdir(source_folder)
file_types = [(".jpg", ".png", ".jpeg", ".bmp"),
              (".doc", ".docx", ".txt", ".xls", ".csv"),
              (".mp3", ".acc", ".wma"),
              (".mp4", ".wmv", ".avi", ".mkv")]


def copy_files():
    for files in src_directory:
        source = source_folder + files
        target = target_folder + files
        for i, x in enumerate(file_types):
            if files.endswith(file_types[i]):
                shutil.copy2(source, target)
                print(f"{files} Copied!")


def move_files():
    for files in src_directory:
        source = source_folder + files
        target = target_folder + files
        for i, x in enumerate(file_types):
            if files.endswith(file_types[i]):
                shutil.move(source, target)
                print(f"{files} Moved!")


def delete_files():
    for files in src_directory:
        target = target_folder + files
        for i, x in enumerate(file_types):
            if files.endswith(file_types[i]):
                os.remove(target)
                print(f"{files} Removed!")


def generate_main_window():
    window = tk.Tk()
    greeting = tk.Label(text="Hello")
    greeting.pack()
    button = tk.Button(text="Click ME", command=window.destroy)
    copy = tk.Button(text="Copy", command=copy_files)
    move = tk.Button(text="Move", command=move_files)
    delete = tk.Button(text="Delete", command=delete_files)
    copy.pack()
    move.pack()
    delete.pack()
    button.pack()
    window.geometry("250x250")
    window.mainloop()





