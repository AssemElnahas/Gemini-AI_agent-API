# 🤖 Gemini AI Agent

A modular AI Agent backend built with **Python, Google Gemini, FastAPI, RAG, and tools**.

This project demonstrates how to build an AI agent from scratch, connect it to a Gemini LLM, give it tools, and expose it through a REST API.

---

# 📋 Requirements

Before starting, make sure you have:

* Windows 10/11
* Internet connection
* VS Code
* Git
* Python 3.11+ recommended
* A Google Gemini API key

---

# 🐍 1. Install Python

Download Python from the official Python website:

https://www.python.org/downloads/windows/

For AI/ML compatibility, **Python 3.11 or 3.12 is recommended** for this project.

During installation:

1. Open the Python installer.
2. Enable:

```text
Add python.exe to PATH
```

3. Click:

```text
Install Now
```

After installation, open a **new** PowerShell or CMD window.

Check Python:

```powershell
python --version
```

Example:

```text
Python 3.11.x
```

Check pip:

```powershell
python -m pip --version
```

If `python` does not work, try:

```powershell
py --version
```

---

# 📦 2. Install Git

Download Git from:

https://git-scm.com/downloads

Verify the installation:

```powershell
git --version
```

Example:

```text
git version 2.x.x
```

---

# 💻 3. Clone the Repository

Open PowerShell or the VS Code terminal.

Clone the project:

```powershell
git clone https://github.com/AssemElnahas/gemini-agent.git
```

Enter the project:

```powershell
cd gemini-agent
```

Check the files:

```powershell
dir
```

You should see something similar to:

```text
.env.example
.gitignore
LICENSE
README.md
requirements.txt
main.py
agent.py
tools.py
RAG.py
```

---

# 🧪 4. Create a Virtual Environment

A virtual environment keeps this project's Python packages isolated from your other projects.

Run:

```powershell
python -m venv venv
```

This creates:

```text
gemini-agent/
└── venv/
```

---

# ▶️ 5. Activate the Virtual Environment

### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

After activation, your terminal should look similar to:

```text
(venv) PS D:\Github repos\gemini-agent>
```

### If PowerShell blocks the activation script

You may see:

```text
Activate.ps1 cannot be loaded because running scripts is disabled
```

Use CMD instead:

```cmd
venv\Scripts\activate.bat
```

Or allow locally created scripts for your Windows user:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate again:

```powershell
.\venv\Scripts\Activate.ps1
```

---

# 📚 6. Upgrade pip

With the virtual environment activated:

```powershell
python -m pip install --upgrade pip
```

Verify:

```powershell
pip --version
```

---

# 📥 7. Install Project Dependencies

The project contains a `requirements.txt` file.

Install everything with:

```powershell
pip install -r requirements.txt
```

You can verify installed packages:

```powershell
pip list
```

---

# 🔑 8. Get a Gemini API Key

The agent uses Google's Gemini API.

Create a Gemini API key through **Google AI Studio**:

https://aistudio.google.com/

Sign in with your Google account and create an API key.

### ⚠️ Important

Never put your API key directly inside your Python code.

Don't do this:

```python
GEMINI_API_KEY = "your-real-api-key"
```

Instead, use an environment variable.

---

# 🔐 9. Configure Environment Variables

The repository contains:

```text
.env.example
```

Create a new file named:

```text
.env
```

Your structure should be:

```text
gemini-agent/
│
├── .env
├── .env.example
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
│
├── main.py
├── agent.py
├── tools.py
├── RAG.py
│
└── data/
```

Inside `.env`:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Replace:

```text
your_gemini_api_key_here
```

with your real API key.

---

# 🛡️ 10. Protect Your API Key

Make sure `.gitignore` contains:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

Your `.env` file should **never** be uploaded to GitHub.

Check Git status:

```powershell
git status
```

You should not see `.env` listed as a file to commit.

---

# 🧠 11. Project Structure

The project is organized into several components:

```text
gemini-agent/
│
├── .env
├── .env.example
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
│
├── main.py
├── agent.py
├── tools.py
├── RAG.py
│
├── data/
│   └── knowledge_base.txt
│
└── venv/
```

### `main.py`

The FastAPI application.

Responsible for exposing the agent through API endpoints.

### `agent.py`

Contains the AI Agent logic and Gemini integration.

### `tools.py`

Contains functions/tools that the AI agent can use.

Examples:

```text
Calculator
Database Search
Product Search
Stock Checker
Web Search
```

### `RAG.py`

Handles Retrieval-Augmented Generation.

It allows the agent to retrieve information from a knowledge base before generating an answer.

### `.env`

Stores secret configuration such as the Gemini API key.

### `requirements.txt`

Contains the Python dependencies required by the project.

---

# 🚀 12. Run the Project

Make sure your virtual environment is activated:

```powershell
.\venv\Scripts\Activate.ps1
```

Then start the FastAPI server:

```powershell
uvicorn main:app --reload
```

You should see something similar to:

```text
INFO:     Uvicorn running on http://127.0.0.1:8000
```

Your backend is now running.

---

