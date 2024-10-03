import uvicorn

if __name__ == "__main__":
    # start the uvicorn server with the desired host and port
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
