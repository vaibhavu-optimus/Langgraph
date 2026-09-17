from typing import TypedDict, List
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    values: List[int]
    name: str
    result: str

def process_value(state: AgentState) -> AgentState:
    """This is the function to compute the sum of all the numbers in values"""
    state["result"] = f"The sum is {sum(state["values"])}"
    return state

graph = StateGraph(AgentState)

graph.add_node("process", process_value)
graph.set_entry_point("process")
graph.set_finish_point("process")

app = graph.compile()

answer = app.invoke({"values": [1,2,3,4,5], "name": "Bob"})
print(answer["result"])