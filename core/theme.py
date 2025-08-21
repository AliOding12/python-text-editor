class ThemeOps:
    def __init__(self, app):
        self.app = app
        self.themes = {
            "Light": {"bg": "white", "fg": "black"},
            "Dark": {"bg": "#2E2E2E", "fg": "white"},
            "Solarized": {"bg": "#FDF6E3", "fg": "#657B83"},
            "Monokai": {"bg": "#272822", "fg": "#F8F8F2"},
        }

    def apply_theme(self, theme_name):
        if theme_name in self.themes:
            colors = self.themes[theme_name]
            self.app.text.config(bg=colors["bg"], fg=colors["fg"])
