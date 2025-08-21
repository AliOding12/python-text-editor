import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from core.file_ops import FileOps
from core.search_ops import SearchOps


class ToolBar(ttk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self.file_ops = FileOps(self.app)

        # New file button
        new_btn = ttk.Button(self, text="New", command=self.file_ops.new_file)
        new_btn.pack(side=tk.LEFT, padx=2, pady=2)

        # Open file button
        open_btn = ttk.Button(self, text="Open", command=self.file_ops.open_file)
        open_btn.pack(side=tk.LEFT, padx=2, pady=2)

        # Save file button
        save_btn = ttk.Button(self, text="Save", command=self.file_ops.save_file)
        save_btn.pack(side=tk.LEFT, padx=2, pady=2)

        # Find button
        find_btn = ttk.Button(self, text="Find", command=lambda: SearchOps(self.app))
        find_btn.pack(side=tk.LEFT, padx=2, pady=2)

        # Font size control
        ttk.Label(self, text="Font Size:").pack(side=tk.LEFT, padx=(10, 2))
        self.font_size_var = tk.IntVar(value=self.app.config.data.get("font_size", 12))
        font_size_spin = ttk.Spinbox(
            self,
            from_=8, to=48,
            textvariable=self.font_size_var,
            width=4,
            command=self.update_font_size
        )
        font_size_spin.pack(side=tk.LEFT, padx=2, pady=2)

    def update_font_size(self):
        new_size = self.font_size_var.get()
        current_font = (self.app.config.data.get("font_family", "Consolas"), new_size)
        self.app.text.config(font=current_font)
        self.app.config.data["font_size"] = new_size
