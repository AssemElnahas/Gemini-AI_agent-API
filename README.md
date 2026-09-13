# 🤖 Gemini AI Agent API

A Python-based **AI Agent API** powered by Google's Gemini LLM.

This project demonstrates how to build an AI agent from scratch with Python, connect it to Gemini, add custom tools, use a simple RAG system, and expose the agent through a REST API using FastAPI.

The project is designed as a **portfolio-ready foundation for AI Agent development**.

---

## 🚀 Features

* 🤖 Gemini LLM integration
* 🧠 AI Agent architecture
* 🔎 Basic RAG (Retrieval-Augmented Generation)
* 🛠️ Custom AI tools
* ⚡ FastAPI REST API
* 🔐 Environment variables for API keys
* 📄 `.env.example` configuration
* 📦 Python virtual environment support
* 🧪 Easy API testing with Swagger UI
* 🏗️ Modular project structure

---

## 🧰 Tech Stack

| Technology    | Purpose                     |
| ------------- | --------------------------- |
| Python        | Core programming language   |
| Gemini API    | Large Language Model        |
| FastAPI       | Backend REST API            |
| Pydantic      | Request/response validation |
| RAG           | Knowledge retrieval         |
| python-dotenv | Environment configuration   |
| Uvicorn       | API server                  |

---

## 📁 Project Structure

All project files are located directly in the repository root.

```text
.
├── agent.py
├── config.py
├── main.py
├── rag.py
├── tools.py
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
├── LICENSE
└── README.md
```

### File Description

#### `main.py`

The FastAPI entry point.

It creates the API application and exposes the agent through HTTP endpoints.

#### `agent.py`

Contains the main AI Agent logic.

Responsible for:

* Receiving user prompts
* Communicating with Gemini
* Using tools
* Calling RAG when necessary
* Returning the final response

#### `tools.py`

Contains custom tools that the AI agent can use.

You can extend this file with tools such as:

* Calculator
* Database search
* Web search
* Product lookup
* File search
* Business logic

#### `rag.py`

Contains the Retrieval-Augmented Generation logic.

The RAG component can retrieve information from your knowledge source and provide relevant context to Gemini.

#### `config.py`

Handles project configuration and environment variables.

Sensitive credentials should **never be hardcoded** into the source code.

#### `requirements.txt`

Contains the Python dependencies required to run the project.

---

# ⚙️ Installation

## 1. Install Python

Download Python from the official Python website:

https://www.python.org/downloads/

Python **3.11+** is recommended for this project.

Verify the installation:

```bash
python --version
```

or:

```bash
py --version
```

---

## 2. Clone the Repository

Clone the GitHub repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Enter the project directory:

```bash
cd YOUR_REPOSITORY_NAME
```

---

## 3. Create a Virtual Environment

Create a virtual environment:

```bash
python -m venv venv
```

### Windows PowerShell

Activate it with:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate again:

```powershell
.\venv\Scripts\Activate.ps1
```

### Windows CMD

Alternatively:

```cmd
venv\Scripts\activate
```

You should see:

```text
(venv)
```

at the beginning of your terminal.

---

# 📦 Install Dependencies

Install all required packages:

```bash
pip install -r requirements.txt
```

If `pip` needs to be upgraded:

```bash
python -m pip install --upgrade pip
```

Then:

```bash
pip install -r requirements.txt
```

---

# 🔑 Gemini API Key

This project requires a Gemini API key.

Create your API key through Google's Gemini API / AI Studio platform.

After obtaining your key, create a file named:

```text
.env
```

in the project root.

Example:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### Important

Never upload your real `.env` file or API key to GitHub.

Your `.gitignore` should contain:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

Use `.env.example` as the public template:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

---

# ▶️ Run the API

Start the FastAPI server with:

```bash
uvicorn main:app --reload
```

You should see something similar to:

```text
Uvicorn running on http://127.0.0.1:8000
```

---

# 🌐 API Documentation

FastAPI automatically provides interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

You can use Swagger UI to test the AI Agent API directly from your browser.

Alternative documentation:

```text
http://127.0.0.1:8000/redoc
```

---

# 🔌 Example API Request

Depending on your implementation, an endpoint can accept a request similar to:

```json
{
    "message": "What is artificial intelligence?"
}
```

Example using `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/chat" \
-H "Content-Type: application/json" \
-d "{\"message\":\"What is artificial intelligence?\"}"
```

The agent processes the request, communicates with Gemini, optionally uses its tools/RAG system, and returns the generated response.

---

# 🧠 How the Agent Works

The general architecture is:

```text
                    User
                      │
                      ▼
                FastAPI API
                      │
                      ▼
                 AI Agent
                      │
             ┌────────┴────────┐
             ▼                 ▼
          Gemini              Tools
             │                 │
             │                 ├── Calculator
             │                 ├── Database
             │                 └── Other Tools
             │
             ▼
             RAG
             │
             ▼
       Relevant Context
             │
             └──────────┐
                        ▼
                  Final Response
                        │
                        ▼
                       User
```

The important concept is that Gemini is not simply being used as a chatbot.

The **agent acts as the orchestration layer** between the user, LLM, tools, and knowledge retrieval system.

---

# 🧪 Testing

Start the server:

```bash
uvicorn main:app --reload
```

Then open:

```text
http://127.0.0.1:8000/docs
```

Use Swagger UI to test the available endpoints.

You can also test the API using tools such as:

* Postman
* cURL
* Python requests
* Frontend applications

---

# 🔮 Future Improvements

This project can be extended into a more advanced production AI Agent.

Possible improvements:

* 🗄️ PostgreSQL / SQL Server integration
* 🔐 JWT authentication
* 👤 User accounts
* 💬 Conversation memory
* 📚 Vector database
* 🔎 Semantic search
* 🌐 Web search tool
* 📄 PDF document RAG
* 🧠 Long-term agent memory
* 🛒 E-commerce/product tools
* 📊 Admin dashboard
* 🔗 Frontend integration
* 📱 Mobile application
* ☁️ Cloud deployment
* 🐳 Docker support
* 🔄 Background tasks
* 📈 Logging and monitoring

---

# 🎯 Example Use Cases

This architecture can be adapted to build:

### Customer Support Agent

```text
Customer
   ↓
AI Agent
   ↓
Product Database + RAG
   ↓
Gemini
   ↓
Customer Response
```

### E-Commerce Agent

The agent can:

* Search products
* Check stock
* Recommend products
* Answer product questions
* Retrieve order information

### Company Knowledge Agent

The agent can answer questions using:

* Company documents
* PDFs
* FAQs
* Policies
* Internal knowledge bases

---

# 🔐 Security

Never commit sensitive credentials.

Do not upload:

```text
.env
```

or any file containing:

```text
GEMINI_API_KEY
```

Use:

```text
.env.example
```

to document the required environment variables.

---

# 📌 Development Status

**Status:** 🚧 Active Development

This repository is currently a foundation for building and experimenting with Gemini-powered AI Agents.

---

# 👨‍💻 Author

**Assem Elnahas**

Computer Science Graduate
AI & Backend Developer

GitHub: **AssemElnahas**

---

# 📄 License

This project is licensed under the terms specified in the `LICENSE` file.

---

⭐ If you find this project useful, consider giving the repository a star!
