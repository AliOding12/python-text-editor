import tkinter as tk
from tkinter import simpledialog, messagebox


class SearchOps:
    def __init__(self, app):
        self.app = app

    def find_text(self):
        query = simpledialog.askstring("Find", "Enter text to find:")
        if query:
            self.app.text.tag_remove("highlight", "1.0", tk.END)
            start_pos = "1.0"
            matches = 0
            while True:
                start_pos = self.app.text.search(query, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f"{start_pos}+{len(query)}c"
                self.app.text.tag_add("highlight", start_pos, end_pos)
                self.app.text.tag_config("highlight", background="yellow", foreground="black")
                start_pos = end_pos
                matches += 1
            if matches == 0:
                messagebox.showinfo("Find", "No matches found.")

    def replace_text(self):
        query = simpledialog.askstring("Replace", "Find:")
        if not query:
            return
        replacement = simpledialog.askstring("Replace", "Replace with:")
        if replacement is None:
            return

        content = self.app.text.get("1.0", tk.END)
        new_content = content.replace(query, replacement)
        self.app.text.delete("1.0", tk.END)
        self.app.text.insert("1.0", new_content)
        messagebox.showinfo("Replace", f"All occurrences of '{query}' replaced.")
