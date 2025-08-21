import tkinter as tk
from tkinter import filedialog, messagebox
import os


class FileOps:
    def __init__(self, app):
        self.app = app
        self.file_path = None

    def new_file(self):
        if self.confirm_unsaved_changes():
            self.app.text.delete(1.0, tk.END)
            self.file_path = None
            self.app.status_bar.set_status("New file created")

    def open_file(self):
        if not self.confirm_unsaved_changes():
            return
        file_path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                self.app.text.delete(1.0, tk.END)
                self.app.text.insert(tk.END, content)
                self.file_path = file_path
                self.app.status_bar.set_status(f"Opened: {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file: {e}")

    def save_file(self):
        if self.file_path:
            try:
                with open(self.file_path, "w", encoding="utf-8") as file:
                    file.write(self.app.text.get(1.0, tk.END).rstrip())
                self.app.status_bar.set_status(f"Saved: {os.path.basename(self.file_path)}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {e}")
        else:
            self.save_file_as()

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(self.app.text.get(1.0, tk.END).rstrip())
                self.file_path = file_path
                self.app.status_bar.set_status(f"Saved As: {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {e}")

    def confirm_unsaved_changes(self):
        # Basic check for changes
        if self.app.text.edit_modified():
            choice = messagebox.askyesnocancel("Unsaved Changes", "Save changes before proceeding?")
            if choice:  # Yes
                self.save_file()
                return True
            elif choice is None:  # Cancel
                return False
            else:  # No
                return True
        return True
