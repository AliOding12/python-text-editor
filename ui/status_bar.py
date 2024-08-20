import tkinter as tk
from tkinter import ttk


class StatusBar(ttk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        self.cursor_label = ttk.Label(self, text="Line 1, Col 1")
        self.cursor_label.pack(side=tk.LEFT, padx=5)

        self.status_label = ttk.Label(self, text="Ready")
        self.status_label.pack(side=tk.RIGHT, padx=5)

        # Bind text widget events to update cursor position
        self.app.text.bind("<KeyRelease>", self.update_cursor_position)
        self.app.text.bind("<ButtonRelease-1>", self.update_cursor_position)

    def update_cursor_position(self, event=None):
        cursor_index = self.app.text.index(tk.INSERT)
        line, col = cursor_index.split(".")
        self.cursor_label.config(text=f"Line {line}, Col {int(col)+1}")

    def set_status(self, text):
        self.status_label.config(text=text)
# Add status bar component
# Add word count to status bar
# Add line and column indicators
