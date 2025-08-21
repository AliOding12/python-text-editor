import tkinter as tk
from tkinter import font, colorchooser


class FormatOps:
    def __init__(self, app):
        self.app = app
        self.current_font_family = "Arial"
        self.current_font_size = 12

    def choose_font(self):
        # Simple font chooser
        fonts = list(font.families())
        fonts.sort()
        top = tk.Toplevel(self.app.root)
        top.title("Choose Font")
        top.geometry("250x300")

        font_listbox = tk.Listbox(top)
        for f in fonts:
            font_listbox.insert(tk.END, f)
        font_listbox.pack(fill=tk.BOTH, expand=True)

        def apply_font():
            selected_font = font_listbox.get(tk.ACTIVE)
            self.current_font_family = selected_font
            self.update_font()
            top.destroy()

        tk.Button(top, text="Apply", command=apply_font).pack(pady=5)

    def choose_font_size(self):
        size_win = tk.Toplevel(self.app.root)
        size_win.title("Font Size")

        tk.Label(size_win, text="Enter size:").pack(pady=5)
        size_var = tk.StringVar(value=str(self.current_font_size))
        size_entry = tk.Entry(size_win, textvariable=size_var)
        size_entry.pack()

        def apply_size():
            try:
                size = int(size_var.get())
                self.current_font_size = size
                self.update_font()
                size_win.destroy()
            except ValueError:
                pass

        tk.Button(size_win, text="Apply", command=apply_size).pack(pady=5)

    def choose_text_color(self):
        color = colorchooser.askcolor(title="Choose Text Color")
        if color[1]:
            self.app.text.config(fg=color[1])

    def choose_bg_color(self):
        color = colorchooser.askcolor(title="Choose Background Color")
        if color[1]:
            self.app.text.config(bg=color[1])

    def update_font(self):
        new_font = font.Font(family=self.current_font_family, size=self.current_font_size)
        self.app.text.config(font=new_font)
