import tkinter as tk
from tkinter import ttk
from ui.menu_bar import MenuBar
from ui.toolbar import ToolBar
from ui.status_bar import StatusBar
from core.linenumber import LineNumberCanvas


class MainWindow:
    def __init__(self, root, config):
        self.root = root
        self.config = config

        # Main container
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Toolbar
        self.toolbar = ToolBar(self.main_frame, self)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        # Text area + scrollbar + line numbers
        self.text_frame = ttk.Frame(self.main_frame)
        self.text_frame.pack(fill=tk.BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.text_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.text = tk.Text(
            self.text_frame,
            wrap="word",
            undo=True,
            font=(self.config.data.get("font_family", "Consolas"),
                  self.config.data.get("font_size", 12))
        )
        self.text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text.yview)

        # Line numbers
        self.line_numbers = LineNumberCanvas(self.text_frame, self.text)
        self.line_numbers.pack(side=tk.LEFT, fill=tk.Y)

        # Status bar
        self.status_bar = StatusBar(self.main_frame, self)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Menu bar
        self.menu_bar = MenuBar(self.root, self)
        self.root.config(menu=self.menu_bar)

        # Bind events
        self.text.bind("<KeyRelease>", self.on_text_change)
        self.text.bind("<ButtonRelease-1>", self.on_text_change)

    def on_text_change(self, event=None):
        self.line_numbers.update()
        self.status_bar.update_status()
