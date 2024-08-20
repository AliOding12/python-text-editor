import json
import os


class Config:
    """
    Simple JSON-backed app config.
    Default location: <project_root>/config/settings.json
    """

    DEFAULTS = {
        "font_family": "Arial",
        "font_size": 12,
        "theme": "Light",
        "window_size": "800x600",
    }

    def __init__(self, path: str | None = None):
        if path is None:
            # utils/ -> project root -> config/settings.json
            root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
            self.path = os.path.join(root, "config", "settings.json")
        else:
            self.path = os.path.abspath(path)

        self.data: dict = dict(self.DEFAULTS)

    def load(self) -> None:
        """Load config from disk; fall back to defaults if missing/broken."""
        try:
            if os.path.exists(self.path):
                with open(self.path, "r", encoding="utf-8") as f:
                    loaded = json.load(f)
                if isinstance(loaded, dict):
                    self.data.update(loaded)
        except Exception:
            # keep defaults on any error
            pass

    def save(self) -> None:
        """Persist current config to disk (creates folder if needed)."""
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2)

    def get(self, key: str, default=None):
        return self.data.get(key, default)

    def set(self, key: str, value) -> None:
        self.data[key] = value
# Add settings load/save functionality
# Fix bug in settings loading
# Add support for user-defined shortcuts
