import uvicorn
import asyncio
from fastapi import FastAPI

app = FastAPI()

# Database initialization logic
@app.on_event("startup")
async def startup_event():
    print("Database initialized.")

# Sample route
@app.get("/")
async def read_root():
    return {"message": "Welcome to R-TUBE Platform"}

def start():
    # Check if the event loop is running
    if asyncio.get_event_loop().is_running():
        config = uvicorn.Config(app, host="0.0.0.0", port=8080, reload=True)
        server = uvicorn.Server(config)
        asyncio.create_task(server.serve())  # create a new task in the running event loop
    else:
        uvicorn.run(app, host="0.0.0.0", port=8080, reload=True)

if __name__ == "__main__":
    start()
