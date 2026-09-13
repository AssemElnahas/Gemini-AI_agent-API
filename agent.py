from google import genai

from app.config import GEMINI_API_KEY, GEMINI_MODEL
from app.rag import retrieve_context
from app.tools import (
    get_current_time,
    search_product,
    check_stock,
    calculate_total,
)


# --------------------------------------------------
# Gemini Client
# --------------------------------------------------

client = genai.Client(
    api_key=GEMINI_API_KEY
)


# --------------------------------------------------
# Agent Tools
# --------------------------------------------------

TOOLS = [
    get_current_time,
    search_product,
    check_stock,
    calculate_total,
]


# --------------------------------------------------
# System Instructions
# --------------------------------------------------

SYSTEM_INSTRUCTION = """
You are Gemini Customer Support Agent.

Your job is to help customers with:
- Products
- Prices
- Stock availability
- Product sizes
- Orders
- Returns
- Shipping
- General customer support

Rules:

1. Use the knowledge base when answering company-related questions.
2. Use tools when you need real-time or structured information.
3. Never invent product information.
4. If information is unavailable, clearly tell the customer.
5. Be helpful, concise, and professional.
6. Do not expose internal tools or implementation details.
"""


# --------------------------------------------------
# Agent Function
# --------------------------------------------------

def ask_agent(message: str) -> str:
    """
    Send a user message to the Gemini agent.

    The agent receives:
    - System instructions
    - RAG context
    - Available tools
    - User message
    """

    # Retrieve relevant information from knowledge base
    context = retrieve_context(message)

    prompt = f"""
Knowledge Base Context:
{context}

Customer Message:
{message}
"""

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config={
            "system_instruction": SYSTEM_INSTRUCTION,
            "tools": TOOLS,
        },
    )

    return response.text
