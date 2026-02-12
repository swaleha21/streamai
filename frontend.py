from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from ai_agent import get_response_from_ai_agent
# ---------------- UI Setup ----------------
st.set_page_config(page_title="LangGraph Agent UI", layout="centered")
st.title("🤖 AI Chatbot Agents")
st.write("Create and Interact with the AI Agents!")
system_prompt = st.text_area(
    "Define your AI Agent:",
    height=70,
    placeholder="Type your system prompt here..."
)
MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]
provider = st.radio("Select Provider:", ("Groq", "OpenAI"))
if provider == "Groq":
    selected_model = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)
else:
    selected_model = st.selectbox("Select OpenAI Model:", MODEL_NAMES_OPENAI)
allow_web_search = st.checkbox("Allow Web Search")
user_query = st.text_area(
    "Enter your query:",
    height=150,
    placeholder="Ask anything!"
)
# ---------------- Run Agent ----------------
if st.button("🚀 Ask Agent!"):
    if not user_query.strip():
        st.warning("Please enter a query.")
    else:
        with st.spinner("Thinking... 🤔"):
            response = get_response_from_ai_agent(
                llm_id=selected_model,
                query=user_query,
                allow_search=allow_web_search,
                system_prompt=system_prompt,
                provider=provider
            )
        st.subheader("🧠 Agent Response")
        st.write(response)
