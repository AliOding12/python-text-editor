import tkinter as tk
from utils.config import Config
from ui.app_window import MainWindow


def main():
    cfg = Config()
    cfg.load()

    root = tk.Tk()
    root.title("TkEdit")

    app = MainWindow(root, cfg)  # noqa: F841  (keep reference)

    def on_close():
        # persist window geometry + settings
        cfg.data["window_geometry"] = root.winfo_geometry()
        cfg.save()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)

    # restore geometry if present
    geom = cfg.data.get("window_geometry")
    if geom:
        root.geometry(geom)

    root.mainloop()


if __name__ == "__main__":
    main()
# Add main application entry point
# Integrate auto-save into main app
# Refactor main app for modularity
# Add error handling for startup
