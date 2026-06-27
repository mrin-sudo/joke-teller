import asyncio
from dotenv import load_dotenv
from agents import Agent, trace, Runner

load_dotenv(override=True)

user_prompt = input("Enter your prompt: ")

agent = Agent(
    name="Joke Teller",
    instructions="You are a joke teller agent. You will tell joke to users",
    model="gpt-4o-mini",
)

async def main():
    with trace("joke-teller"):
        result = await Runner.run(agent, "Tell me a joke.")
        print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())