from config import config

class App:
    """Represents the backend application."""
    
    def __init__(self):
        self.config = config
    
    def __repr__(self) -> str:
        return f"App(config={self.config})"

def create_app() -> App:
    """Factory function to create an instance of the app."""
    return App()
