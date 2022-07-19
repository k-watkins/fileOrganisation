import os
import shutil
import tkinter as tk
from tkinter import *


source_folder = "\\Users\\d891410\\Documents\\Extracts\\DevineHomesMI\\"
target_folder = '\\Users\\d891410\\Documents\\test\\'
src_directory = os.listdir(source_folder)
file_types = [(".jpg", ".png", ".jpeg", ".bmp"),
              (".doc", ".docx", ".txt", ".xls", ".csv", ".xlsx"),
              (".mp3", ".acc", ".wma"),
              (".mp4", ".wmv", ".avi", ".mkv")]
file_list = []


def copy_files():
    if len(os.listdir(source_folder)) == 0:
        print("No files to copy!")
    else:
        for files in src_directory:
            source = source_folder + files
            target = target_folder + files
            for i, x in enumerate(file_types):
                if files.endswith(file_types[i]):
                    shutil.copy2(source, target)
                    file_list.append(str(files))
                    print(f"{file_list} Copied!")


def move_files():
    if len(os.listdir(source_folder)) == 0:
        print("No files to move!")
    else:
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


def show_file_names():
    for files in src_directory:
        print(f"{files}")


def generate_main_window():
    window = tk.Tk()
    listbox = Listbox(window)
    listbox.config(width=20)
    frame = Frame(window)

    def show_file_window():
        listbox.pack(padx=5, pady=5, fill=BOTH, expand=True)
        if len(os.listdir(source_folder)) == 0:
            listbox.insert(0, "No files to list!")
        else:
            show_file_names()
        listbox.pack()

    def delete_window():
        if len(os.listdir(source_folder)) == 0:
            listbox.insert(0, "No files to delete!")
        else:
            delete_files()
            label = Label(window, text=f"{file_list} deleted!", font=('Calibri 15'))
            label.pack()

    def copy_window():
        if len(os.listdir(source_folder)) == 0:
            listbox.insert(0, "No files to copy!")
        else:
            copy_files()
            label = Label(window, text=f"{file_list} copied!", font=('Calibri 15'))
            label.pack()
        listbox.pack(padx=5, pady=5, expand=True)

    def move_window():
        if len(os.listdir(source_folder)) == 0:
            listbox.insert(0, "No files to move!")
        else:
            move_files()
        listbox.pack()
    frame.pack()
    button = tk.Button(frame, text="Click ME", command=window.destroy)
    copy = tk.Button(frame, text="Copy", command=copy_window)
    move = tk.Button(frame, text="Move", command=move_window)
    delete = tk.Button(frame, text="Delete", command=delete_window)
    show = tk.Button(frame, text="Show Files", command=show_file_window)
    show.pack(side=RIGHT)
    copy.pack(side=RIGHT)
    move.pack(side=RIGHT)
    delete.pack(side=RIGHT)
    button.pack(side=LEFT)
    window.wm_title("File Manager")
    window.geometry("400x400")
    window.mainloop()
