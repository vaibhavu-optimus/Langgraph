from typing import TypedDict, List
from langgraph.graph import StateGraph
import math

class Node(TypedDict):
    name: str
    operation: str
    values: List[int]
    result: int

def perform_operation(node: Node) -> Node:
    if node['operation'] == 'sum':
        node['result'] = sum(node['values'])
    elif node['operation'] == 'multiply':
        node['result'] = math.prod(node['values'])
    else:
        raise ValueError(f"Unsupported operation: {node['operation']}")
    return node

graph = StateGraph(Node)

graph.add_node("perform_operation", perform_operation)
graph.set_entry_point("perform_operation")
graph.set_finish_point("perform_operation")

app = graph.compile()

answer = app.invoke({"name": "sum_node", "operation": "sum", "values": [1, 2, 3], "result": 0})
print(answer["result"])  # Output: 6

answer = app.invoke({"name": "multiply_node", "operation": "multiply", "values": [1, 2, 3, 4], "result": 0})
print(answer["result"])  # Output: 24