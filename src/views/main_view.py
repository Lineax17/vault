from tkinter import *
from tkinter import ttk

class MainView:
    def __init__(self, root):
        self.root = root
        self.root.title("Vault - Password Manager")
        self.root.geometry("550x800")

        # New Entry Section
        self.label = Label(self.root, text="New Entry")
        self.label.pack(pady=20)

        self.label = Label(self.root, text="Username:")
        self.label.pack(pady=10)

        self.username = Entry(self.root)
        self.username.pack(pady=10)

        self.label = Label(self.root, text="Password:")
        self.label.pack(pady=10)

        self.password = Entry(self.root)
        self.password.pack(pady=10)

        self.button = Button(self.root, text="Save", command=self.on_button_click)
        self.button.pack(pady=10)

        # Existing Entries Section
        self.label = Label(self.root, text="Existing Entries")
        self.label.pack(pady=20)

    def on_button_click(self):
        print(Entry.get(self.username))
        print(Entry.get(self.password))