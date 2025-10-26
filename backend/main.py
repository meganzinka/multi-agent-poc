from dotenv import load_dotenv
from adk.adk import ADK

# Load environment variables from .env file
load_dotenv()

# Initialize the Agent Development Kit
adk = ADK()

# Define your agents here
# Example:
#
# from adk.agent import Agent
#
# class MyAgent(Agent):
#     def __init__(self):
#         super().__init__()
#
#     def main(self, input_data):
#         # Agent logic goes here
#         return "Hello from MyAgent!"
#
# adk.register_agent(MyAgent, "my_agent")

if __name__ == "__main__":
    adk.run()
