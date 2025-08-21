import tkinter as tk

class LineNumberCanvas(tk.Canvas):
    def __init__(self, parent, text_widget, **kwargs):
        super().__init__(parent, width=40, bg="#f0f0f0", highlightthickness=0, **kwargs)
        self.text_widget = text_widget
        self.text_widget.bind("<KeyRelease>", self.update)
        self.text_widget.bind("<MouseWheel>", self.update)
        self.text_widget.bind("<ButtonRelease-1>", self.update)
        self.update()

    def update(self, event=None):
        self.delete("all")
        i = self.text_widget.index("@0,0")
        while True:
            dline = self.text_widget.dlineinfo(i)
            if dline is None:
                break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2, y, anchor="nw", text=linenum, font=self.text_widget['font'], fill="#888")
            i = self.text_widget.index(f"{i}+1line")