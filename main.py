from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from ai_agents.blog_generator_agent import BlogGeneratorAgent

app = FastAPI()

agent = BlogGeneratorAgent()

class UserInput(BaseModel):
    user_input: str

@app.post("/ai-agent")
async def ai_agent(user_input: UserInput):
    """Handle user input and return AI response."""
    try:
        response = agent.generate_response(user_input.user_input)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def read_root():
    """Welcome message for R-TUBE Platform."""
    return {"message": "Welcome to R-TUBE Platform"}
