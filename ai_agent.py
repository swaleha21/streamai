import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def get_response_from_ai_agent(
    user_query: str,
    system_prompt: str,
    dataset_context: str | None = None,
    provider: str = "groq"
):
    """
    AI assistant with optional dataset awareness.
    Falls back safely if model issues occur.
    """

    if provider == "groq":
        client = OpenAI(
            api_key=os.getenv("GROQ_API_KEY"),
            base_url="https://api.groq.com/openai/v1"
        )
        model = "llama-3.1-8b-instant"   # ✅ STABLE MODEL

    else:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        model = "gpt-4o-mini"

    messages = [{"role": "system", "content": system_prompt}]

    if dataset_context:
        messages.append({
            "role": "system",
            "content": (
                "A dataset has been uploaded. "
                "Answer strictly using this dataset only.\n\n"
                f"{dataset_context}"
            )
        })

    messages.append({"role": "user", "content": user_query})

    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"⚠️ AI service error: {str(e)}"
