import json
import os


class SettingsOps:
    def __init__(self, app):
        self.app = app
        self.settings_file = os.path.join(os.path.dirname(__file__), "..", "config", "settings.json")
        self.settings_file = os.path.abspath(self.settings_file)

    def save_settings(self, settings):
        os.makedirs(os.path.dirname(self.settings_file), exist_ok=True)
        with open(self.settings_file, "w") as f:
            json.dump(settings, f, indent=4)

    def load_settings(self):
        if os.path.exists(self.settings_file):
            with open(self.settings_file, "r") as f:
                return json.load(f)
        return {}
