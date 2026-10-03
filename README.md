# HR Leave Policy Agent

An AI-powered HR assistant that answers company leave policy questions using a LangGraph-based tool-calling agent.

## Features

- LangGraph agent with multi-step reasoning
- Tool calling for policy lookup and calculations
- Multi-turn conversation memory
- Streamlit chat interface
- Clean modular project structure

## Supported Queries

- Casual / Sick / Maternity / Paternity leave policy
- Convert leave duration from weeks to days
- Calculate remaining leaves

## Tech Stack

- Python
- LangGraph
- LangChain
- Groq LLM
- Streamlit

## Project Structure

```text
hr-leave-agent/
├── agent/
│   ├── __init__.py
│   ├── tools.py
│   ├── graph.py
│   └── prompts.py
├── app.py
├── requirements.txt
├── .env.example
└── README.md
```

# HR Leave Agent 🤖

An intelligent HR assistant powered by **LangGraph** and **Streamlit** that helps employees understand leave policies and calculate their remaining leave balances dynamically.

---

## 🚀 Setup & Installation

Follow these steps to get the project running locally on your machine.

### 1. Clone the Repository

```bash
git clone git@github.com:sainisushilk/example-AI-agent.git
cd example-AI-agent
```

### 2. Create a Virtual Environment

```bash
# Create the environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate  
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Environment

Create a file named `.env` in the root directory of the project and add your API key:

```text
GROQ_API_KEY=your_groq_api_key
```

### 5. Run the Application

```bash
streamlit run app.py
```

---

## ❓ Example Questions

You can test the agent's capabilities with these sample queries:

- "What is the maternity leave policy?"
- "Convert that to days."
- "If total casual leave is 12 and used is 4, how many remain?"
- "What is the sick leave policy?"

---

## 🛠️ How It Works

1. **User Input:** The user asks a question via the Streamlit chat UI.
2. **Agent Routing:** The **LangGraph** agent analyzes the prompt and determines if a specific tool is required.
3. **Tool Execution:** Specialized tools either fetch corporate policy information or perform numerical leave calculations.
4. **Response Generation:** The agent synthesizes the tool outputs to return a natural-language answer.
5. **Context Retention:** The conversation history is preserved, enabling seamless follow-up questions.

---

## 🔮 Future Improvements

- [ ] Connect real HR policy PDFs using **RAG (Retrieval-Augmented Generation)**.

- [ ] Add an automated leave request form generation tool.

- [ ] Implement secure user authentication.

- [ ] Deploy the application publicly on **Streamlit Cloud** or **Hugging Face Spaces**.

- [ ] Implement comprehensive logging and evaluation tracking for agent responses.