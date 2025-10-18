from readline import get_current_history_length
from tkinter import *
from tkinter import ttk
import json

class MainView:
    def __init__(self, root):
        self.root = root
        self.root.title("Vault - Password Manager")
        self.root.geometry("550x800")

        # New Entry Section
        self.label = Label(self.root, text="New Entry")
        self.label.pack(pady=20)

        self.label = Label(self.root, text="Name:")
        self.label.pack(pady=10)

        self.name = Entry(self.root)
        self.name.pack(pady=10)

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
        print(Entry.get(self.name))
        print(Entry.get(self.username))
        print(Entry.get(self.password))

        data = {
            "name": Entry.get(self.name),
            "username": Entry.get(self.username),
            "password": Entry.get(self.password)
        }

        self.write_entry(data)

    def read_entry(self, id_number):
        with open('src/passwords.json', 'r') as file:
            data = json.load(file)
            return data

    def write_entry(self, entry):
        try:
            with open('src/passwords.json', 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {
                "entries": []
            }
        data["entries"].append(entry)

        with open('src/passwords.json', 'w') as file:
            json.dump(data, file)