import streamlit as st
import asyncio

from agents import Agent, Runner
from config.sdk_client import model, config
from multi.app_developer_agent import App_Developer_agent
from multi.blog_writer_agent import Blog_Writer_agent
from multi.web_developer_agent import Developer_agent

# Dictionary for all agents
AGENT_MAP = {
    "App Developer Agent": App_Developer_agent,
    "Blog Writer Agent": Blog_Writer_agent,
    "Web Developer Agent": Developer_agent
}

# Orchestrator decides only which agent to call
Orchestrator = Agent(
    name="Orchestrator Agent",
    model=model,
    instructions="""
You are an Orchestrator agent. Your job is to analyze the user's input and decide which specialized agent should handle it.
Respond ONLY with one of the following EXACT names:
- App Developer Agent
- Blog Writer Agent
- Web Developer Agent
Do not explain. Do not solve the task yourself. Just return the exact name.
""",
    handoffs=[App_Developer_agent, Blog_Writer_agent, Developer_agent]
)

# Async functions
async def get_agent_name(user_input: str):
    result = await Runner.run(Orchestrator, user_input, run_config=config)
    return result.final_output.strip()

async def get_agent_response(agent: Agent, user_input: str):
    result = await Runner.run(agent, user_input, run_config=config)
    return result.final_output

# Streamlit UI
st.title("🤖 Multi-Agent Assistant")
user_input = st.text_area("💬 Ask your question or task here:", height=150)

if st.button("Run"):
    if not user_input.strip():
        st.warning("⚠️ Please enter something first.")
    else:
        with st.spinner("🧠 Choosing the best agent..."):
            selected_agent_name = asyncio.run(get_agent_name(user_input))

        if selected_agent_name in AGENT_MAP:
            agent = AGENT_MAP[selected_agent_name]
            with st.spinner(f"📡 {selected_agent_name} is working..."):
                final_output = asyncio.run(get_agent_response(agent, user_input))
            
            st.success(f"✅ Task handled by: {selected_agent_name}")
            st.markdown("### 📝 Result:")
            st.code(final_output)
        else:
            st.error(f"❌ Orchestrator returned unknown agent: {selected_agent_name}")
