from readline import get_current_history_length
from tkinter import *
from tkinter import ttk
import json


class MainView:
    def __init__(self, root):
        self.root = root
        self.root.title("Vault - Password Manager")
        self.root.geometry("350x600")

        self.setup_new_entry_section()
        self.setup_existing_entries_section()

    def setup_new_entry_section(self):
        """ Setting up the section of main view for new entries """
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

        self.button = Button(self.root, text="Save", command=self.on_save_button_click)
        self.button.pack(pady=10)

    def setup_existing_entries_section(self):
        """ Setting up the section of main view for existing entries """
        self.label = Label(self.root, text="Existing Entries")
        self.label.pack(pady=20)

        data = self.read_passwords()

        for entry in data["entries"]:
            entry_text = f"Name: {entry['name']}"
            entry_id = entry['id']
            self.label = Label(self.root, text=entry_text)
            self.label.pack(pady=5)
            self.button = Button(self.root, text="Show", command=lambda id=entry_id: self.on_show_button_click(id))
            self.button.pack(pady=10)

    def on_show_button_click(self, entry_id):
        """
        Show username and password for the given entry id

        Args:
            entry_id (int): The id of the entry to show
        """
        data = self.read_passwords()

        entry = None
        for e in data['entries']:
            if e['id'] == entry_id:
                entry = e
                break

        if entry:
            print(f"Username: {entry['username']}, Password: {entry['password']}")
        else:
            print("Eintrag nicht gefunden")

    def on_save_button_click(self):
        """ Save new entry to passwords.json """

        entry = {
            "id": self.read_passwords()["next_id"],
            "name": Entry.get(self.name),
            "username": Entry.get(self.username),
            "password": Entry.get(self.password)
        }

        self.write_entry(entry)

    def read_passwords(self):
        """
            Read passwords from passwords.json

            Returns:
                dict: The data from passwords.json
        """
        try:
            with open('src/passwords.json', 'r') as file:
                data = json.load(file)
                return data
        except (FileNotFoundError, json.JSONDecodeError):
            data = {
                "entries": [],
                "next_id": 1
            }
            with open('src/passwords.json', 'w') as file:
                json.dump(data, file, indent=4)
            return data

    def write_entry(self, entry):
        """
        Write a new entry to passwords.json

        Args:
            entry (dict): The entry to write
        """
        data = self.read_passwords()
        data["entries"].append(entry)
        data["next_id"] += 1

        with open('src/passwords.json', 'w') as file:
            json.dump(data, file)
