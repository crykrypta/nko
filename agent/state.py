from typing import Annotated, Sequence
from typing_extensions import TypedDict

from langchain_core.messages import BaseMessage

from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph


class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]


workflow = StateGraph(AgentState)
