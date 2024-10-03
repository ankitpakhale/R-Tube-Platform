class AIAgentBase:
    def __init__(self):
        # Common setup for all AI agents can go here
        pass

    async def generate_response(self, prompt):
        raise NotImplementedError("This method should be overridden.")
