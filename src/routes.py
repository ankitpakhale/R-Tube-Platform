from fastapi import FastAPI

def setup_routes(app: FastAPI):
    """Set up routes for the FastAPI application."""

    @app.get("/")
    def index():
        # simple test route
        return {"message": "Welcome to the R-TUBE Platform!"}

    # TODO: Add more routes for user actions like registration, login, etc.
