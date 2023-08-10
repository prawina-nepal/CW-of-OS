import tkinter as tk
from tkinter import filedialog, messagebox
import unittest
import os

class File:
    def __init__(self, name, content=""):
        self.name = name
        self.content = content

class Directory:
    def __init__(self, name):
        self.name = name
        self.files = {}
        self.subdirectories = {}

class FileSystem:
    def __init__(self):
        self.root = Directory("/")
        self.current_directory = self.root

    def create_file(self, name, content=""):
        if name in self.current_directory.files:
            return "File already exists"
        new_file = File(name, content)
        self.current_directory.files[name] = new_file

    def read_file(self, name):
        if name in self.current_directory.files:
            return self.current_directory.files[name].content
        return "File not found"

    def write_file(self, name, content):
        if name in self.current_directory.files:
            self.current_directory.files[name].content = content
        else:
            self.create_file(name, content)

    def create_directory(self, name):
        if name in self.current_directory.subdirectories:
            return "Directory already exists"
        new_directory = Directory(name)
        self.current_directory.subdirectories[name] = new_directory

    def change_directory(self, name):
        if name in self.current_directory.subdirectories:
            self.current_directory = self.current_directory.subdirectories[name]
        else:
            return "Directory not found"

    def list_directory(self):
        return list(self.current_directory.subdirectories.keys()), list(self.current_directory.files.keys())

class FileSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("File System GUI")

        self.file_system = FileSystem()

        self.file_frame = tk.Frame(root)
        self.file_frame.pack(padx=10, pady=10)

        self.current_directory_label = tk.Label(self.file_frame, text="Current Directory:")
        self.current_directory_label.pack()

        self.current_directory_text = tk.Label(self.file_frame, text=self.file_system.current_directory.name)
        self.current_directory_text.pack()

        self.choose_file_button = tk.Button(self.file_frame, text="Choose File", command=self.choose_file)
        self.choose_file_button.pack()

        self.create_file_entry = tk.Entry(self.file_frame)
        self.create_file_entry.pack()

        self.file_content_entry = tk.Entry(self.file_frame)
        self.file_content_entry.pack()

        self.create_file_button = tk.Button(self.file_frame, text="Create File", command=self.create_file)
        self.create_file_button.pack()

        self.file_content_button = tk.Button(self.file_frame, text="Write File", command=self.write_file)
        self.file_content_button.pack()

        self.create_directory_entry = tk.Entry(root)
        self.create_directory_button = tk.Button(root, text="Create Directory", command=self.create_directory)
        self.create_directory_entry.pack()
        self.create_directory_button.pack()

        self.change_directory_entry = tk.Entry(root)
        self.change_directory_button = tk.Button(root, text="Change Directory", command=self.change_directory)
        self.change_directory_entry.pack()
        self.change_directory_button.pack()

        self.list_directory_button = tk.Button(root, text="List Directory", command=self.list_directory)
        self.list_directory_button.pack()

        self.text_area = tk.Text(root, height=10, width=40)
        self.text_area.pack()

    def choose_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.create_file_entry.delete(0, tk.END)
            self.create_file_entry.insert(0, file_path)

    def create_file(self):
        file_path = self.create_file_entry.get()
        file_name = file_path.split("/")[-1]
        result = self.file_system.create_file(file_name)
        messagebox.showinfo("Result", result)
        self.create_file_entry.delete(0, tk.END)

    def write_file(self):
        file_name = self.create_file_entry.get()
        content = self.file_content_entry.get()
        self.file_system.write_file(file_name, content)
        self.create_file_entry.delete(0, tk.END)
        self.file_content_entry.delete(0, tk.END)

    def create_directory(self):
        dir_name = self.create_directory_entry.get()
        result = self.file_system.create_directory(dir_name)
        messagebox.showinfo("Result", result)

    def change_directory(self):
        dir_name = self.change_directory_entry.get()
        result = self.file_system.change_directory(dir_name)
        if "Directory not found" in result:
            messagebox.showerror("Error", result)
        else:
            self.current_directory_text.config(text=self.file_system.current_directory.name)
            self.text_area.delete(1.0, tk.END)

    def list_directory(self):
        subdirs, files = self.file_system.list_directory()
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, "Subdirectories:\n")
        for subdir in subdirs:
            self.text_area.insert(tk.END, subdir + "\n")
        self.text_area.insert(tk.END, "\nFiles:\n")
        for file in files:
            self.text_area.insert(tk.END, file + "\n")

root = tk.Tk()
app = FileSystemGUI(root)
root.mainloop()
