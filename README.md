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

## Setup
git clone <your-repo-url>
cd hr-leave-agent