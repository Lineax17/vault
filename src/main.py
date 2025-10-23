from tkinter import Tk

from src.views.lockscreen_view import LockscreenView
from src.views.main_view import MainView

if __name__ == '__main__':
    root = Tk()
    LockscreenView(root)
    #MainView(root)
    root.mainloop()
