from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from .ai_agent_base import AIAgentBase

class BlogGeneratorAgent(AIAgentBase):
    """Blog Generator AI Agent."""

    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
        self.model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-small")

    def generate_response(self, user_input: str) -> str:
        # encode the input
        new_user_input_ids = self.tokenizer.encode(user_input + self.tokenizer.eos_token, return_tensors='pt')

        # append the new input to the chat history
        bot_input_ids = new_user_input_ids

        # generate a response from the model
        chat_history_ids = self.model.generate(bot_input_ids, max_length=1000, pad_token_id=self.tokenizer.eos_token_id)

        # get the response text
        response = self.tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
        return response
