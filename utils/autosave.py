import os
import time
import threading


class AutoSave:
    """
    Automatically saves the current text at intervals.
    """

    def __init__(self, app, interval: int = 60):
        """
        :param app: The main Tkinter app instance.
        :param interval: Interval in seconds for auto-saving.
        """
        self.app = app
        self.interval = interval
        self.running = False
        self.thread = None
        self.last_content = ""

    def start(self):
        """Start the auto-save background thread."""
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._run, daemon=True)
            self.thread.start()

    def stop(self):
        """Stop auto-save."""
        self.running = False
        if self.thread:
            self.thread.join(timeout=1)

    def _run(self):
        """Background loop that checks for changes and saves."""
        while self.running:
            time.sleep(self.interval)
            try:
                content = self.app.text.get("1.0", "end-1c")
                if content != self.last_content:
                    self._save_temp_file(content)
                    self.last_content = content
            except Exception:
                pass  # ignore any errors silently

    def _save_temp_file(self, content: str):
        """Save current content to a temp file."""
        temp_dir = os.path.join(os.path.dirname(__file__), "..", "temp")
        os.makedirs(temp_dir, exist_ok=True)
        temp_path = os.path.join(temp_dir, "autosave.txt")
        with open(temp_path, "w", encoding="utf-8") as f:
            f.write(content)
