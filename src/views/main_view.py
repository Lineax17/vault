from readline import get_current_history_length
from tkinter import *
from tkinter import ttk
import json


class MainView:
    def __init__(self, root):
        self.root = root
        self.root.title("Vault - Password Manager")
        #self.root.geometry("350x600")

        self.setup_new_entry_section()
        self.setup_existing_entries_section()

    def setup_new_entry_section(self):
        """ Setting up the section of main view for new entries """

        self.label = Label(self.root, text="New Entry", font=("Arial", 16, "bold"))
        self.label.pack(pady=10)

        new_entry_section = ttk.Frame(self.root)
        new_entry_section.pack(pady=10)

        self.label = Label(new_entry_section, text="Name:")
        self.label.grid(row=0, column=0, padx=8, pady=8, sticky="w")

        self.name = Entry(new_entry_section)
        self.name.grid(row=0, column=1, padx=8, pady=8, sticky="w")

        self.label = Label(new_entry_section, text="Username:")
        self.label.grid(row=1, column=0, padx=8, pady=8, sticky="w")

        self.username = Entry(new_entry_section)
        self.username.grid(row=1, column=1, padx=8, pady=8, sticky="w")

        self.label = Label(new_entry_section, text="Password:")
        self.label.grid(row=2, column=0, padx=8, pady=8, sticky="w")

        self.password = Entry(new_entry_section)
        self.password.grid(row=2, column=1, padx=8, pady=8, sticky="w")

        self.button = Button(new_entry_section, text="Save", command=self.on_save_button_click)
        self.button.grid(row=3, column=0, padx=8, pady=8, sticky="w")

    def setup_existing_entries_section(self):
        """ Setting up the section of main view for existing entries """
        self.label = Label(self.root, text="Existing Entries", font=("Arial", 16, "bold"))
        self.label.pack(pady=20)

        data = self.read_passwords()

        entries_frame = Frame(self.root)
        entries_frame.pack(pady=10)

        for index, entry in enumerate(data["entries"]):
            entry_id = entry['id']

            # Name Label
            name_label = Label(entries_frame, text=entry['name'])
            name_label.grid(row=index, column=0, padx=4, pady=4)

            # Password Entry (hidden)
            password_entry = Entry(entries_frame, width=15, show="*")
            password_entry.insert(0, entry['password'])
            password_entry.config(state='readonly')  # Read-only
            password_entry.grid(row=index, column=1, padx=4, pady=4)

            # Toggle Button (Show/Hide)
            toggle_btn = Button(
                entries_frame,
                text="👁",
                width=3,
                command=lambda e=password_entry: self.toggle_password(e)
            )
            toggle_btn.grid(row=index, column=2, padx=2, pady=4)

            # Copy Button
            copy_btn = Button(
                entries_frame,
                text="📋",
                width=3,
                command=lambda pwd=entry['password']: self.copy_to_clipboard(pwd)
            )
            copy_btn.grid(row=index, column=3, padx=2, pady=4)

            # Delete Button
            delete_btn = Button(
                entries_frame,
                text="🗑",
                width=3,
                command=lambda id=entry_id: self.delete_entry(id)
            )
            delete_btn.grid(row=index, column=4, padx=2, pady=4)

    def toggle_password(self, entry_widget):
        """ Show/hide password """
        if entry_widget.cget('show') == '*':
            entry_widget.config(show='')
        else:
            entry_widget.config(show='*')

    def copy_to_clipboard(self, text):
        """ Copy text to clipboard """
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        self.root.update()

    def delete_entry(self, entry_id):
        """ Deletes an entry from passwords.json """
        data = self.read_passwords()
        data["entries"] = [entry for entry in data["entries"] if entry['id'] != entry_id]

        with open('src/passwords.json', 'w') as file:
            json.dump(data, file, indent=4)

        # Reload view
        self.refresh_view()

    def refresh_view(self):
        """ Destroys all widgets and rebuilds the view """
        for widget in self.root.winfo_children():
            widget.destroy()

        self.setup_new_entry_section()
        self.setup_existing_entries_section()

    def on_save_button_click(self):
        """ Save new entry to passwords.json """

        entry = {
            "id": self.read_passwords()["next_id"],
            "name": Entry.get(self.name),
            "username": Entry.get(self.username),
            "password": Entry.get(self.password)
        }

        self.write_entry(entry)
        self.refresh_view()

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