# 🌐 13. Open the API

Open your browser:

http://127.0.0.1:8000

You can also use:

```text
http://localhost:8000
```

---

# 📖 14. Open FastAPI Swagger UI

FastAPI automatically provides interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

You should see the Swagger interface.

From there you can:

1. Select an endpoint.
2. Click **Try it out**.
3. Enter your request.
4. Click **Execute**.
5. View the AI agent response.

---

# 🧪 15. Test the Agent

For example, if your API contains:

```text
POST /chat
```

You can send:

```json
{
    "message": "Explain what an AI agent is."
}
```

The request flow is:

```text
Client
   │
   ▼
FastAPI
   │
   ▼
AI Agent
   │
   ▼
Gemini
   │
   ▼
Response
```

---

# 🔄 16. Run the Project Again

Every time you open the project:

### Step 1 — Open the project

```powershell
cd "D:\Github repos\gemini-agent"
```

### Step 2 — Activate the environment

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 3 — Run FastAPI

```powershell
uvicorn main:app --reload
```

### Step 4 — Open Swagger

```text
http://127.0.0.1:8000/docs
```

---

# 🛑 17. Stop the Server

To stop FastAPI:

```text
CTRL + C
```

To deactivate the virtual environment:

```powershell
deactivate
```

---

# 🔧 Troubleshooting

## Python is not recognized

Try:

```powershell
py --version
```

If `py` works, you can create the environment using:

```powershell
py -3.11 -m venv venv
```

If neither works, reinstall Python and make sure:

```text
Add python.exe to PATH
```

is enabled.

---

## PowerShell cannot activate venv

Run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then:

```powershell
.\venv\Scripts\Activate.ps1
```

---

## `pip install` fails

First upgrade pip:

```powershell
python -m pip install --upgrade pip
```

Then:

```powershell
pip install -r requirements.txt
```

---

## Gemini API key error

Check that `.env` exists:

```text
gemini-agent/
└── .env
```

And contains:

```env
GEMINI_API_KEY=your_api_key
```

Also make sure your Python application loads environment variables correctly.

---

## Port 8000 is already being used

Run FastAPI on another port:

```powershell
uvicorn main:app --reload --port 8001
```

Then open:

```text
http://127.0.0.1:8001/docs
```

---

# 🏗️ AI Agent Architecture

The long-term architecture of this project is:

```text
                     ┌───────────────┐
                     │     User      │
                     └───────┬───────┘
                             │
                             ▼
                     ┌───────────────┐
                     │    FastAPI    │
                     └───────┬───────┘
                             │
                             ▼
                     ┌───────────────┐
                     │  AI Agent     │
                     └───────┬───────┘
                             │
                 ┌───────────┼───────────┐
                 │           │           │
                 ▼           ▼           ▼
              Gemini        RAG        Tools
                 │           │           │
                 └───────────┼───────────┘
                             │
                             ▼
                     ┌───────────────┐
                     │   Response    │
                     └───────────────┘
```

---

# 🗺️ Roadmap

## Phase 1 — Foundation

* [x] Python setup
* [x] Virtual environment
* [x] Gemini integration
* [x] Environment variables
* [x] FastAPI
* [x] Basic API

## Phase 2 — AI Agent

* [ ] Agent reasoning
* [ ] Tool calling
* [ ] Multiple tools
* [ ] Error handling
* [ ] Conversation memory

## Phase 3 — RAG

* [ ] Document loading
* [ ] Text chunking
* [ ] Embeddings
* [ ] Vector database
* [ ] Semantic search
* [ ] Context-aware responses

## Phase 4 — Production

* [ ] Authentication
* [ ] Database
* [ ] User sessions
* [ ] Logging
* [ ] Testing
* [ ] Docker
* [ ] Cloud deployment

## Phase 5 — Integrations

* [ ] Facebook Messenger
* [ ] WhatsApp
* [ ] E-commerce systems
* [ ] Customer support platforms
* [ ] Business databases

---

# 🧰 Technologies

| Technology      | Purpose                   |
| --------------- | ------------------------- |
| Python          | Core development          |
| Gemini          | Large Language Model      |
| FastAPI         | Backend/API               |
| Pydantic        | Data validation           |
| RAG             | Knowledge retrieval       |
| Vector Database | Semantic search           |
| Git             | Version control           |
| Swagger         | API testing/documentation |

---

# 🎯 Project Goal

The goal of this project is to understand how modern AI agents are built:

```text
LLM
 ↓
Agent
 ↓
Tools
 ↓
RAG
 ↓
Memory
 ↓
API
 ↓
Real-world Application
```

The final goal is to transform this project from a simple Gemini chatbot into a **production-ready AI Agent backend** capable of interacting with external systems and business data.

---

# 👨‍💻 Author

**Assem Elnahas**

Computer Science Graduate | AI & Backend Developer

GitHub:
https://github.com/AssemElnahas

LinkedIn:
https://www.linkedin.com/in/assem-elnahas-28887429/

---

# 📜 License

This project is licensed under the MIT License.

See the `LICENSE` file for details.
