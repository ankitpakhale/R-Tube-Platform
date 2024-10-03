#!/bin/bash

# print message
echo "Starting R-TUBE backend..."

# activate virtual environment
source .venv/bin/activate

# start the FastAPI server using Uvicorn
uvicorn main:start --reload
