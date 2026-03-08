from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.memory import InMemorySaver
import yagmail
import requests

# -------------------------------
# API & Email Config
# -------------------------------
GEMINI_API_KEY = "AIzaSyDdb-w5Ef74igAXwZZK_i_t7sqIzaq99BU"
EMAIL = "batch22.ai.010@gmail.com"
APP_PASSWORD = "biom jhko vsmd fgjz"

yag = yagmail.SMTP(user=EMAIL, password=APP_PASSWORD)

# -------------------------------
# Weather API
# -------------------------------
WEATHER_API_URL = "https://p2pclouds.up.railway.app/v1/learn/weather"

# -------------------------------
# LLM Config
# -------------------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GEMINI_API_KEY,
    temperature=0
)

# -------------------------------
# Email Tool
# -------------------------------
def send_email_tool(recipient: str, subject: str, body: str) -> str:
    """
    Sends email to a recipient with subject and body.
    """
    yag.send(to=recipient, subject=subject, contents=body)
    return f"✅ Email sent successfully to {recipient}"

# -------------------------------
# Weather Tool
# -------------------------------
def get_weather(city: str) -> str:
    """
    Fetches weather information for a given city using the weather API.
    """
    try:
        response = requests.get(WEATHER_API_URL, params={"city": city})
        if response.status_code == 200:
            data = response.json()
            return f"🌤️ Weather in {city}: {data}"
        else:
            return f"❌ Could not fetch weather for {city}"
    except Exception as e:
        return f"❌ Error: {str(e)}"

# -------------------------------
# Memory
# -------------------------------
memory = InMemorySaver()

# -------------------------------
# System Prompt
# -------------------------------
prompt = """
You are an intelligent AI assistant working on behalf of Abdul Rafay.

You have two tools:
1. send_email_tool - Send emails
2. get_weather - Check weather for any city

Your responsibilities:
- Write clear, concise, and professional emails when asked.
- Check weather information when asked about weather.

Instructions for Email:
1. If the user asks to send an email, generate a professional email.
2. Keep the email short and clear.
3. Include a proper subject line.
4. End the email with: Best regards, Abdul Rafay
5. Use the send_email_tool to send.

Instructions for Weather:
1. If the user asks about weather, use the get_weather tool.
2. Present weather information clearly.

IMPORTANT:
- Your responses in the UI must be short and clear.
- For emails: respond with 'Email sent successfully' once the tool runs.
- For weather: respond with the weather information clearly.
"""

# -------------------------------
# Create Agent (with both tools)
# -------------------------------
agent = create_react_agent(
    model=llm,
    tools=[send_email_tool, get_weather],
    prompt=prompt,
    checkpointer=memory
)

# -------------------------------
# Agent Function
# -------------------------------
def run_agent(user_input):
    inputs = {"messages": [{"role": "user", "content": user_input}]}
    config = {"configurable": {"thread_id": "email-thread"}}
    final_response = ""

    for chunk in agent.stream(inputs, config=config, stream_mode="updates"):
        # Capture tool output
        if "tool_outputs" in chunk and chunk["tool_outputs"]:
            final_response = chunk["tool_outputs"][-1]["output"]

        # Capture AI response from agent node (stream_mode="updates" uses node names as keys)
        if "agent" in chunk:
            for msg in chunk["agent"].get("messages", []):
                if hasattr(msg, "content") and msg.content:
                    final_response = msg.content

    return final_response
