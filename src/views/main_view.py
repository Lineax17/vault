from tkinter import *
from tkinter import ttk

class MainView:
    def __init__(self, root):
        self.root = root
        self.root.title("Main View")
        self.root.geometry("400x300")

        self.label = Label(self.root, text="Welcome to the Main View")
        self.label.pack(pady=20)

        self.button = Button(self.root, text="Click Me", command=self.on_button_click)
        self.button.pack(pady=10)

    def on_button_click(self):
        print("Button clicked!")