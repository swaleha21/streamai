import streamlit as st
import pandas as pd
from ai_agent import get_response_from_ai_agent

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="GenAI Agent Studio",
    page_icon="🤖",
    layout="centered"
)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("## 🤖 GenAI Agent Studio")
    uploaded_file = st.file_uploader(
        "📂 Upload Dataset",
        type=["csv"]
    )

# ---------------- MAIN UI ----------------
st.title("🤖 GenAI Agent Studio")
st.subheader("Create and interact with AI agents")

# ---------------- AGENT PROMPT ----------------
agent_prompt = st.text_area(
    "🧠 Define Your AI Agent",
    height=120,
    placeholder=(
        "You are a helpful AI assistant. "
        
    )
)

user_query = st.text_input(
    "💬 Ask Your Question",
    placeholder="Ask anything or ask about the uploaded dataset..."
)

# ---------------- DATASET CONTEXT ----------------
dataset_context = None

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ Dataset uploaded successfully")
    st.write("Preview of dataset:")
    st.dataframe(df)

    dataset_context = (
        f"Columns: {list(df.columns)}\n"
        f"Number of rows: {len(df)}\n"
        f"Sample data:\n{df.head(5).to_string()}"
    )

# ---------------- ACTION ----------------
if st.button("🚀 Generate Response"):
    if agent_prompt and user_query:
        with st.spinner("Thinking... 🤖"):
            response = get_response_from_ai_agent(
                user_query=user_query,
                system_prompt=agent_prompt,
                dataset_context=dataset_context,
                provider="groq"
            )

        st.markdown("### 🤖 AI Response")
        st.write(response)
    else:
        st.warning("⚠️ Please define the AI agent and enter a question.")

# ---------------- FOOTER ----------------
st.divider()
st.caption("© 2026 GenAI Agent Studio | Built by Swaleha Sutar")
