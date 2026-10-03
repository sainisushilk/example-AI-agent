import os
from typing import TypedDict, Annotated, Sequence
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.messages import BaseMessage, SystemMessage, HumanMessage
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from langgraph.graph.message import add_messages

from agent.tools import get_tools
from agent.prompts import SYSTEM_PROMPT

load_dotenv()


class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]


def build_agent():
    tools = get_tools()

    llm = ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=0,
        groq_api_key=os.getenv("GROQ_API_KEY"),
    )
    llm_with_tools = llm.bind_tools(tools)

    def agent_node(state: AgentState):
        messages = list(state["messages"])
        if not any(isinstance(m, SystemMessage) for m in messages):
            messages = [SystemMessage(content=SYSTEM_PROMPT)] + messages
        response = llm_with_tools.invoke(messages)
        return {"messages": [response]}

    tool_node = ToolNode(tools)

    def should_continue(state: AgentState):
        last_message = state["messages"][-1]
        if getattr(last_message, "tool_calls", None):
            return "tools"
        return END

    graph = StateGraph(AgentState)
    graph.add_node("agent", agent_node)
    graph.add_node("tools", tool_node)
    graph.set_entry_point("agent")
    graph.add_conditional_edges("agent", should_continue)
    graph.add_edge("tools", "agent")

    return graph.compile()


def run_agent(question: str, history: list[BaseMessage] | None = None):
    app = build_agent()

    if history is None:
        history = [SystemMessage(content=SYSTEM_PROMPT)]

    history = list(history) + [HumanMessage(content=question)]
    result = app.invoke({"messages": history})

    new_history = result["messages"]
    final_answer = new_history[-1].content
    return final_answer, new_history