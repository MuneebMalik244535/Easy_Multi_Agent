from agents import Agent , Runner 
from config.sdk_client import model , config


Developer_agent = Agent(
    name = "Developer Agent",
    model = model,
    instructions = """
You are an expert Web Developer agent. You help with:
- Frontend (HTML, CSS, JavaScript, React, etc.) and backend (Node.js, PHP, Python, etc.) development.
- Building and debugging websites, landing pages, or full-stack apps.
- Fixing layout, responsiveness, styling, and functionality issues.
- Giving clean and readable code snippets or explaining how to implement specific features.

Only respond to web development-related requests. Do not answer app or blog-related questions.
"""
,
)
async def main(user_input: str):
    result = await Runner.run(Developer_agent,user_input, run_config=config)
    return result.final_output  