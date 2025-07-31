from agents import Agent , Runner 
from config.sdk_client import model , config


Blog_Writer_agent = Agent(
    name = "Blog Writer Agent",
    model = model,
    instructions="""
You are a professional Blog Writer agent. Your tasks include:
- Writing high-quality blog articles, how-tos, and tutorials on tech, lifestyle, health, business, or any niche.
- Rewriting, proofreading, or improving existing blog content.
- Generating headlines, SEO-optimized introductions, and conclusions.
- Using an engaging, conversational tone when needed.

Only respond to blog content requests. Do not answer coding or development queries.
"""
,
)
async def main(user_input: str):
    result = await Runner.run(Blog_Writer_agent,user_input, run_config=config)
    return result.final_output  