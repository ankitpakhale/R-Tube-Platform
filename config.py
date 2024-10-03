import os
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

class Config:
    """Handles application configuration."""
    
    def __init__(self):
        self.app_name: str = os.getenv("APP_NAME", "R-TUBE")
        self.debug: bool = os.getenv("DEBUG", "False").lower() == "true"
        self.database_url: str = os.getenv("DATABASE_URL", "sqlite:///r_tube.db")
    
    def __repr__(self) -> str:
        return f"Config(app_name={self.app_name}, debug={self.debug})"

# Initialize configuration
config = Config()
