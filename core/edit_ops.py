import tkinter as tk


class EditOps:
    def __init__(self, app):
        self.app = app

    def cut_text(self):
        try:
            self.copy_text()
            self.app.text.delete("sel.first", "sel.last")
        except tk.TclError:
            pass  # No selection

    def copy_text(self):
        try:
            selected_text = self.app.text.get("sel.first", "sel.last")
            self.app.clipboard_clear()
            self.app.clipboard_append(selected_text)
        except tk.TclError:
            pass  # No selection

    def paste_text(self):
        try:
            cursor_pos = self.app.text.index(tk.INSERT)
            self.app.text.insert(cursor_pos, self.app.clipboard_get())
        except tk.TclError:
            pass  # Clipboard empty

    def undo_action(self):
        try:
            self.app.text.edit_undo()
        except tk.TclError:
            pass

    def redo_action(self):
        try:
            self.app.text.edit_redo()
        except tk.TclError:
            pass

    def select_all(self):
        self.app.text.tag_add("sel", "1.0", tk.END)
        return "break"

    def delete_selected(self):
        try:
            self.app.text.delete("sel.first", "sel.last")
        except tk.TclError:
            pass
