import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
from core.file_ops import FileOps
from core.edit_ops import EditOps
from core.theme import ThemeOps
from core.search_ops import SearchOps


class MenuBar(tk.Menu):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.parent = parent
        self.app = app

        # File menu
        file_menu = tk.Menu(self, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open...", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As...", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.parent.quit)
        self.add_cascade(label="File", menu=file_menu)

        # Edit menu
        edit_menu = tk.Menu(self, tearoff=0)
        edit_menu.add_command(label="Undo", command=self.app.text.edit_undo)
        edit_menu.add_command(label="Redo", command=self.app.text.edit_redo)
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", command=lambda: self.app.text.event_generate("<<Cut>>"))
        edit_menu.add_command(label="Copy", command=lambda: self.app.text.event_generate("<<Copy>>"))
        edit_menu.add_command(label="Paste", command=lambda: self.app.text.event_generate("<<Paste>>"))
        edit_menu.add_separator()
        edit_menu.add_command(label="Find / Replace", command=self.open_search)
        self.add_cascade(label="Edit", menu=edit_menu)

        # View menu
        view_menu = tk.Menu(self, tearoff=0)
        view_menu.add_command(label="Change Theme", command=self.change_theme)
        self.add_cascade(label="View", menu=view_menu)

        # Help menu
        help_menu = tk.Menu(self, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        self.add_cascade(label="Help", menu=help_menu)

        # Helpers
        self.file_ops = FileOps(self.app)
        self.edit_ops = EditOps(self.app)
        self.theme_manager = ThemeOps(self.app)

    # File menu actions
    def new_file(self):
        self.file_ops.new_file()

    def open_file(self):
        self.file_ops.open_file()

    def save_file(self):
        self.file_ops.save_file()

    def save_file_as(self):
        self.file_ops.save_file_as()

    # Edit menu actions
    def open_search(self):
        SearchOps(self.app)

    # View menu actions
    def change_theme(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.theme_manager.apply_theme({"background": color, "foreground": "#000000"})

    # Help menu actions
    def show_about(self):
        messagebox.showinfo("About", "TkEdit - A Modern Tkinter Text Editor\nBuilt with Python.")
