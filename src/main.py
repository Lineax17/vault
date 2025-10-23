from tkinter import Tk

from src.views.lockscreen_view import LockscreenView
from src.views.main_view import MainView

def on_unlock_success(lockscreen):
    """Called when the lockscreen is successfully unlocked."""
    # Destroy all lockscreen widgets
    for widget in lockscreen.root.winfo_children():
        widget.destroy()

    # Start the main view
    MainView(lockscreen.root)

if __name__ == '__main__':
    root = Tk()
    lockscreen = LockscreenView(root, unlock_callback=on_unlock_success)
    root.mainloop()