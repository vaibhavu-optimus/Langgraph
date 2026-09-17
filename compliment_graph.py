from typing import Dict, TypedDict
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    message: str


def compliment(state: AgentState) -> AgentState :
    state["message"] = state["message"] + ", you are doing great!"
    return state

graph = StateGraph(AgentState)

graph.add_node("compliment", compliment)
graph.set_entry_point("compliment")
graph.set_finish_point("compliment")

app = graph.compile()

result = app.invoke({"message" : "Bob"})
print(result["message"])