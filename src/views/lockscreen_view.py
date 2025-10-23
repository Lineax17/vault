from tkinter import ttk

class LockscreenView:
    MASTER_PASSWORD = "lorenz"

    def __init__(self, root, unlock_callback=None):
        self.toggle_btn = None
        self.password_entry = None
        self.check_btn = None
        self.unlock_callback = unlock_callback

        self.root = root
        self.root.title("Vault - Lockscreen")

        self.show_lockscreen(root)

    def show_lockscreen(self, root):
        """
        Display the lockscreen of the application.

        Args:
            root (Tk): The root Tkinter window.
        """
        ttk.Label(root, text="Password:").grid(row=0, column=0, padx=8, pady=8, sticky="w")
        self.password_entry = ttk.Entry(root, show="*")
        self.password_entry.grid(row=0, column=1, padx=8, pady=8)

        # Toggle Button
        self.toggle_btn = ttk.Button(root, text="👁️‍🗨️", width=3, command=self.toggle_password)
        self.toggle_btn.grid(row=0, column=2, padx=4)

        # Check Button
        self.check_btn = ttk.Button(root, text="CHECK", command=self.check_password)
        self.check_btn.grid(row=0, column=3, padx=4)

    def toggle_password(self):
        """Toggle password visibility."""
        if self.password_entry.cget("show") == "":
            self.password_entry.config(show="*")
            self.toggle_btn.config(text="👁️‍🗨️")
        else:
            self.password_entry.config(show="")
            self.toggle_btn.config(text="🙈")

    def check_password(self):
        """Check if the typed password is the MASTER_PASSWORD."""
        if self.password_entry.get() == self.MASTER_PASSWORD:
            if self.unlock_callback:
                self.unlock_callback(self)