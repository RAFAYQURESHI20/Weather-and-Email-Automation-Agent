# Weather and Email Automation Agent

An intelligent AI-powered assistant that automates email sending and weather checking through natural language conversations. Built with Streamlit, LangGraph, and Google Gemini.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red.svg)
![LangGraph](https://img.shields.io/badge/LangGraph-0.2.x-green.svg)

---

## ✨ Features

- **🤖 AI-Powered Email Automation**: Send professional emails using natural language commands
- - **🌤️ Real-Time Weather Check**: Get current weather information for any city worldwide
- **💬 Conversational Interface**: Chat-style UI powered by Streamlit
- **🧠 Persistent Memory**: Remembers conversation context within sessions
- **⚡ Fast Response**: Uses Google's Gemini 2.5 Flash model for quick AI responses

---

## 🏗️ Project Structure

```
Weather and Email Automation Agent/
├── app.py                 # Streamlit web application (UI)
├── multi_agent.py        # AI agent with tools (Email + Weather)
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

---

## 📋 Prerequisites

Before running this project, ensure you have:

1. **Python 3.9 or higher** installed
2. **Google Gemini API Key** - Get it from [Google AI Studio](https://aistudio.google.com/app/apikey)
3. **Gmail Account** with App Password enabled
4. **Internet connection** for API calls

---

## 🔧 Installation

### 1. Clone or Download the Project

```bash
cd "Weather and Email Automation Agent"
```

### 2. Create a Virtual Environment (Recommended)

```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

### Required API Keys and Credentials

#### 1. Google Gemini API Key
Edit `multi_agent.py` and replace the placeholder:

```python
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY_HERE"
```

#### 2. Gmail App Password
For sending emails, you need to enable 2-Factor Authentication and generate an App Password:

1. Go to your Google Account → Security
2. Enable 2-Step Verification
3. Go to App Passwords (search in settings)
4. Generate a new app password for "Mail"
5. Replace in `multi_agent.py`:

```python
EMAIL = "your-email@gmail.com"
APP_PASSWORD = "your-16-character-app-password"
```

---

## 🚀 Usage

### Run the Application

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

### How to Use

#### Sending an Email
Simply type a message like:
- *"Send an email to john@example.com about the project meeting tomorrow"*
- *"Email Sarah at sarah@company.com confirming the appointment"*

The AI will:
1. Generate a professional email
2. Include appropriate subject and body
3. Send it automatically
4. Confirm the delivery

#### Checking Weather
Ask about weather in any city:
- *"What's the weather in London?"*
- *"Check weather for New York"*
- *"Is it sunny in Dubai today?"*

---

## 🧠 How It Works

### Architecture Overview

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│   Streamlit UI  │────▶│   LangGraph      │────▶│   Google Gemini │
│   (User Input)  │     │   ReAct Agent    │     │   (LLM Brain)   │
└─────────────────┘     └──────────────────┘     └─────────────────┘
                                │
                    ┌───────────┴───────────┐
                    │                       │
            ┌───────▼────────┐    ┌────────▼────────┐
            │ send_email    │    │ get_weather     │
            │ (yagmail)      │    │ (Weather API)   │
            └────────────────┘    └─────────────────┘
```

### Key Components

1. **Streamlit UI (app.py)**
   - Chat interface with message history
   - Session state management for conversation continuity

2. **AI Agent (multi_agent.py)**
   - Uses LangGraph's `create_react_agent` for agentic behavior
   - Powered by Google Gemini 2.5 Flash
   - Implements ReAct (Reasoning + Acting) pattern

3. **Tools**
   - **send_email_tool**: Uses yagmail to send emails via SMTP
   - **get_weather**: Calls weather API to fetch real-time data

4. **Memory**
   - InMemorySaver maintains conversation history within sessions

---

## 📦 Dependencies

```
langgraph          # Agent framework
streamlit          # Web UI
langchain_google_genai  # Google Gemini integration
langchain          # LLM orchestration
yagmail           # Email sending
requests           # HTTP requests for weather API
```

See `requirements.txt` for exact versions.

---

## 🔐 Security Notes

- **Never commit** your API keys or passwords to version control
- Consider using environment variables for sensitive data in production
- The current credentials in the code are for demonstration only
- App passwords are different from your regular Gmail password

---

## 🛠️ Troubleshooting

### Common Issues

**1. Email not sending**
- Verify App Password is correct
- Check that 2-Factor Authentication is enabled on Gmail

**2. Weather API error**
- Ensure you have an active internet connection
- The weather API endpoint may be temporarily unavailable

**3. Gemini API error**
- Verify your API key is valid and has quota remaining
- Check API key permissions in Google AI Studio

---



## 👤 Author

**Abdul Rafay**

---

## 🙏 Acknowledgments

- [LangGraph](https://langchain-ai.github.io/langgraph/) - Agent framework
- [Streamlit](https://streamlit.io/) - UI framework
- [Google Gemini](https://gemini.google.com/) - AI model
- [yagmail](https://github.com/kootenpv/yagmail) - Email automation

