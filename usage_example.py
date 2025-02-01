[example]
Find an example usage of the given project files and create a concise, runnable code sample demonstrating its functionality.

# Import necessary modules from the project
import asyncio
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from browser_use import Agent, AgentHistoryList

# Load environment variables from .env file
load_dotenv()

# Create an agent instance with a specific task
async def main():
    agent = Agent(
        task="Navigate to Reddit, search for 'Pytest', and return the first comment in the first post.",
        llm=ChatOpenAI(model="gpt-4o")
    )

    # Run the agent and get the result
    history: AgentHistoryList = await agent.run()
    result = history.final_result()

    # Print the result
    print("First comment on the post:", result)

# Execute the main function
asyncio.run(main())
